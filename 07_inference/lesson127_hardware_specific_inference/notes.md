Lesson 127
TensorRT-LLM, llama.cpp
& Hardware-Specific Inference


Inference stack:

Application
↓
Serving Engine
↓
Inference Runtime
↓
Kernel
↓
Hardware


Same model math
can use very different
hardware implementations.


TensorRT-LLM:

NVIDIA-oriented
LLM inference stack.

Focus:

optimized GPU execution
kernel fusion
precision optimization
multi-GPU inference
hardware-specific acceleration


llama.cpp:

portable local LLM runtime.

Strong use cases:

CPU
Apple Silicon
local inference
quantized models


GGUF:

common model format
in llama.cpp ecosystem.


Important:

quantization
is not only dtype.

It includes:

mapping
storage format
metadata
kernel support


Training stack
can differ from
inference stack.


Example:

Training:
PyTorch + FSDP

Inference:
vLLM
TensorRT-LLM
or llama.cpp


Runtime selection depends on:

model
model format
hardware
precision
workload
serving requirements


NVIDIA GPU:

vLLM
SGLang
TensorRT-LLM
may be candidates.


Apple Silicon:

llama.cpp-style
local runtimes
are common choices.


CPU:

quantized inference
can trade speed
for larger memory capacity.


Important:

Fits in memory
!=
Runs fast.


Hardware-software co-design:

runtime
+
kernel
+
hardware
determines real performance.


Always benchmark
on target hardware
and target workload.