Lesson 143

Agent Authorization
Sandboxing
Least Privilege


Authentication:

Who are you?


Authorization:

What can you do?


Capability:

Specific authority
to perform an action.


Sandbox:

Restricted execution
environment.


Authentication
!=
Authorization

Authorization
!=
Sandboxing

Tool exists
!=
Tool permitted


Least Privilege:

minimum capability
required for task.


RBAC:

permissions
through roles.


ABAC:

permissions
through attributes.


Task-Scoped Authorization:

agent permission
AND
task permission


Effective Permission:

User
∩
Agent
∩
Task
∩
Resource
∩
Environment


Policy engine
should be deterministic.


LLM
!=
Authorization Engine


Agent cannot
self-authorize.


Delegation:

narrow
task-bound
resource-bound
time-limited


Credentials:

stay in runtime.

Do not expose
secrets to LLM.


Sandbox controls:

filesystem
network
CPU
memory
runtime
processes
credentials


Authorized Tool
!=
Unrestricted Execution


Container
!=
Perfect Sandbox


Agent Loop limits:

max steps
max tool calls
max tokens
max runtime
max cost


Fail Closed:

unknown
→ DENY


Allowlist
preferred for
sensitive capabilities.


Audit:

who
what
task
policy
decision
result


Denied actions
are security signals.


Core principle:

Assume model
can be compromised.

Keep authority
outside the model.