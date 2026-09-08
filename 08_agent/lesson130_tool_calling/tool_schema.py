WEATHER_TOOL_SCHEMA = {
    "name": "get_weather",

    "description":
        "Get the weather "
        "for a specified city.",

    "parameters": {
        "type": "object",

        "properties": {
            "city": {
                "type": "string",
                "description":
                    "City name"
            }
        },

        "required": [
            "city"
        ]
    }
}


CALCULATOR_TOOL_SCHEMA = {
    "name": "calculator",

    "description":
        "Evaluate a basic "
        "arithmetic expression.",

    "parameters": {
        "type": "object",

        "properties": {
            "expression": {
                "type": "string"
            }
        },

        "required": [
            "expression"
        ]
    }
}


TOOLS = [
    WEATHER_TOOL_SCHEMA,
    CALCULATOR_TOOL_SCHEMA
]