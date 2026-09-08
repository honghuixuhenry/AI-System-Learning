Lesson 132
Planning & Reasoning Loops


Reactive Agent:

Observe
↓
Choose Next Action
↓
Act
↓
Observe


Planning Agent:

Goal
↓
Create Plan
↓
Execute Steps
↓
Observe
↓
Update Plan


Replanning Agent:

Plan
↓
Execute
↓
Observe
↓
Evaluate
↓
Replan when needed


Plan is runtime state.

A structured plan
is easier to:

execute
validate
track
resume
audit


Planning
is above
tool calling.

Plan:
sequence / graph
of intended tasks.

Each plan step
may invoke one or more tools.


Important:

Plan
!=
Authorization


Planner:
decides what tasks
should happen.

Executor:
runs plan steps.

Evaluator:
checks results.

Scheduler:
decides when/where
work executes.


Retry
!=
Replan

Retry:
same action again.

Replan:
change strategy.


Replanning
!=
Restarting.

Keep completed work.


Plans can include:

steps
dependencies
constraints
success criteria
permissions


Independent plan steps
can execute in parallel.


Complex plans may form:

DAGs
or
hierarchical subgoals.


Use deterministic validation
when possible.

Do not use an LLM
for checks that code
can verify reliably.


Agent planning should have:

max steps
max retries
max replans
timeout
cost budget


Planning has cost:

LLM calls
tokens
latency


More planning
does not always mean
better performance.


Adaptive strategy:

simple task
→ direct action

complex task
→ planning


A robust agent loop:

Plan
↓
Validate
↓
Execute
↓
Observe
↓
Evaluate
↓
Retry / Replan / Finish