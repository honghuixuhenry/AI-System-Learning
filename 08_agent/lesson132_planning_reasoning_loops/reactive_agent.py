class ReactiveAgent:

    def decide(
        self,
        state
    ):

        observations = (
            state["observations"]
        )

        if not observations:

            return {
                "action":
                    "search_flight"
            }

        if len(observations) == 1:

            return {
                "action":
                    "search_hotel"
            }

        if len(observations) == 2:

            return {
                "action":
                    "calculate_cost"
            }

        return {
            "action":
                "finish"
        }