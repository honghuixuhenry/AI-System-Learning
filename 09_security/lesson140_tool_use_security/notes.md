Lesson 140
Tool-Use &
Function-Calling Security


LLM Tool Call
=
Proposed Action


Runtime
=
Execution Authority


Tool Selection
!=
Authorization


Valid JSON
!=
Safe Action


Structured Output
improves reliability,
not complete security.


Tool security checks:

tool exists
arguments valid
agent authorized
task authorized
semantic policy satisfied
approval obtained
execution controlled


Least Privilege:

expose only
required capabilities.


Capability Granularity:

prefer:

file.read
file.write
file.delete

instead of:

filesystem.do_everything


Task-Scoped Authorization:

permission depends
on current task.


Agent Permission
AND
Task Permission


Argument security:

presence
type
range
format
semantic constraints


Schema Valid
!=
Semantically Authorized


Side-effecting tools:

send
write
delete
purchase
transfer

need stronger controls.


Human approval:

must bind
to exact action
and exact arguments.


TOCTOU:

approved action
must not change
before execution.


Retries:

read-only retry
is usually safer.

side-effect retry
requires idempotency.


Tool Output
=
Untrusted Observation


Trusted Tool Server
!=
Trusted Tool Content


Discovery
!=
Permission


Tool metadata
may also be
untrusted input.


Confused Deputy:

high-privilege runtime
is manipulated
to perform action
for lower-privilege attacker.


Authority should derive from:

user intent
+
runtime policy

not from:

LLM text


Security Metrics:

Unauthorized Tool Proposal Rate

Unauthorized Tool Execution Rate

Argument Validation Failure Rate

Policy Denial Rate

External Side-Effect Rate


Model Compromise
!=
System Compromise