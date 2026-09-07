import torch
import torch.nn.functional as F


def attention_with_cache(
    q_new,
    k_new,
    v_new,
    k_cache=None,
    v_cache=None
):

    if k_cache is not None:

        k_all = torch.cat(
            [k_cache, k_new],
            dim=2
        )

        v_all = torch.cat(
            [v_cache, v_new],
            dim=2
        )

    else:

        k_all = k_new
        v_all = v_new


    head_dim = q_new.size(-1)


    scores = (
        q_new
        @
        k_all.transpose(-2, -1)
    ) / (head_dim ** 0.5)


    weights = F.softmax(
        scores,
        dim=-1
    )


    output = (
        weights
        @
        v_all
    )


    return (
        output,
        k_all,
        v_all
    )