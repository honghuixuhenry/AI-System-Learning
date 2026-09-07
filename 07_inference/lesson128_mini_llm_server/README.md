# Lesson 128
# Mini LLM Inference Server

This project demonstrates the
core architecture of an LLM
serving engine.

Pipeline:

Request
→ Queue
→ Scheduler
→ Prefill
→ KV Cache
→ Decode
→ Sampling
→ Streaming

Core components:

- Request lifecycle
- Request queue
- Continuous batching scheduler
- KV cache abstraction
- Prefill/decode runtime
- Inference engine loop
- API layer

This implementation is
educational.

It does not implement
production GPU kernels,
real PagedAttention,
or distributed inference.