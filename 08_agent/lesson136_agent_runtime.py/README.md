# Lesson 136
# Agent Runtime Architecture & MCP-Style Tool Systems

This lesson integrates
previous agent components
into an agent runtime.

Agent Runtime:

Agent Loop
+ Tools
+ Memory
+ Planning
+ RAG
+ Communication


Core architecture:

Agent
→ Runtime
→ Tool Client
→ Tool Provider


Important distinctions:

Agent
!=
Runtime

Agent Runtime
!=
LLM Serving Runtime

Function Calling
!=
External Tool Integration


Function Calling:

LLM proposes a
structured tool invocation.


Tool Integration:

Runtime discovers,
connects to,
and invokes capabilities.


MCP-style architecture:

Host
→ Client
→ Server
→ Tools / Resources


Server
!=
Tool

Client
!=
Agent

Host
!=
LLM


Important runtime responsibilities:

tool discovery
schema validation
authorization
routing
execution
memory/state updates
timeouts
budgets
observability
resource lifecycle