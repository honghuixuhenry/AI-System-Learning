RoPE
Rotary Positional Embedding


Core idea:

Inject position information
by rotating Q and K.


2D rotation:

x' =
R(theta) x


R(theta):

[ cos(theta)  -sin(theta) ]
[ sin(theta)   cos(theta) ]


Position m:

angle =
m * frequency


Different dimension pairs
use different frequencies.


Q/K shape:

(B,H,T,d_h)


RoPE:

(B,H,T,d_h)
→
(B,H,T,d_h)


Attention:

RoPE(Q)
@
RoPE(K)^T

→
(B,H,T,T)


Important property:

Q at position m
K at position n

interaction depends naturally on:

n - m

relative position.


RoPE:

position information


Causal Mask:

future-access restriction


They are different mechanisms.


Typical pipeline:

X
↓
Q/K/V
↓
split heads
↓
RoPE on Q/K
↓
QK^T
↓
scale
↓
causal mask
↓
softmax
↓
V
↓
merge heads


RoPE does not normally require
a learned absolute position table.