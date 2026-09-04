import torch

from torch.utils.data import DataLoader

from dataset import NextTokenDataset
from model import MiniLanguageModel


sentences = [
    "I love AI",
    "I love PyTorch",
    "I study AI",
    "I study PyTorch",
    "AI is useful",
    "PyTorch is useful"
]


tokens = []

for sentence in sentences:
    tokens.extend(
        sentence.split()
    )


vocab = sorted(
    set(tokens)
)


token_to_id = {
    token: idx
    for idx, token in enumerate(
        vocab
    )
}


dataset = NextTokenDataset(
    sentences,
    token_to_id
)


loader = DataLoader(
    dataset,
    batch_size=4,
    shuffle=True
)

if torch.cuda.is_available():

    device = torch.device(
        "cuda"
    )

elif torch.backends.mps.is_available():

    device = torch.device(
        "mps"
    )

else:

    device = torch.device(
        "cpu"
    )

model = MiniLanguageModel(
    vocab_size=len(vocab),
    embedding_dim=16,
    hidden_dim=32
).to(
    device
)

loss_fn = torch.nn.CrossEntropyLoss()


optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=0.01
)

for epoch in range(
    100
):

    total_loss = 0.0
    total_samples = 0


    model.train()


    for x, y in loader:

        x = x.to(
            device
        )

        y = y.to(
            device
        )


        optimizer.zero_grad()


        logits = model(
            x
        )


        loss = loss_fn(
            logits,
            y
        )


        loss.backward()

        optimizer.step()


        batch_size = x.size(
            0
        )


        total_loss += (
            loss.item()
            *
            batch_size
        )

        total_samples += (
            batch_size
        )


    avg_loss = (
        total_loss
        /
        total_samples
    )


    if (
        epoch + 1
    ) % 10 == 0:

        print(
            f"Epoch {epoch + 1}, "
            f"Loss: {avg_loss:.4f}"
        )