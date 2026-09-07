Lesson 126
vLLM, SGLang & Modern Serving Engines


Model:

defines neural network
architecture and weights.


Serving Engine:

organizes inference execution.


Examples:

vLLM
SGLang


Serving engine includes:

request queue
scheduler
continuous batching
KV cache management
model execution
sampling
streaming
distributed runtime


Important:

model
!=
serving engine


HF generate():

excellent for model inference,
experimentation,
and simple use cases.

Production serving additionally needs:

scheduling
batching
memory management
concurrency
streaming
resource control


vLLM:

high-performance LLM
inference/serving runtime.

Important concepts:

Paged KV / PagedAttention
continuous batching
optimized model execution


SGLang:

high-performance serving/runtime
with strong support for
structured and programmatic
LLM execution.


Prefix caching:

reuse KV states
for identical token prefixes.


Prefix caching:

can reduce repeated prefill work.


Important:

KV cache
=
request inference state.

Prefix cache
=
cross-request reuse
of common prefix state.


OpenAI-compatible API:

decouples application
from serving backend.


Same model
can have different performance
under different serving engines.


Performance depends on:

scheduler
KV layout
memory management
kernels
batching
quantization
distributed execution


Always benchmark:

model
+
engine
+
hardware
+
workload
+
configuration