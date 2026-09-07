def word_ngrams(
    text,
    n=3
):

    words = text.split()

    return {
        tuple(
            words[
                i:
                i+n
            ]
        )
        for i in range(
            len(words) - n + 1
        )
    }


def jaccard_similarity(
    a,
    b
):

    if not a and not b:
        return 1.0

    union = a | b

    if not union:
        return 0.0

    return (
        len(a & b)
        /
        len(union)
    )


text1 = (
    "large language models "
    "learn from text data"
)

text2 = (
    "large language models "
    "learn from large text data"
)


a = word_ngrams(
    text1,
    n=2
)

b = word_ngrams(
    text2,
    n=2
)


print(
    jaccard_similarity(
        a,
        b
    )
)