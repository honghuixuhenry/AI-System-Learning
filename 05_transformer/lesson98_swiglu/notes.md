SwiGLU


SiLU:

SiLU(x)
=
x * sigmoid(x)


SwiGLU:

gate =
gate_proj(x)

up =
up_proj(x)


hidden =
SiLU(gate)
*
up


output =
down_proj(hidden)


Shapes:

x:
(B,T,D)

gate:
(B,T,D_ff)

up:
(B,T,D_ff)

hidden:
(B,T,D_ff)

output:
(B,T,D)


Three projections:

gate_proj:
D -> D_ff

up_proj:
D -> D_ff

down_proj:
D_ff -> D


Parameter count
without bias:

3 * D * D_ff


Important:

The multiplication is
element-wise.

It is not matrix multiplication.


Attention:

token mixing


SwiGLU:

per-token nonlinear
gated feature processing


Modern decoder block:

RMSNorm
↓
RoPE Causal Attention
↓
Residual
↓
RMSNorm
↓
SwiGLU
↓
Residual