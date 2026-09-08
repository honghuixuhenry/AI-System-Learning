# Lesson 144
# Agentic AI Security Testing
# & Benchmark Design

Traditional LLM benchmark:

Input
→ Model
→ Output
→ Judge

Agentic security benchmark:

Attack
→ Model
→ Plan
→ Tool Proposal
→ Runtime
→ Memory
→ External Action
→ Evaluation

Core principle:

Evaluate the system,
not only the final response.

A benchmark case should include:

Attack Source
Attack Category
Target Layer
Task
Security Property
Expected System Behavior

Important metrics:

Attack Success Rate
Unauthorized Tool Proposal Rate
Unauthorized Action Rate
Poison Retrieval Rate
Memory Contamination Rate
Benign Task Success Rate

Important distinctions:

Model Manipulation
!=
System Compromise

Attack Prevention
!=
Attack Containment

Attack Payload
!=
Benchmark Case

Semantic Similarity
!=
Security Evaluation

Prefer deterministic evaluation
for observable system events.

Use LLM judges only when
semantic evaluation is needed.

Security benchmarks should
include both attack cases
and benign cases.