Lesson 133
RAG & External Knowledge


RAG:

Retrieval
+
Augmentation
+
Generation


Pipeline:

Query
↓
Retriever
↓
Relevant Chunks
↓
Ranking
↓
Context Builder
↓
LLM
↓
Answer


Important:

LLM Knowledge
!=
Agent Memory
!=
External Knowledge


Document
!=
Chunk


Chunking helps:

reduce context size
improve retrieval precision


Chunk size trade-off:

small chunks
→ precise but less context

large chunks
→ more context but more noise


Retriever can use:

keywords
BM25
embeddings
SQL
metadata
graph search
hybrid search


RAG
does not require
a vector database.


Vector DB:

storage/index/search
for vectors.


Similarity
!=
Relevance


Retrieval and reranking
can be separate stages.


More retrieved context
does not always improve
answer quality.


Context Builder decides
what the LLM actually sees.


RAG allows knowledge
to update without
retraining the model.


RAG does not eliminate
hallucinations.


Important failure types:

retrieval failure

generation failure


Support abstention:

if evidence is absent,
do not invent an answer.


RAG may use:

query rewriting
query expansion
multi-hop retrieval


Agentic RAG:

Reason
↓
Retrieve
↓
Observe
↓
Retrieve/Act Again


RAG can be exposed
as an agent tool.


Security:

retrieved content
must be treated
as untrusted data.


Risks include:

indirect prompt injection
knowledge poisoning
unauthorized retrieval
stale knowledge
false provenance


Authorization should occur
before sensitive knowledge
is exposed to the model.


Useful metadata:

source
date
version
authority
section


Citation is useful
for provenance and audit.


Offline pipeline:

documents
↓
clean
↓
chunk
↓
embed
↓
index


Online pipeline:

query
↓
retrieve
↓
rank
↓
context
↓
generate


Fine-Tuning:

changes model parameters.


RAG:

changes inference context.