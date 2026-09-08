class BenchmarkRunner:

    def __init__(
        self,
        system,
        evaluator
    ):
        self.system = system
        self.evaluator = evaluator


    def run_case(
        self,
        case
    ):

        trace = self.system.run(
            task=case.task,
            input_text=case.input_text
        )

        evaluation = (
            self.evaluator.evaluate(
                case,
                trace
            )
        )

        return {
            "case":
                case,

            "trace":
                trace,

            "evaluation":
                evaluation
        }