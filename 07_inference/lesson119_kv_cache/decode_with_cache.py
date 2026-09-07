def decode(
    model,
    first_token,
    k_cache,
    v_cache,
    max_new_tokens
):

    token = first_token


    for _ in range(
        max_new_tokens
    ):

        logits, k_cache, v_cache = (
            model.decode_step(
                token,
                k_cache,
                v_cache
            )
        )


        token = logits.argmax(
            dim=-1
        )


    return token