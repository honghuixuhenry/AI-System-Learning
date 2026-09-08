# Lesson 143
# Agent Authorization,
# Sandboxing & Least Privilege

Authentication:

Who are you?

Authorization:

What are you
allowed to do?

Capability:

What specific action
can you perform?

Sandboxing:

What can the execution
environment access?

Important:

Authentication
!=
Authorization

Authorization
!=
Sandboxing

Tool Availability
!=
Tool Permission

Model Proposal
!=
Execution Authority

Core principles:

- least privilege
- deny by default
- task-scoped authorization
- capability granularity
- deterministic policy
- credential separation
- bounded delegation
- action-bound approval
- sandboxed execution
- audit logging

Effective permission may depend on:

User
AND
Agent
AND
Task
AND
Resource
AND
Environment

Secrets should remain
in the runtime,
not in the model prompt.

A compromised model
should still have
limited authority.

Security should assume
model decisions can fail
and constrain the
resulting blast radius.