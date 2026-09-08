from injection_detector import (
    detect_suspicious_text
)

from secure_agent import (
    SecureAgent
)


document = """
This document contains
untrusted external content.
"""


agent = SecureAgent(
    allowed_tools=[
        "read_document"
    ]
)


print(
    "Suspicious:",
    detect_suspicious_text(
        document
    )
)


requested_tool = (
    "send_email"
)


if agent.authorize_tool(
    requested_tool
):
    print(
        "Tool authorized."
    )
else:
    print(
        "Tool denied:",
        requested_tool
    )