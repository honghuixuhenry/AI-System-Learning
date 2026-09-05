Self-Attention

Input:
X
shape = (B,T,D)


Q = XWq
K = XWk
V = XWv


Q:
what this token looks for

K:
how this token can be matched

V:
information this token provides


Scores:

Q @ K^T

shape:

(B,T,D)
×
(B,D,T)

=

(B,T,T)


Scaled Scores:

scores / sqrt(d_k)


Attention Weights:

softmax(scores, dim=-1)

Each query row sums to 1.


Output:

weights @ V

(B,T,T)
×
(B,T,D)

=

(B,T,D)


Formula:

Attention(Q,K,V)
=
softmax(
    QK^T / sqrt(d_k)
) V


Important:

Self-Attention
=
Q/K/V come from same sequence.

Attention score matrix
has T × T structure.

This creates quadratic
sequence-length cost.