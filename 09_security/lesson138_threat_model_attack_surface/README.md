# Lesson 138
# AI System Threat Model & Attack Surface

Threat modeling starts
before attack implementation.

Core questions:

1. What are we protecting?
2. Who can attack?
3. Where can attacks enter?
4. What trust boundaries exist?
5. What damage can occur?

Threat Model:

System
+ Assets
+ Threat Actors
+ Attack Surfaces
+ Trust Boundaries
+ Threats


Important AI/Agent surfaces:

- user input
- model
- planner
- RAG
- memory
- tools
- tool outputs
- agent messages
- runtime
- external services
- network

LLM safety
is not equivalent to
system security.

Threat models should
eventually drive
security test cases.