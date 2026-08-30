from fastapi import Header, HTTPexception
from security.api_key import verify_api_key
from typing import Optional

USER = {
    "key-alice": {
        "username": "alice",
        "role": "user"
    },
    "key-bob": {
        "username": "bob",
        "role": "admin"
    }
}

def authenticate(
        x_api_key: Optional[str] = Header(
            default=None
        )
):
    user = USER.get(x_api_key)
    if user is None:
        raise HTTPexception(
            status_code = 401,
            detail = "Invalid API key"
        )
    return user