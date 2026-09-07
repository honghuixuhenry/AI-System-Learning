from fastapi import FastAPI
from pydantic import BaseModel

from request import Request


app = FastAPI()


class GenerateRequest(
    BaseModel
):
    prompt: str
    max_new_tokens: int = 20


@app.post("/generate")
def generate(
    body: GenerateRequest
):

    request = Request(
        request_id="demo-request",
        prompt=body.prompt,
        max_new_tokens=(
            body.max_new_tokens
        )
    )

    return {
        "request_id":
            request.request_id,

        "status":
            request.status.value
    }