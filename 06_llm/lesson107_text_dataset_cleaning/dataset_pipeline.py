from text_cleaning import (
    clean_text
)

from quality_filter import (
    passes_quality_filter
)

from deduplication import (
    text_hash
)


def process_dataset(
    documents
):

    processed = []

    seen_hashes = set()


    stats = {
        "raw": 0,
        "empty": 0,
        "low_quality": 0,
        "duplicate": 0,
        "kept": 0,
    }


    for document in documents:

        stats["raw"] += 1


        # -----------------------------
        # Cleaning
        # -----------------------------

        document.text = clean_text(
            document.text
        )


        if not document.text:

            stats["empty"] += 1

            continue


        # -----------------------------
        # Quality Filtering
        # -----------------------------

        if not passes_quality_filter(
            document.text
        ):

            stats[
                "low_quality"
            ] += 1

            continue


        # -----------------------------
        # Exact Deduplication
        # -----------------------------

        digest = text_hash(
            document.text
        )


        if digest in seen_hashes:

            stats[
                "duplicate"
            ] += 1

            continue


        seen_hashes.add(
            digest
        )


        processed.append(
            document
        )


        stats["kept"] += 1


    return (
        processed,
        stats
    )