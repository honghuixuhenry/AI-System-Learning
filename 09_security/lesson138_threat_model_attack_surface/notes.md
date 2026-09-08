Lesson 138
AI System Threat Model
& Attack Surface


Threat Model:

System
+
Assets
+
Adversaries
+
Attack Surfaces
+
Trust Boundaries
+
Threats


Assets:

things we want
to protect.


Security goals:

Confidentiality
Integrity
Availability


Agentic systems
also strongly require:

Action Integrity
Authorization


Threat Actor:

entity capable
of causing harm.


Examples:

malicious user
external attacker
malicious document
compromised tool
compromised agent
insider


Attack Surface:

places an attacker
can influence
or interact with
the system.


Agent attack surfaces:

user prompt
RAG
memory
planner
tools
tool outputs
agent messages
runtime
model
network


Trust Boundary:

boundary between
different trust levels.


Important:

Trust boundary
does not require
a network boundary.


LLM output
→ Runtime

is a logical
trust boundary.


Tool output
=
untrusted observation.


Retrieved document
=
data,
not trusted instruction.


Agent output
=
untrusted input
to another agent.


STRIDE:

Spoofing
Tampering
Repudiation
Information Disclosure
Denial of Service
Elevation of Privilege


AI-specific threats:

prompt injection
jailbreak
RAG poisoning
memory poisoning
tool misuse
agent hijacking
model backdoor


Attack chain:

Source
↓
Propagation
↓
Sink


Defense in Depth:

multiple independent
security controls.


Threat Model
→ Security Requirements
→ Security Tests


Threat
!=
Risk


Risk depends on:

likelihood
impact


Least privilege
reduces potential damage.


LLM Safety
!=
System Security