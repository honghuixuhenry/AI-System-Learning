Normalization

Basic formula:

x_hat =
(x - mean)
/
sqrt(var + eps)


Then:

y =
gamma * x_hat
+
beta


BatchNorm:

Input:
(B, D)

For each feature:
normalize across batch

Training:
uses batch statistics
updates running statistics

Evaluation:
uses running statistics


LayerNorm:

Input:
(B, D)
or
(B, T, D)

Normalize across feature dimension
for each sample/token

Does not depend on other samples

Transformer:
LayerNorm(D)


Important:

BatchNorm:
batch-dependent

LayerNorm:
sample/token-local


state_dict:

BatchNorm includes:
weight
bias
running_mean
running_var

LayerNorm includes:
weight
bias