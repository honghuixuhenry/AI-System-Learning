KV Cache


Purpose:

Avoid recomputing past K/V
during autoregressive generation.


Prefill:

Input:
(B,T)

Compute Q/K/V for prompt.

Save:

K cache
(B,Hkv,T,d_h)

V cache
(B,Hkv,T,d_h)


Decode:

Input:
(B,1)

New Q:
(B,Hq,1,d_h)

New K/V:
(B,Hkv,1,d_h)

Append K/V to cache.


Attention:

Q_new
@
K_cache^T

Scores:
(B,Hq,1,T_cache)


Why no Q cache?

Old queries are not needed
for generating the new token.

New query reads past keys
and values.


Important:

KV cache is runtime state,
not model parameters.


Every Transformer layer
has its own K/V cache.


RoPE:

new token position must continue
from the cached sequence length.


GQA:

store only Hkv K/V heads,
not expanded Hq copies.


Training:

usually full-sequence parallel
computation without inference-style
KV cache.


Inference:

Prefill once,
then decode one token at a time.


Real systems:

do not usually grow cache
with repeated torch.cat.

They use efficient memory
management such as preallocation
or paged KV-cache techniques.