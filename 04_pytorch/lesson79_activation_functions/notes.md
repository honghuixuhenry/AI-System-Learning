Activation Function
=
Nonlinear Transformation


Why needed?

Linear
↓
Linear
↓
Linear

is still equivalent to:

Linear


Neural Network:

Linear
↓
Activation
↓
Linear
↓
Activation
↓
...


ReLU:

f(x) = max(0, x)

positive gradient ≈ 1
negative gradient = 0

risk:
Dead ReLU


Sigmoid:

range:
0 to 1

useful for:
binary probability / gates

risk:
saturation
vanishing gradient


Tanh:

range:
-1 to 1

zero-centered

also can saturate


GELU:

smooth nonlinear activation

common in:
Transformer / language models


Important:

Activation Function
!=
Trainable Parameter

Activation Function
affects both:

Forward representation
+
Backward gradient flow