def search_documents(query):
    return {
        "results": [
            f"Document about {query}"
        ]
    }


def calculate_percentage(
    value,
    percentage
):
    return value * percentage


def send_mock_email(
    recipient,
    subject
):
    return {
        "status": "mock_sent",
        "recipient": recipient,
        "subject": subject
    }