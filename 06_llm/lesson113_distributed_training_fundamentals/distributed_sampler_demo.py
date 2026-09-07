from torch.utils.data import Dataset
from torch.utils.data.distributed import (
    DistributedSampler
)


class NumberDataset(
    Dataset
):

    def __init__(self, n):
        self.data = list(
            range(n)
        )

    def __len__(self):
        return len(
            self.data
        )

    def __getitem__(self, index):
        return self.data[index]


dataset = NumberDataset(
    16
)


world_size = 4


for rank in range(
    world_size
):

    sampler = DistributedSampler(
        dataset,
        num_replicas=world_size,
        rank=rank,
        shuffle=False
    )


    indices = list(
        iter(sampler)
    )


    print(
        "rank:",
        rank,
        "indices:",
        indices
    )