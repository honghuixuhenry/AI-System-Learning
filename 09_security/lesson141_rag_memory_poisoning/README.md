# Lesson 141
# RAG, Memory & Data Poisoning Attacks

RAG Poisoning:

attacker manipulates
external knowledge used
during retrieval.

Memory Poisoning:

attacker manipulates
persistent agent state.

Indirect Prompt Injection:

untrusted external content
is interpreted as instruction.

Important:

RAG Poisoning
!=
Memory Poisoning
!=
Indirect Prompt Injection

A poisoned document
does not need to contain
an instruction.

False information itself
can poison knowledge.

Core security principles:

Retrieved
!=
Trusted

Remembered
!=
Authorized

Similarity
!=
Credibility

Provenance
!=
Truth

Memory Write
is a privileged
state mutation.

Important defenses:

- provenance
- source validation
- access control
- trust-aware retrieval
- freshness/version checks
- conflict resolution
- controlled memory writes
- memory namespaces
- TTL
- verification
- least privilege
- auditability

Security evaluation should
measure propagation,
not only attack entry.