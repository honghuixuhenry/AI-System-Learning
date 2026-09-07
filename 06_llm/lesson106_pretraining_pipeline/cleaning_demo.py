import re


def clean_text(
    text
):

    text = text.strip()

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text


raw_text = """
    Large     language

    models    are
    interesting.
"""


cleaned = clean_text(
    raw_text
)


print(
    cleaned
)

def keep_document(
    text
):

    words = text.split()

    if len(words) < 5:
        return False

    return True
cleaned_documents = []


for document in documents:

    document = clean_text(
        document
    )

    if keep_document(
        document
    ):

        cleaned_documents.append(
            document
        )


def deduplicate(
    documents
):

    seen = set()

    result = []


    for document in documents:

        if document in seen:
            continue

        seen.add(
            document
        )

        result.append(
            document
        )


    return result