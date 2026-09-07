Lesson 117
LLM Training Capstone


Complete Pipeline:

Raw Text
↓
Cleaning
↓
Tokenization
↓
Packing
↓
Training Sequences
↓
DataLoader
↓
Transformer
↓
Causal LM Loss
↓
Backward
↓
Optimizer
↓
Checkpoint


Input:

(B, T)

Embedding:

(B, T, D)

Logits:

(B, T, V)


Causal LM:

input:
x0 x1 x2 x3

target:
x1 x2 x3 x4


Causal mask:
controls what tokens are visible.

Shifted targets:
control what token is predicted.


Training:

forward
loss
backward
gradient clipping
optimizer step
scheduler step


Effective Batch:

micro_batch
× accumulation_steps
× world_size


Mixed Precision:

FP16 / BF16


Distributed Training:

DDP
FSDP
TP
PP


Fine-Tuning:

Full Fine-Tuning
LoRA / PEFT


Training Checkpoint:

model state
optimizer state
scheduler state
scaler state
global step
configuration


Training:
parallel next-token prediction

Inference:
autoregressive token generation