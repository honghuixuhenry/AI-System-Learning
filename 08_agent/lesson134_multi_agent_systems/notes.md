Lesson 134
Multi-Agent Systems


Multi-Agent System:

multiple autonomous
decision/execution components
working toward tasks/goals.


Multiple LLM calls
do not automatically mean
multiple agents.


Agent may have:

role
state
tools
memory
permissions
task


Core architecture:

Coordinator
+
Worker Agents


Coordinator:

decompose tasks
assign tasks
coordinate order
collect results
handle failures


Worker Agent:

executes a specialized task.


Important:

Role
!=
Agent Instance


Multiple Agents
!=
Multiple Models


Agents may share
the same underlying LLM
with different:

prompts
tools
state
permissions


Shared State:

current information
shared between agents.


Shared State
can act like
shared working memory.


Benefits:

specialization
focused context
parallelism
capability isolation
modularity


Costs:

more LLM calls
more tokens
more latency
coordination overhead
more failure points


More Agents
!=
Better System


Architectures:

centralized
decentralized
hierarchical
blackboard


Common pattern:

Coordinator
→ Worker Agents
→ Aggregator


Workers can execute
in parallel
when tasks are independent.


Fan-Out / Fan-In:

one task
→ multiple workers
→ merge results


Agent output
must not automatically
be trusted by another agent.


Agent-to-Agent communication
needs:

schemas
validation
authorization


Shared state introduces:

race conditions
consistency issues
ownership problems


Multi-Agent systems
need:

task status
agent status
timeouts
budgets
observability


Delegation:

task
+
limited authority


Delegated agents
should follow
least privilege.


Prevent:

delegation loops
unbounded agent calls
unbounded token use


Consensus
!=
Truth


Multiple identical agents
can repeat
the same mistake.


Useful trace fields:

request_id
task_id
agent_id
parent_agent_id
tool_call_id
latency
tokens
errors


Multi-Agent Systems
combine concepts from:

AI Agents
Software Architecture
Concurrency
Distributed Systems
Security