Lesson 137
Agent Capstone


Complete Agent System:

Agent Loop
+
Tools
+
Memory
+
Planning
+
RAG
+
Multi-Agent
+
Communication
+
Runtime


Agent:

proposes decisions.


Runtime:

controls execution.


Tool:

performs capability.


Environment:

produces observations.


Core loop:

Goal
↓
Plan
↓
Select Agent
↓
Retrieve / Tool
↓
Observation
↓
Update State
↓
Evaluate
↓
Continue / Finish


Task should be
structured runtime state.


Task fields:

task_id
description
assigned agent
dependencies
status
result


Task states:

pending
running
completed
failed


Shared Working Memory:

stores current
multi-agent task state.


RAG:

retrieves external evidence.


Tools:

perform actions
or deterministic operations.


Coordinator:

planning
routing
dependency management


Runtime:

execution
state transitions
budgets
failure handling
termination


Multi-Agent:

use specialization
only when useful.


More Agents
!=
Better System


Workflow:

predetermined control flow.


Agentic System:

control flow can change
based on observations.


Good architecture often uses:

Workflow
+
Agentic decision points


LLM should handle:

semantic uncertainty
planning
language generation


Deterministic code should handle:

validation
permissions
math
state transitions
budgets
schemas


Important:

LLM Decision
!=
Execution Permission


Tool Output
!=
Trusted Instruction


Agent Output
!=
Trusted Input


Runtime is a
security enforcement point.


Agentic AI
=
AI
+
Software Engineering
+
Distributed Systems
+
Security