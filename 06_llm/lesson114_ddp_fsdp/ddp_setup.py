import os

import torch
import torch.distributed as dist


def setup_distributed():

    dist.init_process_group(
        backend="nccl"
    )


    rank = dist.get_rank()

    world_size = dist.get_world_size()

    local_rank = int(
        os.environ["LOCAL_RANK"]
    )


    torch.cuda.set_device(
        local_rank
    )


    device = torch.device(
        f"cuda:{local_rank}"
    )


    return (
        rank,
        local_rank,
        world_size,
        device
    )


def cleanup_distributed():

    dist.destroy_process_group()