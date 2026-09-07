import torch


def generate(
    model,
    token_ids,
    max_new_tokens
):

    for _ in range(
        max_new_tokens
    ):

        logits = model(
            token_ids
        )

        next_token_logits = (
            logits[:, -1, :]
        )

        next_token = torch.argmax(
            next_token_logits,
            dim=-1,
            keepdim=True
        )

        token_ids = torch.cat(
            [
                token_ids,
                next_token
            ],
            dim=1
        )

    return token_ids