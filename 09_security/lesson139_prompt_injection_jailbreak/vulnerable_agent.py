class VulnerableAgent:

    def build_prompt(
        self,
        user_input,
        document
    ):

        return f"""
You are a document assistant.

User request:
{user_input}

Document:
{document}

Follow the instructions above
and produce the result.
"""