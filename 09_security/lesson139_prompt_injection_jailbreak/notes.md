Lesson 139
Prompt Injection
& Jailbreak


Prompt Injection:

manipulates
application instructions.


Direct Injection:

user input
contains attack.


Indirect Injection:

external data
contains attack.


Examples of
external sources:

web page
email
PDF
RAG document
tool result
agent message


Jailbreak:

attempts to bypass
model behavioral
or safety constraints.


Prompt Injection
!=
Jailbreak


Core problem:

Data
may be interpreted
as Instruction.


Agentic risk:

Injection
↓
Decision Manipulation
↓
Tool Call
↓
External Consequence


Security principle:

Untrusted Data
must not become
Trusted Authority.


Prompt formatting
is helpful,
but not a
security boundary.


Keyword detector
!=
complete defense.


Security classifier
!=
complete defense.


Least privilege
reduces blast radius.


Task-scoped authorization:

permissions depend
on current task.


Model proposes actions.

Runtime authorizes actions.


LLM Decision
!=
Execution Permission


Tool Output
=
Untrusted Observation


Retrieved Document
=
Untrusted Data


Agent Message
=
Untrusted Input


Memory Write
is a privileged operation.


Model-Level Attack Success
!=
System-Level Attack Success


Metrics:

Attack Success Rate
Task Deviation Rate
Unauthorized Tool Proposal Rate
Unauthorized Action Rate
Data Disclosure Rate
Memory Contamination Rate


Defense in Depth:

reduce exposure
+
reduce interpretation risk
+
limit damage


Prompt Injection
and SQL Injection
share a
Data/Control Confusion analogy,
but are not
the same mechanism.


Assume model manipulation
may happen.

Contain consequences.