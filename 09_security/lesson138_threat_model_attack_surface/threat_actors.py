THREAT_ACTORS = [
    {
        "name": "malicious_user",
        "capabilities": [
            "send_prompts",
            "submit_content"
        ]
    },

    {
        "name": "external_attacker",
        "capabilities": [
            "interact_with_public_interfaces"
        ]
    },

    {
        "name": "malicious_document",
        "capabilities": [
            "influence_retrieved_context"
        ]
    },

    {
        "name": "compromised_tool",
        "capabilities": [
            "return_malicious_output"
        ]
    },

    {
        "name": "compromised_agent",
        "capabilities": [
            "send_malicious_messages"
        ]
    },

    {
        "name": "insider",
        "capabilities": [
            "modify_internal_data"
        ]
    }
]