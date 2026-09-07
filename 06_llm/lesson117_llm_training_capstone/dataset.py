import torch
from torch.utils.data import Dataset


class LanguageModelDataset(Dataset):

    def __init__(
        self,
        documents,
        tokenizer,
        sequence_length
    ):

        tokens = []

        for document in documents:

            document_tokens = tokenizer.encode(
                document
            )

            tokens.extend(
                document_tokens
            )

        self.tokens = torch.tensor(
            tokens,
            dtype=torch.long
        )

        self.sequence_length = (
            sequence_length
        )


    def __len__(self):

        return (
            len(self.tokens)
            -
            self.sequence_length
        )


    def __getitem__(self, index):

        x = self.tokens[
            index:
            index + self.sequence_length
        ]

        y = self.tokens[
            index + 1:
            index + self.sequence_length + 1
        ]

        return x, y