VALID_API_KEY = "secret123"

def verify_api_key(api_key: str) -> bool:
    return api_key == VALID_API_KEY

