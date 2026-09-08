Lesson 131
Agent Memory Systems


Important distinction:

Context
!=
Working Memory
!=
Long-Term Memory
!=
RAG


Context:

information provided
to the LLM
for the current inference.


Conversation Memory:

interaction history.


Working Memory:

current task state.


Long-Term Memory:

persistent information
across tasks/sessions.


Core memory pipeline:

Store
↓
Retrieve
↓
Inject into Context
↓
LLM


Memory is usually managed
by the Agent Runtime,
not magically stored
inside the LLM.


Memory Store
!=
Context Builder


RAG:

retrieves external knowledge
to augment generation.


Memory:

stores agent/user/task
state or experience.


Vector database
is a storage/retrieval
technology.

It is not itself
agent memory.


Memory types can include:

conversation
working
semantic
episodic
procedural


Important memory metadata:

source
created_at
updated_at
expires_at
importance
confidence


Similarity
!=
Relevance


Memory retrieval
is a ranking problem.


Memory write requires policy.

Not every observation
should become
long-term memory.


Untrusted observation
must not automatically
become trusted memory.


Memory poisoning
is an important
agent security risk.


Memory systems also require:

privacy
access control
retention
deletion
provenance


Memory lifecycle:

create
retrieve
update
expire/delete


Long conversations
should not necessarily
be placed entirely
into the context.


Common design:

summary
+
recent messages
+
relevant long-term memory
+
current task


Agent memory
is fundamentally
a state-management system.