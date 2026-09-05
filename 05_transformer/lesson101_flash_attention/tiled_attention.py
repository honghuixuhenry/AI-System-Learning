import math

import torch


def tiled_score_demo(
    q,
    k,
    block_size
):
    # q, k:
    # (T,Dh)

    T = q.shape[0]
    Dh = q.shape[-1]

    for q_start in range(
        0,
        T,
        block_size
    ):

        q_end = min(
            q_start + block_size,
            T
        )

        q_block = q[
            q_start:q_end
        ]


        for k_start in range(
            0,
            T,
            block_size
        ):

            k_end = min(
                k_start + block_size,
                T
            )

            k_block = k[
                k_start:k_end
            ]


            score_block = (
                q_block
                @
                k_block.T
            ) / math.sqrt(
                Dh
            )


            print(
                "Q block:",
                q_start,
                q_end
            )

            print(
                "K block:",
                k_start,
                k_end
            )

            print(
                "Score block:",
                score_block.shape
            )