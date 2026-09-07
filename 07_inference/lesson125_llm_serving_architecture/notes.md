Lesson 125
LLM Serving Architecture


Core architecture:

Client
↓
API Server
↓
Request Queue
↓
Scheduler
↓
Model Worker
↓
GPU
↓
Sampling
↓
Streaming


Request states:

WAITING
PREFILL
DECODING
FINISHED

Possible additional states:

CANCELLED
ERROR
TIMEOUT


API Server:

request handling
validation
authentication
rate limiting
streaming


Request Queue:

buffers requests
waiting for GPU resources.


Scheduler:

controls admission
continuous batching
prefill/decode scheduling
token budgets
priorities.


Model Worker:

owns model execution
and performs GPU inference.


KV Cache Manager:

allocate
append
lookup
free
reuse


Streaming:

return generated tokens
before the full response completes.


Important:

Model
!=
Serving Engine


Serving Engine includes:

request management
scheduling
memory management
batching
sampling
streaming
distributed execution


Paged KV:

memory-management layer.

Continuous Batching:

scheduler layer.

Quantization:

model execution / kernel layer.

Flash Attention:

kernel layer.


Request lifecycle must match
resource lifecycle.

Finished/cancelled/error requests
must release KV memory.


Scale Up:

Tensor Parallelism

Scale Out:

Model Replicas


Production systems also need:

load balancing
backpressure
metrics
health checks
warmup
failure handling