Lesson 112
Mixed Precision & Training Stability


FP32:
4 bytes

FP16:
2 bytes
smaller dynamic range

BF16:
2 bytes
large dynamic range
similar exponent range to FP32


Training memory:

parameters
gradients
optimizer states
activations
temporary buffers


Mixed Precision:

not everything
uses the same dtype.


Autocast:

automatically selects
lower / higher precision
for different operations.


FP16 risk:

underflow
overflow


Gradient Scaling:

loss'
=
scale × loss

↓ backward

scaled gradients

↓ unscale

true gradients


FP16 common flow:

autocast
↓
scaled loss.backward
↓
unscale
↓
gradient clipping
↓
scaler.step
↓
scaler.update


BF16 common flow:

autocast
↓
loss.backward
↓
gradient clipping
↓
optimizer.step


Important:

Unscale
BEFORE
gradient clipping.


Gradient Scaling
!=
Gradient Clipping


Mixed Precision
does not change:

model objective
or
model architecture.


It changes:

numerical execution
memory use
compute throughput.


Training stability:

data correctness
+
architecture correctness
+
normalization
+
learning rate
+
warmup
+
gradient clipping
+
precision
+
loss scaling
+
finite-value monitoring


Useful signals:

loss
learning rate
gradient norm
scale
NaN / Inf
tokens seen