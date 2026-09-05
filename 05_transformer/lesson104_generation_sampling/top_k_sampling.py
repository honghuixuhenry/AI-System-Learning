import torch


def top_k_filter(
    logits,
    k
):

    top_values, _ = torch.topk(
        logits,
        k=k,
        dim=-1
    )


    threshold = (
        top_values[:, -1]
        .unsqueeze(-1)
    )


    filtered_logits = (
        logits.masked_fill(
            logits < threshold,
            float("-inf")
        )
    )


    return filtered_logits