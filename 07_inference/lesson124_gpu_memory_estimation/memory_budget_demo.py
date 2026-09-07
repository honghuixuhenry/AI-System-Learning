def max_requests_from_kv_budget(
    kv_budget_bytes,
    kv_per_request_bytes
):

    return int(
        kv_budget_bytes
        //
        kv_per_request_bytes
    )


kv_budget = (
    8
    *
    1024 ** 3
)


kv_per_request = (
    512
    *
    1024 ** 2
)


max_requests = (
    max_requests_from_kv_budget(
        kv_budget,
        kv_per_request
    )
)


print(
    "Theoretical max requests:",
    max_requests
)