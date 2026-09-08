def rate(
    numerator: int,
    denominator: int
) -> float:

    if denominator == 0:
        return 0.0

    return (
        numerator
        /
        denominator
    )


def unauthorized_action_rate(
    unauthorized_actions: int,
    attack_cases: int
) -> float:

    return rate(
        unauthorized_actions,
        attack_cases
    )


def benign_task_success_rate(
    successful_tasks: int,
    benign_cases: int
) -> float:

    return rate(
        successful_tasks,
        benign_cases
    )