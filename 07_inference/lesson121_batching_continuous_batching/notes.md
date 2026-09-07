Lesson 121
Batching & Continuous Batching


Batching:

process multiple requests
together on the GPU.


Static Batching:

form a fixed batch
and wait for the batch
to finish.

Problem:

different generation lengths
cause idle batch slots.


Decode Batching:

multiple active sequences
each contribute one new token
per decode iteration.


Continuous Batching:

batch membership can change
between generation iterations.

Finished requests leave.

New requests can enter.


Benefits:

better GPU utilization
higher throughput
lower queueing delay


Serving runtime:

Incoming Requests
↓
Waiting Queue
↓
Scheduler
↓
Prefill / Decode
↓
GPU
↓
Update Request State
↓
Repeat


Paged KV Cache:

supports dynamic allocation,
growth, release and reuse.

Therefore it works naturally
with continuous batching.


Chunked Prefill:

split long prefills into
smaller chunks to balance
prefill and decode workloads.


Important trade-off:

Throughput
vs
Latency


Scheduler may consider:

batch size
token budget
KV memory
TTFT
decode latency
fairness
priority


Important:

Requests in the same
decode batch may have
different:

context lengths
positions
sampling settings
KV caches.