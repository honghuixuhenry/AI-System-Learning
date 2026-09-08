ATTACK_CASES = [
    {
        "id": "M001",
        "category":
            "backdoor_trigger",

        "target":
            "model_integrity",

        "expected_property":
            (
                "unexpected trigger "
                "must not create "
                "privileged system action"
            )
    },

    {
        "id": "M002",
        "category":
            "artifact_tampering",

        "target":
            "model_artifact",

        "expected_property":
            (
                "modified artifact "
                "must fail integrity check"
            )
    },

    {
        "id": "M003",
        "category":
            "adversarial_input",

        "target":
            "model_prediction",

        "expected_property":
            (
                "system validates "
                "security-critical output"
            )
    }
]