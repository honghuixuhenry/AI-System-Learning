Lesson 124
GPU Memory & LLM Memory Estimation


Total inference memory:

Weights
+
KV Cache
+
Activations
+
Temporary Workspace
+
Runtime Overhead
+
Safety Margin


Weight memory:

parameters
× bits_per_parameter
/ 8


Approximate raw weight sizes:

7B FP16
≈ 13 GiB

7B INT8
≈ 6.5 GiB

7B INT4
≈ 3.3 GiB


KV Cache:

B
× Layers
× 2
× KV Heads
× Sequence Length
× Head Dimension
× Bytes


KV bytes per token:

Layers
× 2
× KV Heads
× Head Dimension
× Bytes


KV Cache grows with:

context length
concurrency


GQA / MQA reduce KV memory
by reducing KV head count.


Prefill:

larger activation footprint.


Decode:

small current activations
but persistent growing KV Cache.


Flash Attention:

reduces attention
intermediate memory.


Important:

Weights fit
does not mean
Serving fits.


Quantization:

reduces weight memory.

Paged KV Cache:

reduces allocation waste,
not actual required KV values.


Total capacity:

memory
→ concurrency
→ throughput


OOM may happen during:

model loading
prefill
decode
high concurrency


Always combine:

analytical estimation
+
actual profiling.