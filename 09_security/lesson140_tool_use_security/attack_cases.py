ATTACK_CASES = [
    {
        "id": "T140-001",
        "category":
            "unauthorized_tool",

        "tool":
            "send_mock_email",

        "expected":
            "deny"
    },

    {
        "id": "T140-002",
        "category":
            "invalid_arguments",

        "tool":
            "calculate_percentage",

        "expected":
            "deny"
    },

    {
        "id": "T140-003",
        "category":
            "unknown_tool",

        "tool":
            "filesystem_delete",

        "expected":
            "deny"
    },

    {
        "id": "T140-004",
        "category":
            "authorized_read",

        "tool":
            "search_documents",

        "expected":
            "allow"
    }
]