import torch


grad_rank0 = torch.tensor(
    [1.0, 2.0]
)

grad_rank1 = torch.tensor(
    [3.0, 4.0]
)

grad_rank2 = torch.tensor(
    [5.0, 6.0]
)

grad_rank3 = torch.tensor(
    [7.0, 8.0]
)


all_gradients = torch.stack(
    [
        grad_rank0,
        grad_rank1,
        grad_rank2,
        grad_rank3
    ]
)


global_gradient = (
    all_gradients.mean(
        dim=0
    )
)


print(
    global_gradient
)