Lesson 118
LLM Inference Pipeline

Inference:

Prefill
+
Decode


Prefill:

process entire prompt once.

Input:

(B, T_prompt)

Purpose:

process context
build KV cache
produce first token.


Decode:

generate one new token
per sequence per step.

Input:

(B, 1)

Uses:

previous KV cache

then:

compute new K/V
append cache
generate next token.


Autoregressive generation:

token 1
↓
token 2
↓
token 3
↓
...

Future tokens are unknown,
so generation is sequential.


Training:

full known sequence
+
causal mask
→ positions can be processed
in parallel.


Prefill:

often more compute intensive.


Decode:

often more sensitive
to memory bandwidth.


Important metrics:

TTFT
→ Time To First Token

Inter-token latency

Tokens per second

Throughput


Core mental model:

Prompt
↓
Prefill
↓
KV Cache
↓
First Token
↓
Decode
↓
Update Cache
↓
Next Token
↓
Repeat