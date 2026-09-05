print(
    "X:",
    x.shape
)

print(
    "Q:",
    Q.shape
)

print(
    "K:",
    K.shape
)

print(
    "V:",
    V.shape
)

print(
    "K^T:",
    K.transpose(
        -2,
        -1
    ).shape
)

print(
    "scores:",
    scores.shape
)

print(
    "weights:",
    weights.shape
)

print(
    "output:",
    output.shape
)