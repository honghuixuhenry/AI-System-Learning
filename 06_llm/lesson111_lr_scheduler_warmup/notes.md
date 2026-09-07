Lesson 111
Learning Rate Scheduler & Warmup


Optimizer:

uses gradients
to update parameters


Learning Rate:

controls update size


Scheduler:

changes learning rate
over training


Typical LLM schedule:

small LR
↓
linear warmup
↓
peak LR
↓
decay
↓
small LR


Warmup:

lr(t) ≈
peak_lr ×
t / warmup_steps


Cosine decay:

lr =
min_lr
+
0.5 ×
(peak_lr - min_lr)
×
(1 + cos(pi × progress))


Important:

Micro Step
!=
Optimizer Step


With gradient accumulation:

micro batch
↓ backward

...

optimizer.step
scheduler.step
zero_grad


Scheduler should usually
advance with optimizer updates.


Total optimizer steps:

ceil(
    micro_batches
    /
    accumulation_steps
)
× epochs


Warmup steps may be:

fixed number

or

warmup_ratio
× total_steps


Do not confuse:

Learning Rate Decay

with

Weight Decay


Useful training logs:

loss
learning rate
gradient norm
optimizer step
tokens seen


Training stability:

Data correctness
+
Model correctness
+
Optimizer
+
Learning-rate schedule
+
Numerical precision