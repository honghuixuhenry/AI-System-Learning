import time


def token_stream():

    tokens = [
        "Large",
        " language",
        " models",
        " generate",
        " tokens"
    ]

    for token in tokens:

        time.sleep(0.2)

        yield token


for token in token_stream():
    print(
        token,
        end="",
        flush=True
    )