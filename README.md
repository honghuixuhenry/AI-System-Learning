# AI System Learning

A hands-on learning repository for building a systematic understanding of modern AI systems, from Python programming and software engineering to PyTorch, Transformers, large language model training and inference, AI agents, AI security, networking, and distributed AI systems.

This repository documents a **150-lesson AI System Engineering learning journey**. The goal is not only to learn how to train or use an AI model, but to understand how a complete AI system is designed, implemented, deployed, secured, communicated, and evaluated.

The overall philosophy of this repository is:

> **An AI system is much more than a model.**

A production AI system may include:

- Software architecture
- Model training
- Model inference
- API servers
- Agent runtimes
- Retrieval-Augmented Generation (RAG)
- Memory systems
- Tool execution
- Authorization and policy enforcement
- Networking
- Distributed computing
- Observability
- Security testing

The repository progresses from basic programming foundations to an end-to-end secure AI system.

---

# Repository Structure

```text
AI-System-Learning/
├── 01_python
├── 02_data_structure_algo
├── 03_software_design
├── 04_pytorch
├── 05_transformer
├── 06_llm
├── 07_inference
├── 08_agent
├── 09_security
├── 10_network
├── LICENSE
└── README.md
```

The learning path follows this progression:

```text
Python
   ↓
Data Structures & Algorithms
   ↓
Software & System Engineering
   ↓
PyTorch
   ↓
Transformer
   ↓
LLM Training
   ↓
LLM Inference
   ↓
AI Agent Systems
   ↓
AI / Agentic Security
   ↓
Networking & Distributed AI
   ↓
End-to-End Secure AI System
```

---

# Learning Roadmap

The repository contains **150 lessons** organized into ten major modules.

```text
Lessons 1–50
Python + Data Structures + Software Foundations

Lessons 51–75
Mini AI Server + Software/System Engineering

Lessons 76–90
PyTorch

Lessons 91–105
Transformer

Lessons 106–117
LLM Training

Lessons 118–128
LLM Inference Systems

Lessons 129–137
AI Agent Systems

Lessons 138–145
AI / Agentic System Security

Lessons 146–150
Networking & Distributed AI Systems
```

---

# 01 — Python Foundations

The first module builds the programming foundation required for AI and system engineering.

Topics include:

- Python syntax
- Variables and data types
- Functions
- Lists, tuples, dictionaries, and sets
- File operations
- Exceptions
- Object-oriented programming
- Classes and inheritance
- Iterators
- Generators
- Decorators
- Context managers
- Type hints
- Dataclasses
- Enums
- Multithreading
- Multiprocessing
- Concurrency concepts

The purpose of this module is not simply to learn Python syntax, but to develop the programming skills required to build larger AI systems.

---

# 02 — Data Structures and Algorithms

This module develops the algorithmic foundations needed for software systems, AI infrastructure, graph-based systems, scheduling, search, and optimization.

Topics include:

- Stacks
- Queues
- Priority queues
- Linked structures
- Trees
- Binary trees
- Graphs
- Breadth-First Search
- Depth-First Search
- Shortest paths
- Dijkstra's algorithm
- Tries
- Union-Find
- Backtracking
- Permutations
- Graph traversal and path finding

These concepts later appear naturally in:

- Agent planning
- Search systems
- Routing
- Scheduling
- Task queues
- Retrieval
- Distributed systems

---

# 03 — Software Design and AI Server Engineering

This module transitions from programming to **system engineering**.

It introduces software architecture and gradually builds a Mini AI Server.

Major topics include:

- Software architecture
- Project organization
- Python packages
- Interfaces
- Dependency management
- SOLID principles
- Unit testing
- Debugging
- Factory Pattern
- Strategy Pattern
- Service Layer
- Dependency Injection
- Configuration
- Logging
- Caching
- Task queues
- Futures
- Async programming
- Rate limiting
- Backpressure
- Retry
- Exponential backoff
- Circuit breakers
- Observability
- Application lifecycle
- API security
- Environment variables
- Secrets
- Persistence
- SQLite
- Docker

The networking portion begins with:

- Socket programming
- TCP
- HTTP
- REST APIs
- FastAPI
- Pydantic

The module culminates in a:

## Mini AI Server Capstone

A simplified architecture such as:

```text
Client
   ↓
FastAPI
   ↓
Route Layer
   ↓
Service Layer
   ↓
Task Queue
   ↓
Worker
   ↓
LLM Interface
```

with supporting components for:

```text
Configuration
Logging
Caching
Rate Limiting
Retry
Persistence
Authentication
Testing
Containerization
```

This module establishes the software architecture foundation used by later AI systems.

---

# 04 — PyTorch

The PyTorch module introduces deep learning implementation from a system-oriented perspective.

Topics include:

- Tensors
- Tensor shapes
- Tensor operations
- Automatic differentiation
- Computational graphs
- `nn.Module`
- Linear layers
- Activation functions
- Loss functions
- Cross-entropy
- Optimizers
- SGD
- Adam
- AdamW
- Dataset
- DataLoader
- Training loops
- Validation loops
- Checkpoints
- Regularization
- Dropout
- Batch normalization
- Layer normalization
- Weight initialization
- Gradient clipping
- Device management
- CPU
- CUDA
- MPS
- FP32
- FP16
- BF16
- Mixed precision
- Embeddings
- Residual connections

The main mental model is:

```text
Data
 ↓
Model
 ↓
Forward
 ↓
Loss
 ↓
Backward
 ↓
Gradients
 ↓
Optimizer
 ↓
Updated Parameters
```

---

# 05 — Transformer

This module builds the Transformer architecture from fundamental components.

Topics include:

- Token embeddings
- Query, Key, and Value
- Self-attention
- Scaled dot-product attention
- Causal masks
- Padding masks
- Multi-head attention
- Feed-forward networks
- Residual connections
- Pre-Norm architecture
- Positional embeddings
- Sinusoidal position encoding
- Rotary Position Embedding
- RMSNorm
- SwiGLU
- Grouped Query Attention
- Multi-Query Attention
- KV Cache
- Scaled Dot Product Attention
- FlashAttention concepts
- Decoder-only Transformers
- Tokenization
- Language modeling
- Autoregressive generation
- Temperature
- Top-k sampling
- Top-p sampling

The modern Transformer capstone combines:

```text
Token Embedding
      ↓
RoPE
      ↓
GQA
      ↓
SDPA
      ↓
Residual
      ↓
RMSNorm
      ↓
SwiGLU
      ↓
Residual
      ↓
Transformer Blocks
      ↓
Language Model Head
```

---

# 06 — LLM Training

This module moves from individual Transformer components to the complete large language model training pipeline.

## Lesson 106
LLM Pretraining Pipeline

## Lesson 107
Large-Scale Text Dataset & Data Cleaning

## Lesson 108
Tokenization, Packing & Training Sequences

## Lesson 109
Pretraining Objective & Causal Language Modeling

## Lesson 110
Training Loop, Gradient Accumulation & Effective Batch Size

## Lesson 111
Learning Rate Scheduler & Warmup

## Lesson 112
Mixed Precision & Training Stability

## Lesson 113
Distributed Training Fundamentals

## Lesson 114
Data Parallelism, DDP & FSDP

## Lesson 115
Tensor Parallelism & Pipeline Parallelism

## Lesson 116
Fine-Tuning, LoRA & Parameter-Efficient Fine-Tuning

## Lesson 117
LLM Training Capstone: From Dataset to Checkpoint

The complete training pipeline can be summarized as:

```text
Raw Text
   ↓
Data Cleaning
   ↓
Tokenizer
   ↓
Token IDs
   ↓
Sequence Packing
   ↓
Mini-Batches
   ↓
Transformer
   ↓
Causal Language Modeling Loss
   ↓
Backward
   ↓
Distributed Gradient Computation
   ↓
Optimizer
   ↓
Checkpoint
```

---

# 07 — LLM Inference Systems

Training creates a model.

Inference turns that model into a usable AI service.

This module studies the systems problems behind efficient LLM inference.

## Lesson 118
LLM Inference Pipeline: Prefill & Decode

## Lesson 119
KV Cache Implementation

## Lesson 120
KV Cache Memory & Paged Attention

## Lesson 121
Batching & Continuous Batching

## Lesson 122
Quantization: FP16, INT8 & INT4

## Lesson 123
Inference Performance: Latency, Throughput & TTFT

## Lesson 124
GPU Memory & LLM Memory Estimation

## Lesson 125
LLM Serving Architecture

## Lesson 126
vLLM, SGLang & Modern Serving Engines

## Lesson 127
TensorRT-LLM, llama.cpp & Hardware-Specific Inference

## Lesson 128
LLM Inference Capstone: Build a Mini LLM Server

A modern inference architecture can be viewed as:

```text
Client
   ↓
API Server
   ↓
Request Queue
   ↓
Scheduler
   ↓
Continuous Batching
   ↓
Model Worker
   ↓
GPU
   ↓
KV Cache
   ↓
Streaming Output
```

Important performance concepts include:

```text
TTFT
Time to First Token

ITL
Inter-Token Latency

TPS
Tokens per Second

Throughput
Requests / Tokens per unit time

Goodput
Useful work satisfying service objectives
```

---

# 08 — AI Agent Systems

This module moves from a passive language model to an **AI Agent Runtime**.

A simplified agent architecture is:

```text
User
 ↓
Agent Runtime
 ↓
LLM
 ↓
Decision
 ↓
Tool / Memory / RAG
 ↓
Observation
 ↓
LLM
 ↓
Next Decision
```

The central concept is:

> An LLM generates decisions, while the Agent Runtime controls execution.

## Lesson 129
AI Agent Fundamentals & Agent Loop

## Lesson 130
Tool Calling & Function Calling

## Lesson 131
Agent Memory Systems

## Lesson 132
Planning & Reasoning Loops

## Lesson 133
RAG & External Knowledge

## Lesson 134
Multi-Agent Systems

## Lesson 135
Agent Communication & Coordination

## Lesson 136
Agent Runtime Architecture & MCP-Style Tool Systems

## Lesson 137
Agent Capstone: Build a Complete Agent System

The complete agent architecture is:

```text
                Agent Runtime
                      │
         ┌────────────┼────────────┐
         ▼            ▼            ▼
        LLM          RAG         Memory
         │
         ▼
      Planner
         │
         ▼
    Tool Proposal
         │
         ▼
    Tool Runtime
         │
         ▼
    Environment
```

Important distinctions include:

```text
LLM
!=
Agent

Agent
!=
Agent Runtime

Tool Selection
!=
Authorization

Memory
!=
KV Cache

RAG
!=
Long-Term Memory
```

---

# 09 — AI and Agentic System Security

This module studies security at the **AI system level**, rather than treating AI security as only a model problem.

The core security principle is:

> **Model output is a proposal, not execution authority.**

## Lesson 138
AI System Threat Model & Attack Surface

## Lesson 139
Prompt Injection & Jailbreak Attacks

## Lesson 140
Tool-Use & Function-Calling Security

## Lesson 141
RAG, Memory & Data Poisoning Attacks

## Lesson 142
Model Security: Backdoors, Adversarial Inputs & Model Attacks

## Lesson 143
Agent Authorization, Sandboxing & Least Privilege

## Lesson 144
Agentic AI Security Testing & Benchmark Design

## Lesson 145
AI Security Capstone: Attack–Defense Evaluation Framework

The security analysis follows the general chain:

```text
Attack Source
      ↓
Entry Point
      ↓
Propagation
      ↓
AI / Agent Decision
      ↓
Runtime
      ↓
Security Enforcement
      ↓
External Impact
```

Important attack surfaces include:

```text
User Input
RAG Documents
Memory
Tool Results
Agent Messages
Model Artifacts
Network
Runtime
External Services
```

The secure tool execution pipeline is:

```text
LLM Proposal
      ↓
Tool Validation
      ↓
Argument Validation
      ↓
Authentication
      ↓
Authorization
      ↓
Task Scope
      ↓
Optional User Confirmation
      ↓
Sandbox
      ↓
Execution
      ↓
Audit
```

Important security principles include:

```text
Retrieved
!=
Trusted

Remembered
!=
Authorized

Tool Available
!=
Tool Permitted

Authentication
!=
Authorization

Valid JSON
!=
Safe Action

Model Manipulation
!=
System Compromise

Information
!=
Authority
```

---

# 10 — Networking and Distributed AI Systems

The final module connects AI systems to the communication infrastructure on which they depend.

## Lesson 146
Computer Networking for AI Systems

Topics include:

- Application layer
- Transport layer
- TCP
- UDP
- QUIC
- IP
- Ethernet
- Wi-Fi
- IP addresses
- Ports
- Endpoints
- DNS
- NAT
- Firewalls
- MTU
- Latency
- Bandwidth
- Throughput
- Serialization

A simplified stack:

```text
AI Application
      ↓
HTTP / RPC
      ↓
TCP / QUIC
      ↓
IP
      ↓
Ethernet / Wi-Fi
```

## Lesson 147
TCP, HTTP, RPC & API Communication

Important distinctions:

```text
Socket
!=
TCP

TCP
!=
HTTP

HTTP
!=
REST

REST
!=
RPC

RPC
!=
API
```

Topics include:

- Socket communication
- HTTP request/response
- REST
- RPC
- gRPC
- Protocol Buffers
- HTTP streaming
- WebSocket
- API Gateway
- Load balancing
- Service discovery
- API versioning
- Timeouts
- Retries
- Idempotency

## Lesson 148
Distributed AI Communication & Collective Operations

Topics include:

- Rank
- World size
- Point-to-point communication
- Collective communication
- Broadcast
- Reduce
- All-Reduce
- Gather
- All-Gather
- Scatter
- Reduce-Scatter
- Ring All-Reduce
- Communication cost
- Compute-communication overlap
- Network topology
- NCCL
- Stragglers

Communication patterns across parallelism:

| Parallelism | Main Communication |
|---|---|
| Data Parallel / DDP | Gradient All-Reduce |
| FSDP | All-Gather + Reduce-Scatter |
| Tensor Parallel | Tensor collectives |
| Pipeline Parallel | Point-to-point activations |

## Lesson 149
Network Performance & Communication Security

Topics include:

- Latency
- Bandwidth
- Throughput
- Jitter
- Packet loss
- Tail latency
- TLS
- Authentication
- Authorization
- Eavesdropping
- Tampering
- Spoofing
- Man-in-the-Middle attacks
- Replay attacks
- Replay protection
- Rate limiting
- Resource exhaustion
- Secure Agent communication

A secure API boundary looks like:

```text
Secure Channel
      ↓
Authentication
      ↓
Replay Protection
      ↓
Schema Validation
      ↓
Authorization
      ↓
Rate Limiting
      ↓
Execution
      ↓
Audit
```

## Lesson 150
Final Capstone: End-to-End Secure AI System

The final lesson integrates the entire repository.

```text
                           Client
                              │
                              ▼
                       API Gateway
                              │
                              ▼
                       Agent Runtime
                              │
           ┌──────────────────┼──────────────────┐
           │                  │                  │
           ▼                  ▼                  ▼
      LLM Service       Knowledge Service    Tool Runtime
                              │                  │
                          RAG / Memory       Policy Engine
                                                 │
                                                 ▼
                                          External Services

                              │
                              ▼
                        Observability
                              │
                              ▼
                     Security Evaluation
```

The major responsibilities are separated clearly:

```text
LLM
→ semantic intelligence

Agent Runtime
→ control and orchestration

Policy Engine
→ authorization

Tool Runtime
→ external execution

RAG / Memory
→ external and persistent knowledge

Network
→ communication

Observability
→ system visibility

Security Benchmark
→ invariant verification
```

---

# Final System Mental Model

The complete learning journey leads to the following system view:

```text
User
 │
 ▼
Secure Network
 │
 ▼
API Gateway
 │
 ▼
Agent Runtime
 │
 ├───────────────┬───────────────┐
 │               │               │
 ▼               ▼               ▼
LLM             RAG            Memory
 │
 ▼
Planning
 │
 ▼
Tool Proposal
 │
 ▼
Policy Engine
 │
 ▼
Tool Runtime
 │
 ▼
External Environment

        │
        ├── Observability
        │
        ├── Security Testing
        │
        └── Distributed Communication
```

---

# Core Engineering Principles

Several principles appear repeatedly throughout the repository.

### 1. A Model Is Not an AI System

```text
Model
+
Runtime
+
Data
+
Tools
+
Network
+
Security
=
AI System
```

### 2. Remote Calls Are Not Local Calls

Remote services introduce:

```text
Latency
Timeout
Failure
Retry
Serialization
Authentication
Authorization
Partial Failure
```

### 3. Distributed AI Is Compute + Communication

```text
Distributed AI Performance
=
Compute Performance
+
Memory Performance
+
Communication Performance
```

### 4. LLM Output Is Not Authority

```text
LLM
→ proposes

Runtime
→ validates

Policy
→ authorizes

Tool Runtime
→ executes
```

### 5. Security Must Be Enforced Outside the Model

Models are probabilistic.

Security properties should be enforced by deterministic and auditable system controls whenever possible.

### 6. Defense in Depth

No single security mechanism is sufficient.

```text
Authentication
+
Authorization
+
Validation
+
Least Privilege
+
Sandboxing
+
Secure Communication
+
Rate Limiting
+
Observability
+
Security Testing
```

### 7. Security and Utility Must Be Evaluated Together

A system that blocks every action may be secure but useless.

Therefore, evaluation should consider both:

```text
Security
+
Task Utility
```

---

# Important Security Invariants

Examples of security properties that an AI system may enforce:

```text
Unauthenticated users
must not access the Agent Runtime.
```

```text
A research task
must not execute email.send.
```

```text
Untrusted retrieved documents
must not grant permissions.
```

```text
Model output
must not bypass runtime authorization.
```

```text
Unverified external information
must not automatically become
trusted persistent memory.
```

```text
Repeated side-effecting requests
must not cause duplicate execution.
```

```text
Security-relevant actions
must generate auditable events.
```

Security testing attempts to violate these invariants while measuring whether the system successfully prevents or contains the attack.

---

# Security Evaluation Model

The repository develops the following evaluation methodology:

```text
Threat Model
      ↓
Attack Library
      ↓
Benchmark Dataset
      ↓
System Under Test
      ↓
Execution Trace
      ↓
Security Evaluator
      ↓
Metrics
      ↓
Attack–Defense Comparison
```

Possible metrics include:

```text
Attack Success Rate

Model Manipulation Rate

Unauthorized Tool Proposal Rate

Unauthorized Action Rate

Memory Contamination Rate

Poison Retrieval Rate

Benign Task Success Rate
```

A particularly important distinction is:

```text
Model-level attack success
does not necessarily imply
system-level compromise.
```

For example:

```text
Model Manipulated:
YES

Unauthorized Tool Proposed:
YES

Runtime Authorization:
DENY

Unauthorized Tool Executed:
NO
```

This represents successful **containment** even though model-level manipulation occurred.

---

# Performance Mental Model

AI system latency can be approximated conceptually as:

```text
Total Latency

=
Network Latency
+
Queue Latency
+
Serialization
+
Model Inference
+
Tool Execution
+
Runtime Overhead
```

For Agent systems:

```text
Task Latency

≈

Sum of multiple:

LLM calls
+
Tool calls
+
RAG calls
+
Agent communication
+
Network round trips
```

Therefore:

> A faster model does not automatically create a faster AI system.

---

# Distributed AI Mental Model

Large AI systems may communicate at two very different levels.

## Service-Level Communication

```text
Agent Runtime
     ↓
HTTP / RPC
     ↓
LLM Server
```

## GPU-Level Communication

```text
GPU 0
 ↕
GPU 1
 ↕
GPU 2
 ↕
GPU 3
```

using operations such as:

```text
All-Reduce
All-Gather
Reduce-Scatter
Broadcast
Point-to-Point Communication
```

These two communication layers should not be confused.

---

# How to Use This Repository

Each lesson typically contains:

```text
Python implementation
Conceptual examples
Architecture diagrams
README
Notes
Exercises / homework
```

A recommended learning workflow is:

```text
1. Read the lesson concepts

2. Write the code manually

3. Run and debug the implementation

4. Modify the examples

5. Complete the homework

6. Write key concepts into notes.md

7. Connect the lesson to previous modules
```

The repository is designed for active coding rather than passive reading.

---

# Recommended Development Environment

The examples are primarily designed for Python.

A typical setup can include:

```text
Python 3
VS Code
Git
GitHub
PyTorch
FastAPI
pytest
```

Later lessons may additionally involve tools and frameworks such as:

```text
Docker

Hugging Face Transformers

vLLM

SGLang

TensorRT-LLM

llama.cpp

PyTorch Distributed
```

Not every framework is required to complete the conceptual exercises.

---

# Learning Philosophy

This repository emphasizes understanding systems from the inside out.

Rather than only learning:

```text
How do I call an LLM API?
```

the goal is to understand:

```text
How is the model trained?

How does inference work?

How is KV cache managed?

How does an inference scheduler work?

How does an Agent call tools?

Where should authorization happen?

How can RAG or memory be poisoned?

How do multiple agents communicate?

How do GPUs communicate?

Where does network latency appear?

How do attacks propagate through the system?

How can system-level defenses contain model failures?
```

The long-term objective is to develop the ability to reason about an AI system as a complete computational system.

---

# Final Takeaway

The entire repository can be summarized by the following architecture:

```text
                     AI SYSTEM

                        User
                         │
                         ▼
                  Secure Network
                         │
                         ▼
                    API Layer
                         │
                         ▼
                  Agent Runtime
                  /     |      \
                 /      |       \
                ▼       ▼        ▼
              LLM      RAG      Tools
                │       │         │
                └───────┼─────────┘
                        │
                        ▼
                   Policy Engine
                        │
                        ▼
                  External World

                        │
             ┌──────────┴──────────┐
             ▼                     ▼
       Observability        Security Testing
```

The key principles are:

```text
LLM
!=
AI System

LLM
!=
Agent

Agent
!=
Runtime

Retrieved
!=
Trusted

Remembered
!=
Authorized

Authenticated
!=
Authorized

Tool Available
!=
Tool Permitted

Model Proposal
!=
Execution Authority

Model Manipulation
!=
System Compromise

Information
!=
Authority
```

The ultimate engineering goal is:

> **Build AI systems in which individual components can fail, behave incorrectly, or even be manipulated without automatically causing system-level compromise.**

---

# Progress

```text
150 / 150 Lessons Completed
```

Modules completed:

```text
✓ Python

✓ Data Structures & Algorithms

✓ Software & System Engineering

✓ Mini AI Server

✓ PyTorch

✓ Transformer

✓ LLM Training

✓ LLM Inference

✓ AI Agent Systems

✓ AI / Agentic Security

✓ Networking & Distributed AI

✓ End-to-End Secure AI System
```

---

# License

See the `LICENSE` file for license information.
