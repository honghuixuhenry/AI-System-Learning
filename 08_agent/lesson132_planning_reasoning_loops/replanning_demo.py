def evaluate_result(
    step,
    result
):

    if (
        step.description
        ==
        "Search flight"
        and
        result is None
    ):
        return "REPLAN"

    return "CONTINUE"


def replan(
    old_plan
):

    print(
        "No flight found."
    )

    print(
        "New strategy:"
    )

    print(
        "Search nearby airports."
    )