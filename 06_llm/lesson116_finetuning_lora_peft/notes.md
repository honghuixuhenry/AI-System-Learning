Lesson 116
Fine-Tuning, LoRA & PEFT


Pretraining:
train model from large-scale corpus.


Fine-Tuning:
continue training a pretrained model
on specialized data.


Full Fine-Tuning:

all parameters are trainable.


PEFT:

Parameter-Efficient Fine-Tuning

train only a small number
of parameters.


LoRA:

Low-Rank Adaptation


Original:

y = xW


LoRA:

y = xW + scale * xAB


W:
frozen pretrained weight


A, B:
trainable low-rank matrices


scale:

alpha / rank


rank:

r << model dimension


Benefits:

fewer trainable parameters
smaller optimizer states
smaller gradient memory
small adapter checkpoints
multiple adapters per base model


Important:

small trainable parameter count
does NOT mean total GPU memory
drops by the same percentage.


PEFT includes:

LoRA
Adapters
Prompt Tuning
Prefix Tuning
...


QLoRA:

Quantized Base Model
+
LoRA


Full Fine-Tuning:
maximum adaptation capacity
but expensive.


LoRA:
efficient adaptation
with frozen base weights.