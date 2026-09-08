from benchmark_dataset import (
    BENCHMARK_CASES
)

from system_under_test import (
    ToyAgentSystem
)

from evaluator import (
    SecurityEvaluator
)

from benchmark_runner import (
    BenchmarkRunner
)


system = ToyAgentSystem()

evaluator = SecurityEvaluator()

runner = BenchmarkRunner(
    system=system,
    evaluator=evaluator
)


for case in BENCHMARK_CASES:

    result = runner.run_case(
        case
    )

    print(
        case.case_id,
        result["evaluation"]
    )