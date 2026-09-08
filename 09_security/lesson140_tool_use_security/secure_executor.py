from tool_models import (
    ToolResult
)

from tool_registry import (
    TOOLS
)

from authorization import (
    authorize_tool
)

from argument_validation import (
    validate_arguments
)


class SecureToolExecutor:

    def execute(
        self,
        tool_call
    ):

        tool_name = (
            tool_call.tool_name
        )

        if tool_name not in TOOLS:

            return ToolResult(
                tool_name=tool_name,
                success=False,
                error="Unknown tool."
            )

        if not authorize_tool(
            tool_call.agent_id,
            tool_call.task_id,
            tool_name
        ):

            return ToolResult(
                tool_name=tool_name,
                success=False,
                error=(
                    "Tool call "
                    "is not authorized."
                )
            )

        if not validate_arguments(
            tool_name,
            tool_call.arguments
        ):

            return ToolResult(
                tool_name=tool_name,
                success=False,
                error=(
                    "Invalid arguments."
                )
            )

        try:

            result = TOOLS[
                tool_name
            ](
                **tool_call.arguments
            )

            return ToolResult(
                tool_name=tool_name,
                success=True,
                output=result
            )

        except Exception:

            return ToolResult(
                tool_name=tool_name,
                success=False,
                error=(
                    "Tool execution failed."
                )
            )