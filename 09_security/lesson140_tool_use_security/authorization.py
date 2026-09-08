AGENT_PERMISSIONS = {
    "research_agent": {
        "search_documents",
        "calculate_percentage"
    },

    "communication_agent": {
        "send_mock_email"
    }
}

TASK_PERMISSIONS = {
    "research_task": {
        "search_documents",
        "calculate_percentage"
    },

    "send_report_task": {
        "send_mock_email"
    }
}

def is_tool_allowed(
    agent_id,
    tool_name
):

    allowed = (
        AGENT_PERMISSIONS.get(
            agent_id,
            set()
        )
    )

    return tool_name in allowed

def authorize_tool(
    agent_id,
    task_id,
    tool_name
):

    agent_allowed = (
        tool_name
        in AGENT_PERMISSIONS.get(
            agent_id,
            set()
        )
    )

    task_allowed = (
        tool_name
        in TASK_PERMISSIONS.get(
            task_id,
            set()
        )
    )

    return (
        agent_allowed
        and
        task_allowed
    )