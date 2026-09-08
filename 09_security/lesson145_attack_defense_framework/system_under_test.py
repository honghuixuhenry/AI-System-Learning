class ToyAgentSystem:

    def __init__(
        self,
        defense
    ):
        self.defense = defense


    def process_attack(
        self,
        attack
    ):
        model_manipulated = True

        unauthorized_tool_proposed = (
            attack.category
            in {
                "prompt_injection",
                "model_backdoor"
            }
        )

        memory_contaminated = (
            attack.category
            in {
                "rag_poisoning",
                "memory_poisoning"
            }
            and
            not self.defense.memory_policy_enabled
        )

        unauthorized_tool_executed = (
            unauthorized_tool_proposed
            and
            not self.defense.authorization_enabled
        )

        return {
            "model_manipulated":
                model_manipulated,

            "unauthorized_tool_proposed":
                unauthorized_tool_proposed,

            "unauthorized_tool_executed":
                unauthorized_tool_executed,

            "memory_contaminated":
                memory_contaminated
        }