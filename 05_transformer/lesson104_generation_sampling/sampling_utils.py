import torch


def sample_next_token(
    logits,
    temperature=1.0,
    top_k=None,
    top_p=None
):

    if temperature <= 0:

        return torch.argmax(
            logits,
            dim=-1,
            keepdim=True
        )


    logits = (
        logits
        /
        temperature
    )


    if top_k is not None:

        logits = top_k_filter(
            logits,
            top_k
        )


    if top_p is not None:

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