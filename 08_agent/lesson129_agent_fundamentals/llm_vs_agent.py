def llm_call(prompt):
    return (
        "LLM response to: "
        + prompt
    )


def simple_llm_app():
    prompt = (
        "Find the weather "
        "and decide whether "
        "I need an umbrella."
    )

    response = llm_call(
        prompt
    )

    print(response)


simple_llm_app()