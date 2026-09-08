class Agent:

    def __init__(
        self,
        name
    ):
        self.name = name


    def run(
        self,
        task,
        context
    ):
        raise NotImplementedError


class ResearchAgent(
    Agent
):

    def run(
        self,
        task,
        context
    ):

        documents = (
            context[
                "retriever"
            ].retrieve(
                task.description,
                top_k=4
            )
        )

        memory_result = (
            context[
                "tools"
            ].call(
                "estimate_model_memory",
                {
                    "parameters_billion":
                        7,

                    "bytes_per_parameter":
                        2
                }
            )
        )

        result = {
            "documents":
                documents,

            "hardware_estimate":
                memory_result
        }

        context[
            "memory"
        ].write(
            "research",
            result
        )

        return str(result)


class WriterAgent(
    Agent
):

    def run(
        self,
        task,
        context
    ):

        research = (
            context[
                "memory"
            ].read(
                "research"
            )
        )

        if research is None:

            raise RuntimeError(
                "Research result "
                "is missing."
            )

        report = (
            "Local LLM inference offers "
            "several potential benefits. "
            "It can reduce exposure of "
            "sensitive data to remote systems, "
            "reduce dependence on network "
            "connectivity, and may reduce "
            "network-related latency. "
            "However, local deployment can "
            "require substantial computing "
            "and memory resources. "
            "For example, a 7-billion-parameter "
            "model stored with 2 bytes per "
            "parameter requires about 14 GB "
            "for model weights alone."
        )

        context[
            "memory"
        ].write(
            "draft",
            report
        )

        return report

class ReviewerAgent(
    Agent
):

    def run(
        self,
        task,
        context
    ):

        draft = (
            context[
                "memory"
            ].read(
                "draft"
            )
        )

        if draft is None:

            raise RuntimeError(
                "Draft is missing."
            )

        required_terms = [
            "benefits",
            "memory"
        ]

        review = {
            "approved":
                len(draft) > 100,

            "notes":
                (
                    "Draft includes both "
                    "advantages and resource "
                    "limitations."
                )
        }

        context[
            "memory"
        ].write(
            "review",
            review
        )

        return str(review)