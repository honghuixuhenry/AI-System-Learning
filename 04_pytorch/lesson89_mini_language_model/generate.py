import torch


def predict_next_token(
    model,
    token,
    token_to_id,
    id_to_token,
    device
):

    model.eval()


    token_id = token_to_id[
        token
    ]


    x = torch.tensor(
        [token_id],
        dtype=torch.long,
        device=device
    )


    with torch.inference_mode():

        logits = model(
            x
        )


    next_id = (
        logits[
            0
        ]
        .argmax()
        .item()
    )


    return id_to_token[
        next_id
    ]

def generate(
    model,
    start_token,
    steps,
    token_to_id,
    id_to_token,
    device
):

    tokens = [
        start_token
    ]


    current_token = (
        start_token
    )


    for _ in range(
        steps
    ):

        next_token = predict_next_token(
            model,
            current_token,
            token_to_id,
            id_to_token,
            device
        )


        tokens.append(
            next_token
        )


        current_token = (
            next_token
        )


    return " ".join(
        tokens
    )