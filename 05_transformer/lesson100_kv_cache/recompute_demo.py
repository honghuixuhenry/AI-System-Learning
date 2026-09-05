import torch


def generate_without_cache(
    model,
    input_ids,
    max_new_tokens
):

    tokens = input_ids


    for _ in range(
        max_new_tokens
    ):

        logits = model(
            tokens
        )


        next_token_logits = (
            logits[:, -1, :]
        )


        next_token = torch.argmax(
            next_token_logits,
            dim=-1,
            keepdim=True
        )


        tokens = torch.cat(
            [
                tokens,
                next_token
            ],
            dim=1
        )


    return tokens