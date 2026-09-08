class PlanExecutor:

    def __init__(
        self,
        tools
    ):
        self.tools = tools


    def execute_step(
        self,
        step
    ):

        description = (
            step.description
        )

        if description == "Search flight":

            return self.tools[
                "search_flight"
            ]()


        if description == "Search hotel":

            return self.tools[
                "search_hotel"
            ]()


        if (
            description
            ==
            "Calculate total cost"
        ):

            return self.tools[
                "calculate_cost"
            ]()


        if (
            description
            ==
            "Prepare itinerary"
        ):

            return self.tools[
                "prepare_itinerary"
            ]()


        raise ValueError(
            "Unknown plan step"
        )