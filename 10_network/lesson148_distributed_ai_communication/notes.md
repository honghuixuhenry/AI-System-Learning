Lesson 148

Distributed AI Communication


Rank:

worker identity


World Size:

number of workers


Point-to-Point:

one worker
to another


Collective:

multiple workers
participate


Broadcast:

one
→
all


Reduce:

all
→
one


All-Reduce:

all
→
reduce
→
all


All-Gather:

shards
→
full tensor
on all ranks


Reduce-Scatter:

reduce
→
shards


DDP:

gradient
All-Reduce


FSDP:

parameter
All-Gather

gradient
Reduce-Scatter


Tensor Parallel:

frequent
collective communication


Pipeline Parallel:

activation
point-to-point


Communication cost:

latency
+
data / bandwidth


Small messages:

latency sensitive


Large messages:

bandwidth sensitive


Overlap:

compute
+
communication


Topology matters.


Collectives
are synchronization points.


Straggler:

slowest rank
can slow everybody.


Distributed AI:

not only
GPU compute

but also
communication system.