Lesson 115
Tensor Parallelism
&
Pipeline Parallelism


DDP:
split data

FSDP:
split model states

TP:
split tensor computation

PP:
split model layers


Tensor Parallel:

Y = XW


Column Parallel:

W = [W0 W1]

Y0 = XW0
Y1 = XW1

Y = [Y0 Y1]


Row Parallel:

Y = [Y0 Y1]

W =
[W0
 W1]

Z =
Y0W0 + Y1W1

requires reduction.


TP:

multiple GPUs
compute one layer together.


Pipeline Parallel:

GPU0:
Layers 1-N

GPU1:
Layers N+1-M

GPU2:
later layers


Communication:

activations forward
gradients backward


Pipeline Bubble:

some stages idle
while pipeline fills/drains.


Micro-batches:

keep multiple stages
busy simultaneously.


Hybrid Parallelism:

DP × TP × PP


Example:

DP = 8
TP = 4
PP = 2

Total GPUs:

8 × 4 × 2
=
64


Mental Model:

DDP → Data
FSDP → State
TP → Tensor
PP → Layers