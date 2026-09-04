Weight Initialization

Why?
- break neuron symmetry
- maintain signal scale
- improve optimization


Zero initialization:
bad for weights of symmetric hidden neurons


Bias:
can often start at zero


Xavier:
nn.init.xavier_uniform_
nn.init.xavier_normal_

Commonly associated with:
Linear / Tanh-like networks


Kaiming:
nn.init.kaiming_uniform_
nn.init.kaiming_normal_

Designed for:
ReLU-like activations


Vanishing Gradient:
gradients become extremely small
in earlier/deeper paths


Exploding Gradient:
gradients become extremely large


Gradient clipping:

loss.backward()

clip_grad_norm_(
    model.parameters(),
    max_norm=1.0
)

optimizer.step()


Important:

Initialization
Activation
Normalization
Learning Rate
Optimizer
Gradient Clipping

all affect training stability.