import torch


B = 1
H_KV = 2
HEAD_DIM = 4


k_cache = None
v_cache = None


for step in range(5):

    k_new = torch.randn(
        B,
        H_KV,
        1,
        HEAD_DIM
    )


    v_new = torch.randn(
        B,
        H_KV,
        1,
        HEAD_DIM
    )


    if k_cache is None:

        k_cache = k_new
        v_cache = v_new

    else:

        k_cache = torch.cat(
            [
                k_cache,
                k_new
            ],
            dim=2
        )

        v_cache = torch.cat(
            [
                v_cache,
                v_new
            ],
            dim=2
        )


    print(
        f"step {step + 1}"
    )

    print(
        "K cache:",
        k_cache.shape
    )

    print(
        "V cache:",
        v_cache.shape
    )