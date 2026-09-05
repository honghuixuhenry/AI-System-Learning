class SimpleTokenizer:

    def __init__(
        self,
        texts
    ):

        special_tokens = [
            "<pad>",
            "<bos>",
            "<eos>",
            "<unk>"
        ]


        words = set()

        for text in texts:

            words.update(
                text.split()
            )


        vocabulary = (
            special_tokens
            +
            sorted(words)
        )


        self.token_to_id = {
            token: idx
            for idx, token
            in enumerate(vocabulary)
        }


        self.id_to_token = {
            idx: token
            for token, idx
            in self.token_to_id.items()
        }


        self.pad_id = (
            self.token_to_id[
                "<pad>"
            ]
        )

        self.bos_id = (
            self.token_to_id[
                "<bos>"
            ]
        )

        self.eos_id = (
            self.token_to_id[
                "<eos>"
            ]
        )

        self.unk_id = (
            self.token_to_id[
                "<unk>"
            ]
        )
    def encode(
        self,
        text,
        add_special_tokens=True
    ):

        tokens = text.split()


        ids = [
            self.token_to_id.get(
                token,
                self.unk_id
            )
            for token in tokens
        ]


        if add_special_tokens:

            ids = [
                self.bos_id,
                *ids,
                self.eos_id
            ]


        return ids
    def decode(
        self,
        ids,
        skip_special_tokens=True
    ):

        tokens = []


        for idx in ids:

            token = (
                self.id_to_token[
                    int(idx)
                ]
            )


            if (
                skip_special_tokens
                and
                token in {
                    "<pad>",
                    "<bos>",
                    "<eos>"
                }
            ):

                continue


            tokens.append(
                token
            )


        return " ".join(
            tokens
        )