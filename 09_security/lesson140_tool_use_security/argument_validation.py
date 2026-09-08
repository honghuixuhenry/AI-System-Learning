def validate_arguments(
    tool_name,
    arguments
):

    if tool_name == (
        "search_documents"
    ):

        query = arguments.get(
            "query"
        )

        if not isinstance(
            query,
            str
        ):
            return False

        if not query.strip():
            return False

        return True


    if tool_name == (
        "calculate_percentage"
    ):

        value = arguments.get(
            "value"
        )

        percentage = arguments.get(
            "percentage"
        )

        if not isinstance(
            value,
            (int, float)
        ):
            return False

        if not isinstance(
            percentage,
            (int, float)
        ):
            return False

        if not (
            0 <= percentage <= 1
        ):
            return False

        return True


    if tool_name == (
        "send_mock_email"
    ):

        recipient = arguments.get(
            "recipient"
        )

        subject = arguments.get(
            "subject"
        )

        return (
            isinstance(recipient, str)
            and
            isinstance(subject, str)
        )

    return False