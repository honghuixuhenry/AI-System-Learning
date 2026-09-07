Lesson 113
Distributed Training Fundamentals


Why distributed training?

1. Increase throughput
2. Scale beyond one device


Data Parallel:

replicate model
+
split data


Each rank:

different local batch
↓
forward
↓
loss
↓
backward
↓
local gradients


Then:

All-Reduce gradients
↓
same global gradient
↓
optimizer update


Rank:

global process ID


Local Rank:

process/GPU ID
inside current node


World Size:

total number
of distributed processes


Typical model:

one process
per GPU


Example:

2 nodes
×
4 GPUs

world_size = 8


Distributed Sampler:

different ranks
receive different
dataset partitions


Important:

Data Parallel
does NOT shard
the full model.


DDP:

full model replica
on every GPU


Gradient Accumulation:

parallelism across
micro steps / time


Data Parallel:

parallelism across
devices


Global Batch:

micro_batch
×
accumulation
×
world_size


Global Tokens/Update:

global_batch
×
sequence_length


Collectives:

All-Reduce
Broadcast
All-Gather
Reduce-Scatter


Performance:

compute
+
communication
+
synchronization


Important concepts:

intra-node
vs
inter-node communication


slowest worker
can become
a straggler bottleneck


Distributed AI stack:

Model
↓
Distributed Runtime
↓
Collective Communication
↓
Network / Interconnect
↓
GPU Hardware