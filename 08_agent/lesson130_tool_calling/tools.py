def get_weather(city: str) -> str:

    fake_weather = {
        "Atlanta": "86°F",
        "New York": "75°F",
        "Los Angeles": "78°F"
    }

    return fake_weather.get(
        city,
        "Weather unavailable"
    )


def calculator(
    expression: str
) -> float:

    allowed_chars = set(
        "0123456789+-*/(). "
    )

    if not set(expression).issubset(
        allowed_chars
    ):
        raise ValueError(
            "Invalid expression"
        )

    return eval(
        expression,
        {"__builtins__": {}},
        {}
    )