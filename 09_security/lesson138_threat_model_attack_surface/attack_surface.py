ATTACK_SURFACES = [
    {
        "component": "user_input",
        "entry_points": [
            "chat_prompt",
            "file_upload"
        ]
    },

    {
        "component": "rag",
        "entry_points": [
            "documents",
            "retrieval_results"
        ]
    },

    {
        "component": "memory",
        "entry_points": [
            "memory_write",
            "memory_retrieval"
        ]
    },

    {
        "component": "tools",
        "entry_points": [
            "tool_arguments",
            "tool_outputs"
        ]
    },

    {
        "component": "multi_agent",
        "entry_points": [
            "agent_messages",
            "task_handoffs"
        ]
    },

    {
        "component": "runtime",
        "entry_points": [
            "routing",
            "authorization",
            "execution"
        ]
    }
]