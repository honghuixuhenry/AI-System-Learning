from models import ToolProposal


class LLMService:

    def decide(
        self,
        task_type: str,
        prompt: str
    ):

        if (
            task_type
            == "research"
        ):

            return ToolProposal(
                tool_name=(
                    "documents.search"
                ),
                capability=(
                    "documents.search"
                ),
                arguments={
                    "query":
                        prompt
                }
            )

        return None