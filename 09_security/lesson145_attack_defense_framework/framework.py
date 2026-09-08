from attack_library import (
    ATTACK_LIBRARY
)

from system_under_test import (
    ToyAgentSystem
)

from evaluator import (
    evaluate
)


class AttackDefenseFramework:

    def __init__(
        self,
        defense
    ):
        self.defense = defense

        self.system = (
            ToyAgentSystem(
                defense
            )
        )


    def run(self):

        results = []

        for attack in ATTACK_LIBRARY:

            outcome = (
                self.system.process_attack(
                    attack
                )
            )

            result = evaluate(
                attack,
                outcome
            )

            results.append(
                result
            )

        return results