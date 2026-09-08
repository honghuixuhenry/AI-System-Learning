# Lesson 140
# Tool-Use & Function-Calling Security

LLM tool calls are proposals,
not execution authority.

Core principle:

Tool Selection
!=
Authorization

Valid JSON
!=
Safe Action

Tool Security Pipeline:

LLM Proposal
→ Tool Validation
→ Argument Validation
→ Agent Authorization
→ Task Authorization
→ Semantic Policy
→ User Confirmation
→ Execution
→ Result Handling

Important defenses:

- least privilege
- narrow capabilities
- task-scoped permissions
- deterministic validation
- argument bounds
- user confirmation
- idempotency
- sandboxing
- audit logging

Important distinctions:

Discovery
!=
Authorization

Schema Validity
!=
Semantic Authorization

Tool Output
!=
Trusted Instruction

Agent Permission
!=
Task Permission

Model-Level Attack Success
!=
System-Level Attack Success

Side-effecting tools require
stronger controls than
read-only tools.