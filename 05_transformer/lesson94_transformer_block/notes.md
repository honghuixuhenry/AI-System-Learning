Complete Transformer Block


Pre-Norm structure:

x1 =
x +
Attention(
    LayerNorm(x)
)


x2 =
x1 +
FFN(
    LayerNorm(x1)
)


Attention:

token-to-token communication


FFN:

per-token nonlinear processing


Input:

(B,T,D)


Output:

(B,T,D)


Attention internally:

(B,T,D)
→
(B,H,T,head_dim)
→
(B,H,T,T)
→
(B,H,T,head_dim)
→
(B,T,D)


FFN:

(B,T,D)
→
(B,T,D_ff)
→
(B,T,D)


Residual:

preserves hidden dimension


Transformer stack:

Embedding
↓
Block × N
↓
Final Norm
↓
LM Head
↓
(B,T,V)


Important:

Shifted labels
and
causal masking
solve different problems.

Shift:
defines next-token targets.

Causal mask:
prevents future information leakage.