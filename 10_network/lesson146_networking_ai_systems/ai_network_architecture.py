from endpoints import Endpoint


LLM_SERVER = Endpoint(
    protocol="http",
    host="10.0.0.20",
    port=8000,
    path="/v1/chat"
)


RAG_SERVER = Endpoint(
    protocol="http",
    host="10.0.0.21",
    port=8001,
    path="/search"
)


TOOL_SERVER = Endpoint(
    protocol="http",
    host="10.0.0.22",
    port=8002,
    path="/tools"
)