from openai import OpenAI


client = OpenAI(
    base_url=(
        "http://localhost:8000/v1"
    ),
    api_key="dummy"
)


response = (
    client.chat.completions.create(
        model="my-model",
        messages=[
            {
                "role": "user",
                "content":
                    "Explain KV cache."
            }
        ]
    )
)


print(
    response
    .choices[0]
    .message
    .content
)