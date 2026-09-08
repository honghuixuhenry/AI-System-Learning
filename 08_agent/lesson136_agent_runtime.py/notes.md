Lesson 136
Agent Runtime Architecture
& MCP-Style Tool Systems


Agent Runtime:

Loop
+
Tools
+
Memory
+
Planning
+
RAG
+
Communication


Agent:

makes decisions.

Runtime:

coordinates execution.


Agent Runtime
!=
LLM Serving Runtime


Agent Runtime:

Goal
↓
Build Context
↓
LLM
↓
Structured Decision
↓
Validate
↓
Authorize
↓
Execute
↓
Observation
↓
Update State
↓
Repeat


Tool Calling:

model expresses
which capability
it wants to invoke.


Tool Provider:

exposes capabilities.


Tool Client:

connects runtime
to provider.


Tool Discovery:

runtime discovers
available capabilities
dynamically.


Static Registry:

manually registered tools.


Dynamic Discovery:

provider advertises tools.


MCP-style mental model:

Host
↓
Client
↓
Protocol Boundary
↓
Server
↓
Tools / Resources


Host:

main AI application.


Client:

protocol-side connector
inside the host.


Server:

capability provider.


Tool:

action capability.


Resource:

readable context/data.


Important:

Function Calling
!=
MCP-style integration


Function Calling:

LLM → Runtime


Capability Protocol:

Runtime → External Provider


Discoverable
!=
Authorized


Tool selection
!=
Execution permission


LLM tool call
is a proposed action,
not trusted execution.


Runtime should:

validate schema
check authorization
apply policy
control side effects
enforce limits


Tool result
is observation,
not trusted instruction.


Use:

timeouts
max steps
max tool calls
cost budget
token budget


Remote tools introduce:

network failures
authentication
rate limits
protocol errors
versioning


Tool providers
may be namespaced:

web.search
documents.search
calendar.create_event


Runtime is an important
security enforcement point.


Prompt policy
alone is weaker than
runtime enforcement.


Agent architecture:

Decision
→ Orchestration
→ Integration
→ Capability