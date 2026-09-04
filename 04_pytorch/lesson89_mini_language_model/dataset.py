import torch

from torch.utils.data import Dataset


class NextTokenDataset(
    Dataset
):

    def __init__(
        self,
        sentences,
        token_to_id
    ):

        self.samples = []

        for sentence in sentences:

            tokens = sentence.split()

            ids = [
                token_to_id[token]
                for token in tokens
            ]

            for i in range(
                len(ids) - 1
            ):

                x = ids[i]

                y = ids[i + 1]

                self.samples.append(
                    (
                        x,
                        y
                    )
                )

    def __len__(
        self
    ):

        return len(
            self.samples
        )

    def __getitem__(
        self,
        index
    ):

        x, y = self.samples[
            index
        ]

        return (
            torch.tensor(
                x,
                dtype=torch.long
            ),
            torch.tensor(
                y,
                dtype=torch.long
            )
        )