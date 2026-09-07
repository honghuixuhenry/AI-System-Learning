Lesson 110
Training Loop &
Gradient Accumulation


Normal training:

batch
↓
forward
↓
loss
↓
backward
↓
optimizer.step


Gradient accumulation:

micro batch 1
↓ backward

micro batch 2
↓ backward

...

micro batch K
↓ backward

↓
optimizer.step


PyTorch gradients
accumulate by default.


For equal-size micro batches:

scaled_loss =
raw_loss / accumulation_steps


Do not zero gradients
between accumulated
micro batches.


Single GPU:

Effective Batch
=
Micro Batch
×
Accumulation Steps


Data Parallel:

Global Batch
=
Micro Batch
×
Accumulation Steps
×
World Size


Global Tokens / Update
≈
Micro Batch
×
Sequence Length
×
Accumulation Steps
×
World Size


Important:

Gradient accumulation
reduces peak activation
memory requirement.

It does NOT:

increase context length
increase model size
create free compute


Training terms:

Micro Step
!=
Optimizer Step


Gradient clipping:

after accumulation
before optimizer.step


Logging:

record raw loss,
not loss divided by
accumulation_steps.


Large-scale training
often tracks:

optimizer steps
tokens seen
global batch
learning rate
loss
gradient norm


Gradient accumulation:
across time / micro steps

Data parallelism:
across devices