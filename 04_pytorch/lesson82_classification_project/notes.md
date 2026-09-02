Classification Pipeline:

Dataset
↓
DataLoader
↓
Input Batch
↓
Model
↓
Raw Logits
↓
CrossEntropyLoss
↓
Loss
↓
Backward
↓
Optimizer


Prediction:

Raw Logits
↓
argmax(dim=1)
↓
Class Index


CrossEntropy:

logits:
(B, C)

labels:
(B,)

labels dtype:
torch.long


Loss
=
optimization objective

Accuracy
=
evaluation metric


Training:

model.train()

zero_grad
forward
loss
backward
step


Validation:

model.eval()

torch.no_grad()

forward
loss
accuracy


Overfitting:

Train performance high
Validation performance significantly worse


Underfitting:

Train performance poor
Validation performance also poor


Debug first:

shape
dtype
device