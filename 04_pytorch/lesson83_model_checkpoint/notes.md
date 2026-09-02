PyTorch Model Saving

1. Save model weights:

torch.save(
    model.state_dict(),
    "model.pt"
)


2. Load model weights:

model = Model()

state_dict = torch.load(
    "model.pt",
    weights_only=True
)

model.load_state_dict(
    state_dict
)


3. Inference:

model.eval()

with torch.no_grad():
    output = model(x)


4. Training checkpoint:

checkpoint = {
    "epoch": epoch,
    "model_state_dict":
        model.state_dict(),
    "optimizer_state_dict":
        optimizer.state_dict()
}


5. Resume:

Create Model
↓
Create Optimizer
↓
Load Checkpoint
↓
Load Model State
↓
Load Optimizer State
↓
Restore Epoch
↓
Continue Training


6. Best vs Latest:

best_model.pt
→ evaluation / inference

last_checkpoint.pt
→ resume training