Regularization

Goal:
improve generalization
reduce overfitting


Dropout:

nn.Dropout(p)

Training mode:
randomly zero activations

Evaluation mode:
dropout disabled


model.train()
→ activates training behavior

model.eval()
→ activates evaluation behavior


Important:

train/eval mode
and
autograd enable/disable

are different mechanisms.


Weight Decay:

AdamW(
    ...,
    weight_decay=...
)

regularizes parameters


Too little regularization:
possible overfitting

Too much regularization:
possible underfitting


Monitor:

Train Loss
Val Loss
Train Accuracy
Val Accuracy