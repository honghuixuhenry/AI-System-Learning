Lesson 122
Quantization


Goal:

represent model parameters
using fewer bits.


Typical formats:

FP32
32 bits

FP16/BF16
16 bits

INT8
8 bits

INT4
4 bits


Weight memory:

parameters
× bits
/ 8


Quantization:

float
↓
integer representation
+
scale
+
optional zero point


Symmetric:

q = round(x / scale)

x_hat = q × scale


Asymmetric:

q = round(x / scale) + zero_point

x_hat =
scale × (q - zero_point)


Quantization introduces:

approximation error.


Granularity:

per-tensor
per-channel
group-wise


Group-wise:

small groups
share individual scales.

Smaller group:
better fidelity
more metadata.


INT4:

two 4-bit values
can be packed into one byte.


Weight-only quantization:

weights:
INT8 / INT4

activations:
FP16 / BF16


Why useful for LLM inference:

less weight memory

less memory traffic

potentially higher decode throughput


Important:

smaller datatype
does not automatically mean
faster inference.

Hardware and kernels matter.


PTQ:

Post-Training Quantization


Calibration:

use representative data
to choose quantization parameters.


QAT:

Quantization-Aware Training


Examples:

GPTQ
AWQ


QLoRA:

quantized frozen base
+
trainable LoRA adapters


Important:

Quantization
is NOT simple integer casting.


Total serving memory:

Model Weights
+
KV Cache
+
Activations
+
Runtime Buffers