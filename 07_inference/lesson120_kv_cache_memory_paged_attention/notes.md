Lesson 120
KV Cache Memory & Paged Attention


KV Cache memory:

2
× layers
× KV heads
× sequence length
× head dimension
× bytes
× batch


KV Cache is dynamic:

requests arrive
sequences grow
requests finish
memory must be reused


Contiguous allocation problems:

over-allocation
internal fragmentation
external fragmentation
growth difficulty


Paged KV Cache:

split KV memory into
fixed-size blocks.


Logical KV sequence:

Block 0
Block 1
Block 2


Physical memory:

Block 17
Block 3
Block 28


Block Table:

logical block
→ physical block


Benefits:

dynamic allocation
less memory waste
easy growth
easy reuse
better concurrency


Paged Attention:

attention kernel accesses
paged/non-contiguous KV blocks
through block metadata.


Important:

Paged Attention does NOT
remove historical attention.

It primarily improves
KV Cache memory management.


Block size trade-off:

larger block
→ less metadata
→ more internal waste

smaller block
→ better utilization
→ more management overhead


Connection to serving:

Paged KV Cache
+
Continuous Batching
+
Scheduling

→ efficient LLM serving