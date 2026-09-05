import torch


def sample_next_token(
    logits,
    temperature=1.0,
    top_k=None,
    top_p=None
):

    if temperature == 0:

        return torch.argmax(
            logits,
            dim=-1,
            keepdim=True
        )


    if temperature < 0:

        raise ValueError(
            "temperature must be >= 0"
        )


    logits = (
        logits
        /
        temperature
    )


    if top_k is not None:

        if top_k <= 0:

            raise ValueError(
                "top_k must be positive"
            )

        logits = top_k_filter(
            logits,
            top_k
        )


    if top_p is not None:

        if not (
            0.0
            <
            top_p
            <=
            1.0
        ):

            raise ValueError(
                "top_p must be in (0, 1]"
            )

        logits = top_p_filter(
            logits,
            top_p
        )


    probs = torch.softmax(
        logits,
        dim=-1
    )


    return torch.multinomial(
        probs,
        num_samples=1
    )