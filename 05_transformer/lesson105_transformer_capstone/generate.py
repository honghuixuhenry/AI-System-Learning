@torch.no_grad()
def generate(
    model,
    tokenizer,
    prompt,
    device,
    max_new_tokens=20,
    temperature=0.8,
    top_k=5
):

    model.eval()


    prompt_ids = tokenizer.encode(
        prompt,
        add_special_tokens=False
    )


    tokens = torch.tensor(
        [
            [
                tokenizer.bos_id,
                *prompt_ids
            ]
        ],
        dtype=torch.long,
        device=device
    )


    for _ in range(
        max_new_tokens
    ):

        logits = model(
            tokens
        )


        next_token_logits = (
            logits[:, -1, :]
        )


        next_token = (
            sample_next_token(
                next_token_logits,
                temperature=temperature,
                top_k=top_k
            )
        )


        if (
            next_token.item()
            ==
            tokenizer.eos_id
        ):

            break


        tokens = torch.cat(
            [
                tokens,
                next_token
            ],
            dim=1
        )


    return tokenizer.decode(
        tokens[0].tolist()
    )