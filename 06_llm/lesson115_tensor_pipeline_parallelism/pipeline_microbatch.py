import torch


batch = torch.randn(
    8,
    16
)


micro_batches = torch.chunk(
    batch,
    chunks=4,
    dim=0
)


for i, micro_batch in enumerate(
    micro_batches
):

    print(
        "micro batch:",
        i,
        "shape:",
        micro_batch.shape
    )