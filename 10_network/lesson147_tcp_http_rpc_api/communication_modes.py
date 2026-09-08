COMMUNICATION_MODES = {

    "request_response": {
        "example":
            "REST API",

        "pattern":
            "one request -> one response"
    },

    "server_streaming": {
        "example":
            "LLM token streaming",

        "pattern":
            "one request -> many messages"
    },

    "bidirectional": {
        "example":
            "WebSocket",

        "pattern":
            "client <-> server"
    },

    "rpc": {
        "example":
            "embedding service",

        "pattern":
            "remote procedure call"
    }
}