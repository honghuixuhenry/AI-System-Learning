import hashlib


def sha256_file(
    file_path: str
) -> str:

    hasher = hashlib.sha256()

    with open(
        file_path,
        "rb"
    ) as file:

        while True:

            chunk = file.read(
                1024 * 1024
            )

            if not chunk:
                break

            hasher.update(
                chunk
            )

    return hasher.hexdigest()

def verify_hash(
    file_path: str,
    expected_hash: str
) -> bool:

    actual_hash = (
        sha256_file(
            file_path
        )
    )

    return (
        actual_hash
        ==
        expected_hash
    )