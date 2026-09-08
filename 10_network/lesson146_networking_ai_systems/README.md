# Lesson 146
# Computer Networking for AI Systems

Modern AI systems are often
distributed systems.

Example:

Agent
→ LLM Server
→ RAG Server
→ Tool Server
→ Memory Service

Simplified network stack:

Application
→ Transport
→ Network
→ Link

Application:

HTTP
HTTPS
gRPC
WebSocket

Transport:

TCP
UDP
QUIC

Network:

IPv4
IPv6

Link:

Ethernet
Wi-Fi

Important concepts:

IP identifies a host/interface.

Port identifies a service endpoint.

Application Message
!=
Network Packet

Latency
!=
Bandwidth

Streaming
!=
Faster Model Computation

Local LLM
!=
No Networking

Distributed AI performance
depends on:

Compute
+
Communication

Agentic systems may amplify
network cost because one task
can require many remote calls.