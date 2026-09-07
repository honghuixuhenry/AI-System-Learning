requests = {
    "A": 10,
    "B": 100,
    "C": 20,
    "D": 80
}


for step in range(
    max(requests.values())
):

    active = []

    for request_id, length in requests.items():

        if step < length:

            active.append(
                request_id
            )

    print(
        f"step {step + 1}:",
        active
    )