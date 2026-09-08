# Lesson 139
# Prompt Injection & Jailbreak Attacks

Prompt Injection:

untrusted input manipulates
application-level model behavior.

Direct Prompt Injection:

malicious instruction enters
through user-controlled input.

Indirect Prompt Injection:

malicious instruction enters
through external content such as
documents, websites, emails,
RAG results, or tool outputs.

Jailbreak:

attempt to bypass
model-level behavioral
or safety constraints.

Important:

Prompt Injection
!=
Jailbreak

Prompt Injection
!=
Indirect Prompt Injection

Agent systems increase risk because:

model output
can become
external action.

Core security principle:

Untrusted Data
must not automatically
become Trusted Control.

LLM Proposal
!=
Execution Permission.

Model-Level Attack Success
!=
System-Level Attack Success.

Important defenses:

least privilege
task-scoped authorization
data/control separation
provenance
tool allowlists
schema validation
human approval
sandboxing
audit logging

Prompt detectors
are useful signals,
not complete security boundaries.