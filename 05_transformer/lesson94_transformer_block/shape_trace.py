def forward(self, x):

    print(
        "input:",
        x.shape
    )


    norm1 = self.norm1(
        x
    )

    print(
        "norm1:",
        norm1.shape
    )


    attn_output, weights = (
        self.attention(
            norm1
        )
    )

    print(
        "attention:",
        attn_output.shape
    )

    print(
        "weights:",
        weights.shape
    )


    x = x + attn_output

    print(
        "residual1:",
        x.shape
    )


    norm2 = self.norm2(
        x
    )

    print(
        "norm2:",
        norm2.shape
    )


    ffn_output = self.ffn(
        norm2
    )

    print(
        "ffn:",
        ffn_output.shape
    )


    x = x + ffn_output

    print(
        "output:",
        x.shape
    )


    return x