import os

import torch
import torch.distributed as dist
import torch.nn.functional as F

from torch.nn.parallel import (
    DistributedDataParallel as DDP
)

from torch.utils.data import (
    DataLoader
)

from torch.utils.data.distributed import (
    DistributedSampler
)


def train(
    model,
    dataset,
    epochs,
    micro_batch_size
):

    dist.init_process_group(
        backend="nccl"
    )


    rank = dist.get_rank()

    world_size = (
        dist.get_world_size()
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


    model = DDP(
        model,
        device_ids=[
            local_rank
        ]
    )


    sampler = DistributedSampler(
        dataset,
        num_replicas=world_size,
        rank=rank,
        shuffle=True
    )


    dataloader = DataLoader(
        dataset,
        batch_size=micro_batch_size,
        sampler=sampler
    )


    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=3e-4
    )


    for epoch in range(
        epochs
    ):

        sampler.set_epoch(
            epoch
        )


        model.train()


        for (
            input_ids,
            targets
        ) in dataloader:

            input_ids = (
                input_ids.to(
                    device
                )
            )

            targets = (
                targets.to(
                    device
                )
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


        if rank == 0:

            print(
                f"epoch={epoch}, "
                f"loss={loss.item():.4f}"
            )


    dist.destroy_process_group()