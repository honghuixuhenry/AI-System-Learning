from collections import deque


waiting = deque([
    {"id": "A", "remaining": 3},
    {"id": "B", "remaining": 8},
    {"id": "C", "remaining": 2},
    {"id": "D", "remaining": 5},
    {"id": "E", "remaining": 4},
])


active = []

max_batch_size = 3

iteration = 0


while waiting or active:

    iteration += 1


    while (
        waiting
        and
        len(active)
        <
        max_batch_size
    ):

        active.append(
            waiting.popleft()
        )


    print(
        f"\nIteration {iteration}"
    )

    print(
        "Running:",
        [
            r["id"]
            for r in active
        ]
    )


    for request in active:

        request["remaining"] -= 1


    finished = [
        request
        for request in active
        if request["remaining"] == 0
    ]


    for request in finished:

        print(
            "Finished:",
            request["id"]
        )


    active = [
        request
        for request in active
        if request["remaining"] > 0
    ]