RMSNorm
Root Mean Square Normalization


Input:

x
(B,T,D)


RMS:

sqrt(
    mean(
        x^2,
        dim=-1
    )
    +
    eps
)


Normalize:

x_norm =
x / RMS(x)


Trainable scale:

y =
weight * x_norm


weight:

(D,)


Output:

(B,T,D)


LayerNorm:

subtract mean
+
normalize variance


RMSNorm:

does not subtract mean

normalizes using
root mean square


LayerNorm:

(x - mean)
/
sqrt(
    variance + eps
)


RMSNorm:

x
/
sqrt(
    mean(x^2) + eps
)


Important:

RMSNorm is per-token.

For:

(B,T,D)

each token's D-dimensional
hidden vector receives its
own RMS value.


Modern LLM block:

x
↓
RMSNorm
↓
RoPE Causal Attention
↓
Residual
↓
RMSNorm
↓
FFN
↓
Residual