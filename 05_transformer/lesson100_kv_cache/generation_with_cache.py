import torch


@torch.no_grad()
def generate_with_cache(
    model,
    input_ids,
    max_new_tokens
):

    model.eval()


    logits, past_key_values = model(
        input_ids,
        past_key_values=None,
        use_cache=True
    )


    next_token = torch.argmax(
        logits[:, -1, :],
        dim=-1,
        keepdim=True
    )


    generated = torch.cat(
        [
            input_ids,
            next_token
        ],
        dim=1
    )


    for _ in range(
        max_new_tokens - 1
    ):

        logits, past_key_values = model(
            next_token,
            past_key_values=past_key_values,
            use_cache=True
        )


        next_token = torch.argmax(
            logits[:, -1, :],
            dim=-1,
            keepdim=True
        )


        generated = torch.cat(
            [
                generated,
                next_token
            ],
            dim=1
        )


    return generated