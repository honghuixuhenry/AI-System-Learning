TRUST_BOUNDARIES = [
    {
        "from": "user",
        "to": "agent_runtime",
        "reason": (
            "User input is untrusted."
        )
    },

    {
        "from": "external_documents",
        "to": "rag_pipeline",
        "reason": (
            "Retrieved content "
            "may be malicious."
        )
    },

    {
        "from": "agent_runtime",
        "to": "external_tools",
        "reason": (
            "External services "
            "have separate trust."
        )
    },

    {
        "from": "agent_a",
        "to": "agent_b",
        "reason": (
            "Agent output must not "
            "automatically become "
            "trusted control input."
        )
    }
]