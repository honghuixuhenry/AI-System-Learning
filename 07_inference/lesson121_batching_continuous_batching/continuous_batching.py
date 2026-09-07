from collections import deque


waiting = deque([
    ("A", 3),
    ("B", 7),
    ("C", 2),
    ("D", 5),
    ("E", 4)
])


max_batch_size = 2

active = []


while waiting or active:

    while (
        waiting
        and
        len(active) < max_batch_size
    ):

        request_id, remaining = (
            waiting.popleft()
        )

        active.append({
            "id": request_id,
            "remaining": remaining
        })


    print(
        "Active:",
        [
            r["id"]
            for r in active
        ]
    )


    for request in active:

        request["remaining"] -= 1


    active = [
        request
        for request in active
        if request["remaining"] > 0
    ]