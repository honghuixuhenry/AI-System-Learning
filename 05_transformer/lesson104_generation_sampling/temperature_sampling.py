import torch


def get_probs(
    logits,
    temperature
):

    scaled_logits = (
        logits
        /
        temperature
    )

    return torch.softmax(
        scaled_logits,
        dim=-1
    )


logits = torch.tensor(
    [[1.0, 2.0, 3.0]]
)


for temperature in [
    0.5,
    1.0,
    2.0
]:

    probs = get_probs(
        logits,
        temperature
    )

    print(
        temperature,
        probs
    )