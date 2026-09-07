def unique_word_ratio(
    text
):

    words = text.split()

    if not words:
        return 0.0

    return (
        len(set(words))
        /
        len(words)
    )


def passes_quality_filter(
    text,
    min_words=5,
    max_words=5000,
    min_unique_ratio=0.2
):

    words = text.split()

    num_words = len(
        words
    )

    if (
        num_words < min_words
        or
        num_words > max_words
    ):
        return False


    if (
        unique_word_ratio(text)
        <
        min_unique_ratio
    ):
        return False


    return True