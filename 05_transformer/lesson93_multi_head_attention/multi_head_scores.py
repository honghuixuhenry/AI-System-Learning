import math

scores = (
    Q
    @
    K.transpose(
        -2,
        -1
    )
)


scores = (
    scores
    /
    math.sqrt(
        head_dim
    )
)


print(
    scores.shape
)