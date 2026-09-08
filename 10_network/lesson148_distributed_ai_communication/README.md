# Lesson 148
# Distributed AI Communication
# & Collective Operations

Distributed AI:

Compute
+
Communication

Core concepts:

Rank
World Size

Point-to-Point
vs
Collective Communication

Collectives:

Broadcast
Reduce
All-Reduce
Gather
All-Gather
Scatter
Reduce-Scatter

Broadcast:

one -> all

Reduce:

many -> one

All-Reduce:

many -> all
after reduction

All-Gather:

distributed shards
-> full data on all ranks

Reduce-Scatter:

reduce
+
distribute shards

DDP:

gradient All-Reduce

FSDP:

parameter All-Gather
+
gradient Reduce-Scatter

Tensor Parallel:

frequent tensor collectives

Pipeline Parallel:

primarily point-to-point
activation communication

Distributed performance depends on:

compute
memory
communication
topology
stragglers