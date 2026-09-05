GQA / MQA


MHA:

Q heads = H
K heads = H
V heads = H


GQA:

Q heads = Hq
K heads = Hkv
V heads = Hkv

Hkv < Hq


MQA:

Hkv = 1


Requirement:

Hq % Hkv == 0


Group size:

Hq / Hkv


Example:

Hq = 32
Hkv = 8

group size = 4


Shapes:

Q:
(B,Hq,T,d_h)

K:
(B,Hkv,T,d_h)

V:
(B,Hkv,T,d_h)


Attention maps:

(B,Hq,T,T)


KV Cache per layer:

2
*
B
*
T
*
Hkv
*
d_h


Total KV Cache:

2
*
L
*
B
*
T
*
Hkv
*
d_h


Main benefit:

fewer K/V heads
→
smaller KV cache
→
less memory traffic
→
better inference efficiency


MHA:
no sharing

GQA:
group sharing

MQA:
all query heads share one K/V head