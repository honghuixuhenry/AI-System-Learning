import torch
import torch.nn as nn
import torch.nn.functional as F


# =========================================================
# 1. RMSNorm
# =========================================================

class RMSNorm(nn.Module):

    def __init__(
        self,
        dim,
        eps=1e-6
    ):
        super().__init__()

        self.weight = nn.Parameter(
            torch.ones(dim)
        )

        self.eps = eps


    def forward(
        self,
        x
    ):

        # Keep original dtype, such as:
        # float32 / float16 / bfloat16
        input_dtype = x.dtype

        # Compute normalization in float32
        # for better numerical stability.
        x_float = x.float()

        rms_inv = torch.rsqrt(
            x_float
            .pow(2)
            .mean(
                dim=-1,
                keepdim=True
            )
            +
            self.eps
        )

        normalized = (
            x_float
            *
            rms_inv
        )

        normalized = normalized.to(
            input_dtype
        )

        return (
            normalized
            *
            self.weight
        )


# =========================================================
# 2. RoPE
# =========================================================

def build_rope_cache(
    seq_len,
    head_dim,
    base,
    device
):

    if head_dim % 2 != 0:
        raise ValueError(
            "head_dim must be even "
            "for this RoPE implementation."
        )

    # Example:
    #
    # head_dim = 8
    #
    # indices:
    # [0, 2, 4, 6]
    #
    # normalized:
    # [0/8, 2/8, 4/8, 6/8]

    indices = torch.arange(
        0,
        head_dim,
        2,
        device=device,
        dtype=torch.float32
    )

    inv_freq = (
        1.0
        /
        (
            base
            **
            (
                indices
                /
                head_dim
            )
        )
    )

    # positions:
    # (T,)
    positions = torch.arange(
        seq_len,
        device=device,
        dtype=torch.float32
    )

    # angles:
    #
    # (T, head_dim / 2)
    angles = torch.outer(
        positions,
        inv_freq
    )

    cos = angles.cos()
    sin = angles.sin()

    return cos, sin


def apply_rope(
    x,
    cos,
    sin
):

    # x:
    # (B, H, T, head_dim)

    if x.shape[-1] % 2 != 0:
        raise ValueError(
            "The last dimension must be even "
            "for this RoPE implementation."
        )

    # Split:
    #
    # even dimensions:
    # x0, x2, x4, ...
    #
    # odd dimensions:
    # x1, x3, x5, ...

    x_even = x[..., 0::2]

    x_odd = x[..., 1::2]

    # cos/sin:
    # (T, head_dim / 2)
    #
    # expand to:
    # (1, 1, T, head_dim / 2)

    cos = cos[
        None,
        None,
        :,
        :
    ]

    sin = sin[
        None,
        None,
        :,
        :
    ]

    rotated_even = (
        x_even * cos
        -
        x_odd * sin
    )

    rotated_odd = (
        x_even * sin
        +
        x_odd * cos
    )

    # Recombine even/odd dimensions.

    output = torch.empty_like(
        x
    )

    output[..., 0::2] = (
        rotated_even
    )

    output[..., 1::2] = (
        rotated_odd
    )

    return output


# =========================================================
# 3. Causal Grouped Query Attention
# =========================================================

class CausalGQAAttention(nn.Module):

    def __init__(
        self,
        config
    ):
        super().__init__()

        self.dim = config.dim

        self.num_q_heads = (
            config.num_q_heads
        )

        self.num_kv_heads = (
            config.num_kv_heads
        )

        self.rope_base = (
            config.rope_base
        )

        # D must be divisible by Hq.
        if (
            self.dim
            %
            self.num_q_heads
            !=
            0
        ):
            raise ValueError(
                "config.dim must be divisible "
                "by config.num_q_heads."
            )

        # GQA requirement:
        #
        # Hq must be divisible by Hkv.
        if (
            self.num_q_heads
            %
            self.num_kv_heads
            !=
            0
        ):
            raise ValueError(
                "config.num_q_heads must be divisible "
                "by config.num_kv_heads."
            )

        self.head_dim = (
            self.dim
            //
            self.num_q_heads
        )

        if self.head_dim % 2 != 0:
            raise ValueError(
                "head_dim must be even "
                "for RoPE."
            )

        self.group_size = (
            self.num_q_heads
            //
            self.num_kv_heads
        )

        # -------------------------------------------------
        # Q projection
        #
        # D -> Hq * head_dim
        #
        # Since:
        #
        # Hq * head_dim = D
        #
        # this is effectively:
        #
        # D -> D
        # -------------------------------------------------

        self.q_proj = nn.Linear(
            self.dim,
            self.num_q_heads
            *
            self.head_dim,
            bias=False
        )

        # -------------------------------------------------
        # K projection
        #
        # D -> Hkv * head_dim
        #
        # Usually smaller than D when using GQA.
        # -------------------------------------------------

        self.k_proj = nn.Linear(
            self.dim,
            self.num_kv_heads
            *
            self.head_dim,
            bias=False
        )

        # -------------------------------------------------
        # V projection
        # -------------------------------------------------

        self.v_proj = nn.Linear(
            self.dim,
            self.num_kv_heads
            *
            self.head_dim,
            bias=False
        )

        # -------------------------------------------------
        # Output projection
        #
        # D -> D
        # -------------------------------------------------

        self.out_proj = nn.Linear(
            self.dim,
            self.dim,
            bias=False
        )


    def forward(
        self,
        x
    ):

        # x:
        # (B, T, D)

        B, T, D = x.shape

        # -------------------------------------------------
        # Q / K / V projections
        # -------------------------------------------------

        q = self.q_proj(
            x
        )

        k = self.k_proj(
            x
        )

        v = self.v_proj(
            x
        )

        # Current shapes:
        #
        # q:
        # (B, T, Hq * head_dim)
        #
        # k:
        # (B, T, Hkv * head_dim)
        #
        # v:
        # (B, T, Hkv * head_dim)

        # -------------------------------------------------
        # Split heads
        # -------------------------------------------------

        q = q.reshape(
            B,
            T,
            self.num_q_heads,
            self.head_dim
        )

        q = q.transpose(
            1,
            2
        )

        # q:
        # (B, Hq, T, head_dim)

        k = k.reshape(
            B,
            T,
            self.num_kv_heads,
            self.head_dim
        )

        k = k.transpose(
            1,
            2
        )

        # k:
        # (B, Hkv, T, head_dim)

        v = v.reshape(
            B,
            T,
            self.num_kv_heads,
            self.head_dim
        )

        v = v.transpose(
            1,
            2
        )

        # v:
        # (B, Hkv, T, head_dim)

        # -------------------------------------------------
        # RoPE
        # -------------------------------------------------

        cos, sin = build_rope_cache(
            seq_len=T,
            head_dim=self.head_dim,
            base=self.rope_base,
            device=x.device
        )

        # Apply RoPE to Q and K.
        #
        # V is not rotated.

        q = apply_rope(
            q,
            cos,
            sin
        )

        k = apply_rope(
            k,
            cos,
            sin
        )

        # -------------------------------------------------
        # GQA expansion
        # -------------------------------------------------
        #
        # Educational implementation:
        #
        # K/V:
        # (B, Hkv, T, head_dim)
        #
        # repeat to:
        # (B, Hq, T, head_dim)
        #
        # Example:
        #
        # Hq = 8
        # Hkv = 2
        #
        # group_size = 4
        #
        # Each KV head is shared by 4 query heads.
        #
        # Important:
        # Real optimized GQA kernels do not necessarily
        # physically duplicate K/V like this.

        k = k.repeat_interleave(
            self.group_size,
            dim=1
        )

        v = v.repeat_interleave(
            self.group_size,
            dim=1
        )

        # Now:
        #
        # q:
        # (B, Hq, T, head_dim)
        #
        # k:
        # (B, Hq, T, head_dim)
        #
        # v:
        # (B, Hq, T, head_dim)

        # -------------------------------------------------
        # Causal Scaled Dot Product Attention
        # -------------------------------------------------

        context = (
            F.scaled_dot_product_attention(
                q,
                k,
                v,
                attn_mask=None,
                dropout_p=0.0,
                is_causal=True
            )
        )

        # context:
        # (B, Hq, T, head_dim)

        # -------------------------------------------------
        # Merge heads
        # -------------------------------------------------

        context = context.transpose(
            1,
            2
        )

        # (B, T, Hq, head_dim)

        context = (
            context
            .contiguous()
            .reshape(
                B,
                T,
                D
            )
        )

        # context:
        # (B, T, D)

        output = self.out_proj(
            context
        )

        # output:
        # (B, T, D)

        return output


# =========================================================
# 4. SwiGLU
# =========================================================

class SwiGLU(nn.Module):

    def __init__(
        self,
        dim,
        hidden_dim
    ):
        super().__init__()

        # Gate branch:
        #
        # D -> D_ff

        self.gate_proj = nn.Linear(
            dim,
            hidden_dim,
            bias=False
        )

        # Content / up branch:
        #
        # D -> D_ff

        self.up_proj = nn.Linear(
            dim,
            hidden_dim,
            bias=False
        )

        # Down projection:
        #
        # D_ff -> D

        self.down_proj = nn.Linear(
            hidden_dim,
            dim,
            bias=False
        )


    def forward(
        self,
        x
    ):

        # x:
        # (B, T, D)

        gate = self.gate_proj(
            x
        )

        # gate:
        # (B, T, D_ff)

        up = self.up_proj(
            x
        )

        # up:
        # (B, T, D_ff)

        hidden = (
            F.silu(
                gate
            )
            *
            up
        )

        # hidden:
        # (B, T, D_ff)

        output = self.down_proj(
            hidden
        )

        # output:
        # (B, T, D)

        return output


# =========================================================
# 5. Transformer Block
# =========================================================

class TransformerBlock(nn.Module):

    def __init__(
        self,
        config
    ):
        super().__init__()

        # Attention Pre-Norm

        self.attn_norm = RMSNorm(
            config.dim,
            eps=config.rms_eps
        )

        self.attention = (
            CausalGQAAttention(
                config
            )
        )

        # FFN Pre-Norm

        self.ffn_norm = RMSNorm(
            config.dim,
            eps=config.rms_eps
        )

        self.ffn = SwiGLU(
            dim=config.dim,
            hidden_dim=config.hidden_dim
        )


    def forward(
        self,
        x
    ):

        # -------------------------------------------------
        # Attention block
        #
        # x1 =
        # x + Attention(RMSNorm(x))
        # -------------------------------------------------

        attention_output = (
            self.attention(
                self.attn_norm(
                    x
                )
            )
        )

        x = (
            x
            +
            attention_output
        )

        # -------------------------------------------------
        # Feed-forward block
        #
        # x2 =
        # x1 + SwiGLU(RMSNorm(x1))
        # -------------------------------------------------

        ffn_output = (
            self.ffn(
                self.ffn_norm(
                    x
                )
            )
        )

        x = (
            x
            +
            ffn_output
        )

        # Shape remains:
        #
        # (B, T, D)

        return x


# =========================================================
# 6. Decoder-Only Transformer
# =========================================================

class DecoderOnlyTransformer(nn.Module):

    def __init__(
        self,
        config
    ):
        super().__init__()

        self.config = config

        # -------------------------------------------------
        # Token Embedding
        #
        # token IDs:
        # (B, T)
        #
        # ->
        #
        # hidden states:
        # (B, T, D)
        # -------------------------------------------------

        self.token_embedding = nn.Embedding(
            config.vocab_size,
            config.dim
        )

        # -------------------------------------------------
        # Transformer Blocks
        # -------------------------------------------------

        self.layers = nn.ModuleList(
            [
                TransformerBlock(
                    config
                )
                for _ in range(
                    config.num_layers
                )
            ]
        )

        # -------------------------------------------------
        # Final RMSNorm
        # -------------------------------------------------

        self.final_norm = RMSNorm(
            config.dim,
            eps=config.rms_eps
        )

        # -------------------------------------------------
        # Language Model Head
        #
        # D -> V
        #
        # hidden:
        # (B, T, D)
        #
        # logits:
        # (B, T, V)
        # -------------------------------------------------

        self.lm_head = nn.Linear(
            config.dim,
            config.vocab_size,
            bias=False
        )

        # -------------------------------------------------
        # Optional Weight Tying
        # -------------------------------------------------
        #
        # If you want embedding and LM head
        # to share parameters, uncomment:
        #
        # self.lm_head.weight = (
        #     self.token_embedding.weight
        # )


    def forward(
        self,
        input_ids
    ):

        # input_ids:
        # (B, T)

        if input_ids.dim() != 2:
            raise ValueError(
                "input_ids must have shape (B, T)."
            )

        B, T = input_ids.shape

        if T > self.config.max_seq_len:
            raise ValueError(
                f"Sequence length {T} exceeds "
                f"max_seq_len "
                f"{self.config.max_seq_len}."
            )

        # -------------------------------------------------
        # Token Embedding
        # -------------------------------------------------

        x = self.token_embedding(
            input_ids
        )

        # x:
        # (B, T, D)

        # -------------------------------------------------
        # Transformer Stack
        # -------------------------------------------------

        for layer in self.layers:

            x = layer(
                x
            )

        # Still:
        #
        # (B, T, D)

        # -------------------------------------------------
        # Final Norm
        # -------------------------------------------------

        x = self.final_norm(
            x
        )

        # -------------------------------------------------
        # LM Head
        # -------------------------------------------------

        logits = self.lm_head(
            x
        )

        # logits:
        # (B, T, V)

        return logits