PyTorch Model:

Tensor
   ↓
nn.Module
   ↓
Layers
   ↓
forward()
   ↓
Output
   ↓
Loss
   ↓
Autograd
   ↓
Parameter Gradients


nn.Module:

__init__()
→ define layers / parameters

forward()
→ define data flow


Parameter:

trainable Tensor
registered inside Module


Useful APIs:

model.parameters()
model.named_parameters()
model.state_dict()

model.to(device)

model.train()
model.eval()


Important:

model(x)
→ calls forward()

Linear:
Input (..., in_features)
Output (..., out_features)

Linear parameter count:

in_features × out_features
+
out_features