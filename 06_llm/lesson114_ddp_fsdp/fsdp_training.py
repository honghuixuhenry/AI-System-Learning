import os

import torch
import torch.distributed as dist
import torch.nn.functional as F

from torch.distributed.fsdp import (
    FullyShardedDataParallel as FSDP
)


def train(
    model,
    dataloader
):

    dist.init_process_group(
        backend="nccl"
    )


    local_rank = int(
        os.environ["LOCAL_RANK"]
    )


    torch.cuda.set_device(
        local_rank
    )


    device = torch.device(
        f"cuda:{local_rank}"
    )


    model = model.to(
        device
    )


    model = FSDP(
        model
    )


    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=3e-4
    )


    model.train()


    for (
        input_ids,
        targets
    ) in dataloader:

        input_ids = input_ids.to(
            device
        )

        targets = targets.to(
            device
        )


        optimizer.zero_grad()


        logits = model(
            input_ids
        )


        loss = F.cross_entropy(
            logits.reshape(
                -1,
                logits.size(-1)
            ),
            targets.reshape(-1)
        )


        loss.backward()


        optimizer.step()


    dist.destroy_process_group()