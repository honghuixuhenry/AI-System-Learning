import torch

from torch.utils.data import Dataset


class LanguageModelDataset(
    Dataset
):

    def __init__(
        self,
        texts,
        tokenizer,
        seq_len
    ):

        self.seq_len = seq_len


        all_ids = []


        for text in texts:

            ids = tokenizer.encode(
                text,
                add_special_tokens=True
            )

            all_ids.extend(
                ids
            )


        self.tokens = torch.tensor(
            all_ids,
            dtype=torch.long
        )
    def __len__(
        self
    ):

        return max(
            0,
            len(self.tokens)
            -
            self.seq_len
        )
    def __getitem__(
        self,
        index
    ):

        chunk = self.tokens[
            index:
            index
            +
            self.seq_len
            +
            1
        ]


        x = chunk[:-1]

        target = chunk[1:]


        return x, target