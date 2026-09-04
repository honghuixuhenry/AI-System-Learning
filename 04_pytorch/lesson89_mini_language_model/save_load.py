checkpoint = {
    "model_state_dict":
        model.state_dict(),

    "optimizer_state_dict":
        optimizer.state_dict(),

    "token_to_id":
        token_to_id,

    "id_to_token":
        id_to_token
}

checkpoint = {
    "config": {
        "vocab_size": len(
            token_to_id
        ),
        "embedding_dim": 16,
        "hidden_dim": 32
    },

    "model_state_dict":
        model.state_dict(),

    "token_to_id":
        token_to_id,

    "id_to_token":
        id_to_token
}


torch.save(
    checkpoint,
    "mini_lm_checkpoint.pt"
)

checkpoint = torch.load(
    "mini_lm_checkpoint.pt",
    map_location=device
)


token_to_id = checkpoint[
    "token_to_id"
]


id_to_token = checkpoint[
    "id_to_token"
]


model = MiniLanguageModel(
    vocab_size=len(
        token_to_id
    )
).to(
    device
)


model.load_state_dict(
    checkpoint[
        "model_state_dict"
    ]
)