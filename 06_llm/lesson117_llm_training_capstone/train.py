import torch
import torch.nn.functional as F

from torch.utils.data import DataLoader

from config import TrainingConfig
from tokenizer import ByteTokenizer
from dataset import LanguageModelDataset
from model import MiniLLM


config = TrainingConfig()

device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)


documents = [
    "Artificial intelligence is changing computing.",
    "Large language models learn token sequences.",
    "Transformers use attention mechanisms.",
]


tokenizer = ByteTokenizer()


dataset = LanguageModelDataset(
    documents,
    tokenizer,
    config.sequence_length
)


loader = DataLoader(
    dataset,
    batch_size=config.batch_size,
    shuffle=True
)


model = MiniLLM(
    vocab_size=config.vocab_size,
    d_model=config.d_model,
    num_heads=config.num_heads,
    num_layers=config.num_layers
).to(device)


optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=config.learning_rate,
    weight_decay=config.weight_decay
)


model.train()

optimizer.zero_grad()


global_step = 0


for epoch in range(100):

    for micro_step, (
        inputs,
        targets
    ) in enumerate(loader):

        inputs = inputs.to(device)

        targets = targets.to(device)


        causal_mask = (
            torch.triu(
                torch.full(
                    (
                        inputs.size(1),
                        inputs.size(1)
                    ),
                    float("-inf"),
                    device=device
                ),
                diagonal=1
            )
        )


        logits = model(
            inputs,
            causal_mask
        )


        loss = F.cross_entropy(
            logits.reshape(
                -1,
                logits.size(-1)
            ),
            targets.reshape(-1)
        )


        loss = (
            loss
            /
            config.gradient_accumulation_steps
        )


        loss.backward()


        if (
            micro_step + 1
        ) % config.gradient_accumulation_steps == 0:

            torch.nn.utils.clip_grad_norm_(
                model.parameters(),
                config.max_grad_norm
            )


            optimizer.step()

            optimizer.zero_grad()

            global_step += 1


            print(
                "step:",
                global_step,
                "loss:",
                loss.item()
                *
                config.gradient_accumulation_steps
            )


            if (
                global_step
                >=
                config.max_steps
            ):

                break


    if global_step >= config.max_steps:

        break