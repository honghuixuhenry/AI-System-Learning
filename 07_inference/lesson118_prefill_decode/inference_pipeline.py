def inference_pipeline(
    prompt_tokens,
    max_new_tokens
):

    print(
        "=== Prefill ==="
    )

    print(
        "Process prompt:",
        prompt_tokens
    )


    generated_tokens = []


    for step in range(
        max_new_tokens
    ):

        print(
            f"=== Decode {step + 1} ==="
        )

        print(
            "Generate one token"
        )

        new_token = step

        generated_tokens.append(
            new_token
        )


    return generated_tokens


tokens = inference_pipeline(
    prompt_tokens=[
        10,
        20,
        30,
        40
    ],
    max_new_tokens=3
)


print(tokens)