Lesson 119
KV Cache


Self-Attention:

Q = XWq
K = XWk
V = XWv


Prefill:

process all prompt tokens
and create K/V cache.


Decode:

new token
↓
Q_new
K_new
V_new


K_all =
K_cache + K_new

V_all =
V_cache + V_new


Attention:

Q_new
attends to
all cached K


then uses:

all cached V


Why cache K/V?

Historical tokens do not change,
so their K/V do not need
to be recomputed.


Why not cache Q?

Q represents the current query.
Each new token creates a new Q.


KV Cache is per layer.


Typical shape:

K/V:

(B, H_kv, T, D_head)


Decode Q:

(B, H_q, 1, D_head)


KV Cache saves computation
but consumes GPU memory.


Cache grows with:

batch
layers
sequence length
KV heads
head dimension
dtype size


GQA/MQA:

reduce H_kv
→ smaller KV Cache


Important:

KV Cache does NOT make
attention O(1).

New queries still attend
to historical K/V.


Model weights:
shared across users.

KV Cache:
request-specific.