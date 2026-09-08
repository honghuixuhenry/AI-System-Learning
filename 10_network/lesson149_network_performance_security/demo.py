from authentication import (
    authenticate
)

from replay_protection import (
    ReplayProtector
)

from rate_limiter import (
    SimpleRateLimiter
)

from communication_policy import (
    authorize
)


replay = ReplayProtector()

limiter = SimpleRateLimiter(
    max_requests=3
)


api_key = (
    "demo-key-research"
)

request_id = (
    "request-100"
)

capability = (
    "documents.search"
)


identity = authenticate(
    api_key
)


if identity is None:
    print("DENY: unauthenticated")

elif not replay.accept(
    request_id
):
    print("DENY: replay")

elif not limiter.allow(
    identity.client_id
):
    print("DENY: rate limit")

elif not authorize(
    identity.role,
    capability
):
    print("DENY: unauthorized")

else:
    print(
        "ALLOW:",
        identity.client_id,
        capability
    )