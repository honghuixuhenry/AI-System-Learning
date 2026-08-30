import os

from dotenv import load_dotenv


load_dotenv()


MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "Qwen"
)

PORT = int(
    os.getenv(
        "PORT",
        "8000"
    )
)

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)

API_KEY = os.environ[
    "API_KEY"
]