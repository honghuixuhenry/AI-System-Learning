Lesson 141

RAG, Memory
& Data Poisoning


RAG Poisoning:

manipulates
external knowledge.


Memory Poisoning:

manipulates
persistent agent state.


Indirect Prompt Injection:

untrusted data
is interpreted
as instruction.


Poisoning
does not require
instruction text.


RAG attack surface:

source
ingestion
chunking
metadata
index
retrieval
ranking
context


Similarity
!=
Truth

Similarity
!=
Trust


Secure retrieval needs:

provenance
authorization
trust
freshness
conflict resolution


Memory:

Store
Retrieve
Inject


Memory Write
=
Privileged State Mutation


LLM believes something
!=
Memory write authorized


Raw tool/RAG output
should not automatically
become long-term memory.


Memory security:

write policy
read policy
namespace
TTL
versioning
verification
audit
recovery


Persistent poisoning:

attack once
→ influence future sessions


Cross-agent poisoning:

Agent A
→ Shared Memory
→ Agent B


Provenance
should follow
data propagation.


Provenance
!=
Truth


Important metrics:

Poison Retrieval Rate
Poison Influence Rate
Memory Contamination Rate
Persistent Influence Rate
Unauthorized Action Rate


Core principle:

Information
!=
Authority