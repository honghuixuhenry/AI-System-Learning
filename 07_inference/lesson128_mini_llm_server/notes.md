Lesson 128
LLM Inference Capstone


Mini LLM Server:

Client
↓
API
↓
Request Queue
↓
Scheduler
↓
Inference Engine
↓
Model Runtime
↓
KV Cache
↓
Sampling
↓
Streaming


Request state:

WAITING
PREFILL
DECODING
FINISHED


Continuous batching:

finished requests leave
and waiting requests
can enter active batch.


Engine step:

admit
schedule
prefill/decode
sample
update KV
stream
finish
free memory


Important separation:

Control Plane:

request lifecycle
scheduler
memory management


Data Plane:

Transformer forward
attention
GEMM
GPU kernels


Toy implementation:

simulates system behavior.

Production systems:

perform true batched
GPU execution.


Production serving
also requires:

Paged KV
prefix caching
quantization
distributed execution
metrics
failure handling
memory admission control


Core lesson:

model.generate()

is not the same as

LLM serving system.