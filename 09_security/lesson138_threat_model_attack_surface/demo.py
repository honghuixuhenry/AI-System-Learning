from assets import ASSETS
from threat_actors import THREAT_ACTORS
from attack_surface import ATTACK_SURFACES
from trust_boundaries import TRUST_BOUNDARIES


print(
    "\n=== Assets ==="
)

for asset in ASSETS:
    print(
        asset["name"],
        asset["security_goals"]
    )


print(
    "\n=== Threat Actors ==="
)

for actor in THREAT_ACTORS:
    print(
        actor["name"]
    )


print(
    "\n=== Attack Surfaces ==="
)

for surface in ATTACK_SURFACES:
    print(
        surface["component"],
        surface["entry_points"]
    )


print(
    "\n=== Trust Boundaries ==="
)

for boundary in TRUST_BOUNDARIES:
    print(
        boundary["from"],
        "->",
        boundary["to"]
    )