import torch

from model import Classifier


model = Classifier()


optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=0.001
)


checkpoint = torch.load(
    "checkpoints/last_checkpoint.pt",
    map_location="cpu",
    weights_only=True
)


model.load_state_dict(
    checkpoint[
        "model_state_dict"
    ]
)


optimizer.load_state_dict(
    checkpoint[
        "optimizer_state_dict"
    ]
)


start_epoch = (
    checkpoint["epoch"]
    +
    1
)


print(
    "Resume from epoch:",
    start_epoch
)