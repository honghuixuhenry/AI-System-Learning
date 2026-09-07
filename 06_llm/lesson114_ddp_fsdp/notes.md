Lesson 114
DDP & FSDP


DDP:

Distributed Data Parallel


Model:
replicated on every GPU

Data:
split across GPUs


Each rank:

local batch
↓
forward
↓
loss
↓
backward
↓
local gradient


DDP:

gradient All-Reduce
↓
same gradient
on every rank


DDP memory:

full parameters
full gradients
full optimizer states

on every GPU


Therefore:

DDP does NOT solve
a model that cannot fit
on one GPU.



FSDP:

Fully Sharded Data Parallel


Persistent model states:

parameters
gradients
optimizer states

are sharded
across ranks.


FSDP Forward:

parameter shards
↓
All-Gather
↓
compute
↓
reshard


FSDP Backward:

compute gradient
↓
Reduce-Scatter
↓
gradient shards


Approximate state memory:

Total Model State
/
World Size


But peak memory also includes:

activations
temporary full parameters
communication buffers
CUDA overhead


DDP:

simpler
higher state replication

FSDP:

lower model-state memory
more communication


Gradient Accumulation + DDP:

first K-1 micro steps:
no_sync()

last micro step:
normal backward
→ gradient synchronization


Important:

FSDP
!=
Tensor Parallelism


FSDP:
shards model state

Tensor Parallel:
splits actual tensor compute


Distributed training stack:

Gradient Accumulation
+
Mixed Precision
+
DDP / FSDP
+
Optimizer
+
Scheduler
+
Checkpointing