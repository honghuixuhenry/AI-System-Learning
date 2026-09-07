Lesson 108
Tokenization, Packing & Training Sequences


Pipeline:

Clean Documents
↓
Tokenizer
↓
Token IDs
↓
EOS
↓
Packing
↓
T+1 Chunk
↓
Input / Target
↓
Batch


Tokenizer:

Text
→ Token IDs


Embedding:

Token IDs
→ Vectors


Important:

Tokenizer != Embedding


Document Boundary:

Document A
<eos>
Document B
<eos>


EOS token
does NOT automatically
block cross-document attention.


Padding:

short sequence
+
PAD tokens
→ fixed length


Packing:

multiple documents
→ token stream
→ fixed-length sequences


Goal:

higher token utilization


Training sample:

Raw:
A B C D E

Input:
A B C D

Target:
B C D E


Therefore:

T+1 raw tokens
→ T predictions


Shapes:

single input:
(T,)

single target:
(T,)

batch input:
(B,T)

batch target:
(B,T)

logits:
(B,T,V)


Masks:

Causal Mask
→ blocks future

Padding Attention Mask
→ blocks padding from attention

Loss Mask
→ excludes positions from loss


Important:

Document
!=
Training Sequence
!=
Batch


Sequence Length:

larger T
→ longer context
→ more compute/memory

Dense attention:
roughly quadratic in T


Token Budget:

tokens per step
≈
B × T

with gradient accumulation:
micro_batch × T × accumulation_steps

with data parallel:
also multiply across workers
for global token batch


Large-scale training often tracks:

tokens seen
steps
global batch size

rather than only epochs.