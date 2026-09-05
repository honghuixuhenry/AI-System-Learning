FlashAttention


Standard Attention:

Attention(Q,K,V)
=
softmax(
    QK^T / sqrt(d_h)
) V


Shapes:

Q/K/V:
(B,H,T,d_h)

Scores:
(B,H,T,T)

Weights:
(B,H,T,T)

Output:
(B,H,T,d_h)


Problem:

T x T intermediate matrices
become very large for
long sequences.


Attention matrix memory:

B * H * T * T
* bytes_per_element


If T doubles:

attention matrix memory
approximately quadruples.


FlashAttention core idea:

Do not materialize the entire
T x T attention matrix in HBM.

Process Q/K/V in tiles.

Use online stable softmax.

Accumulate output incrementally.


Important:

FlashAttention does NOT
change the mathematical
definition of dense attention.

It does NOT generally change
dense attention from O(T^2)
to O(T).

Its main benefit is reducing:

memory traffic
HBM reads/writes
large intermediate storage


Online Softmax:

Maintain:

running max
running exponential sum

when processing blocks.


PyTorch:

torch.nn.functional
.scaled_dot_product_attention


SDPA is a high-level API.

The exact backend depends on:

device
dtype
shape
PyTorch version
hardware


KV Cache:

avoids recomputing old K/V
during autoregressive decoding.


GQA:

reduces number of distinct
K/V heads.


FlashAttention:

optimizes attention computation
and memory IO.


They solve different problems
and can be used together.