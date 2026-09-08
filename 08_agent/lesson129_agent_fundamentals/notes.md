Lesson 129
AI Agent Fundamentals
& Agent Loop


LLM application:

Prompt
↓
LLM
↓
Response


Agent:

Goal
↓
Observe
↓
Reason
↓
Act
↓
Observe
↓
Repeat


Agent:

LLM
+
State
+
Tools
+
Environment
+
Control Loop


Core concepts:

Goal

State

Action

Observation

Environment

Agent Loop


Agent state stores:

goal
history
observations
actions
progress
completion state


Agent loop:

while not finished:

    observe
    reason
    choose action
    execute
    update state


Important:

Agent
does not necessarily
require an LLM.

Decision logic can be:

rules
search
RL
LLM


LLM Agent:

uses LLM
as the decision /
reasoning component.


Workflow:

predetermined
control flow.


Agent:

dynamic
control flow.


Agent autonomy
is a spectrum.


Important safety principle:

LLM decision
!=
execution permission


Agent runtime should include:

max steps
timeout
budget
permissions
logging
termination rules


Agent Runtime
!=
LLM Serving Runtime


Stack:

Application
↓
Agent Runtime
↓
LLM + Tools
↓
Serving Engine
↓
Hardware