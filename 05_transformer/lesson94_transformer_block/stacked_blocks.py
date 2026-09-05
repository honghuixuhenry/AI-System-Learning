class TransformerBlock(nn.Module):

    def __init__(
        self,
        dim,
        num_heads,
        ffn_hidden_dim,
        dropout=0.1
    ):

        super().__init__()

        self.norm1 = nn.LayerNorm(
            dim
        )

        self.attention = (
            CausalMultiHeadAttention(
                dim,
                num_heads
            )
        )

        self.attn_dropout = nn.Dropout(
            dropout
        )

        self.norm2 = nn.LayerNorm(
            dim
        )

        self.ffn = FeedForward(
            dim,
            ffn_hidden_dim,
            dropout
        )


    def forward(
        self,
        x
    ):

        attn_output, _ = self.attention(
            self.norm1(
                x
            )
        )

        x = (
            x
            +
            self.attn_dropout(
                attn_output
            )
        )


        x = (
            x
            +
            self.ffn(
                self.norm2(
                    x
                )
            )
        )


        return x