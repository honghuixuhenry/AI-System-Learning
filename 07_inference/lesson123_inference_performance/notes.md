Lesson 123
Inference Performance


TTFT:

Time To First Token

request arrival
→
first generated token


TTFT may include:

queueing
tokenization
scheduling
prefill
sampling
runtime overhead


ITL:

Inter-Token Latency

time between consecutive
generated tokens.


TPOT:

Time Per Output Token

closely related to ITL
depending on benchmark definition.


Single-request TPS:

approximately

1 / ITL

when ITL is measured
in seconds per token.


End-to-End Latency:

request arrival
→
response completion


Throughput:

work completed
per unit time.


Possible definitions:

requests/s
input tokens/s
output tokens/s
total tokens/s


Important:

per-user tokens/s
is different from
aggregate server throughput.


Prefill:

many tokens
usually more compute-heavy.


Decode:

one new token per sequence
often memory-bandwidth-sensitive.


Batching:

can improve aggregate throughput
but may affect latency.


Percentiles:

P50
P90
P95
P99


P99:

important for tail latency.


Production benchmark:

measure performance
under realistic load.


SLO:

Service Level Objective


Goodput:

useful throughput
that satisfies an SLO.


Always report workload:

model
hardware
precision
input length
output length
concurrency
serving engine


Never compare:

prefill tok/s
directly with
decode tok/s.