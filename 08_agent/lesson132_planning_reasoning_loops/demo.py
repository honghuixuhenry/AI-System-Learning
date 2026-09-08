from planning_agent import (
    PlanningAgent
)

from plan_executor import (
    PlanExecutor
)


def search_flight():
    return {
        "flight": "F100",
        "price": 300
    }


def search_hotel():
    return {
        "hotel": "Hotel A",
        "price": 400
    }


def calculate_cost():
    return 700


def prepare_itinerary():
    return (
        "Flight F100 + Hotel A"
    )


tools = {
    "search_flight":
        search_flight,

    "search_hotel":
        search_hotel,

    "calculate_cost":
        calculate_cost,

    "prepare_itinerary":
        prepare_itinerary
}


planner = PlanningAgent()

executor = PlanExecutor(
    tools
)


plan = planner.create_plan(
    "Prepare a business trip"
)


while not plan.done():

    step = (
        plan.get_current_step()
    )

    print(
        "Executing:",
        step.description
    )

    result = (
        executor.execute_step(
            step
        )
    )

    plan.complete_current_step(
        result
    )

    print(
        "Result:",
        result
    )