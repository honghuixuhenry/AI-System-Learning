import torch


def top_p_filter(
    logits,
    top_p
):

    sorted_logits, sorted_indices = (
        torch.sort(
            logits,
            descending=True,
            dim=-1
        )
    )


    sorted_probs = torch.softmax(
        sorted_logits,
        dim=-1
    )


    cumulative_probs = torch.cumsum(
        sorted_probs,
        dim=-1
    )


    remove_mask = (
        cumulative_probs
        >
        top_p
    )


    remove_mask[:, 1:] = (
        remove_mask[:, :-1].clone()
    )

    remove_mask[:, 0] = False


    sorted_logits = (
        sorted_logits.masked_fill(
            remove_mask,
            float("-inf")
        )
    )


    filtered_logits = (
        torch.full_like(
            logits,
            float("-inf")
        )
    )


    filtered_logits.scatter_(
        dim=-1,
        index=sorted_indices,
        src=sorted_logits
    )


    return filtered_logits