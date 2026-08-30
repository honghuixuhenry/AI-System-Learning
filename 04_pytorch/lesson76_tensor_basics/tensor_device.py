import torch


if torch.cuda.is_available():

    device = "cuda"

elif (
    hasattr(
        torch.backends,
        "mps"
    )
    and
    torch.backends.mps.is_available()
):

    device = "mps"

else:

    device = "cpu"


print(
    "device:",
    device
)


x = torch.tensor(
    [1., 2., 3.]
)

x = x.to(
    device
)

print(
    x.device
)