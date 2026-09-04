Device

CPU:
general computation

CUDA:
NVIDIA GPU

MPS:
Apple Silicon GPU backend


Tensor properties:

shape
dtype
device


Precision:

FP32
= 32-bit float
= 4 bytes

FP16
= 16-bit float
= 2 bytes
= smaller numerical range

BF16
= 16-bit float
= 2 bytes
= large exponent range


Memory:

memory =
numel × element_size


Mixed Precision:

Goal:
speed + memory saving
while maintaining stability


Autocast:

with torch.autocast(...):
    forward
    loss


FP16 Training:

GradScaler
helps prevent gradient underflow


Typical order:

zero_grad
↓
autocast forward
↓
loss
↓
scale(loss).backward
↓
unscale
↓
gradient clipping
↓
scaler.step
↓
scaler.update


Important:

AMP
!=
everything FP16


MPS
!=
CUDA