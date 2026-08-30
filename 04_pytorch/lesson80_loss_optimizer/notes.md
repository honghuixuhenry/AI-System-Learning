Loss Function
=
measures prediction error


Regression:

Prediction
↓
MSELoss
↓
Loss


Multi-class Classification:

Raw Logits
↓
CrossEntropyLoss

Do NOT manually apply Softmax first
for standard CrossEntropyLoss usage.


Binary / Multi-label:

Raw Logits
↓
BCEWithLogitsLoss

Sigmoid is built into the stable loss formulation.


Optimizer:

model.parameters()
      ↓
Optimizer
      ↓
Parameter Update


Standard Training Step:

optimizer.zero_grad()

prediction = model(x)

loss = loss_fn(
    prediction,
    target
)

loss.backward()

optimizer.step()


Meaning:

zero_grad()
→ clear old gradients

forward()
→ predictions

loss()
→ measure error

backward()
→ compute gradients

step()
→ update parameters


Common Optimizers:

SGD
SGD + Momentum
Adam
AdamW