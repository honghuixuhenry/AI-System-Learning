Lesson 144

Agentic AI Security
Benchmark


Traditional Benchmark:

Prompt
↓
Model
↓
Response


Agentic Benchmark:

Attack
↓
Model
↓
Plan
↓
Tool
↓
Runtime
↓
Memory
↓
External Action


Benchmark Case:

Attack Source
Category
Target
Task
Security Property
Expected Behavior


Security Property:

property that
must not be violated.


Benchmark Dataset:

Benign Cases
+
Attack Cases


Execution Trace:

model output
tool proposal
tool execution
memory write
runtime decision
external action


Prefer:

deterministic evaluation

for:

tool execution
authorization
memory writes
external actions


Security
+
Utility


Metrics:

ASR
UTPR
UAR
PRR
MCR
BTSR


Define denominators
and success criteria
explicitly.


Repeated Trials:

important for
stochastic models.


Runtime security:

prefer deterministic.


Stochastic Intelligence
+
Deterministic Enforcement


Prevention:

stop attack early.


Containment:

limit consequences
after manipulation.


Model attack success
!=
system attack success.


Benchmark goal:

measure
where attack propagates
and where defense stops it.