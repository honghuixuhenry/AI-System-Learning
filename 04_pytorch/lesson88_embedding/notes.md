Embedding

Text
→ Tokens
→ Token IDs
→ Embedding Vectors


Vocabulary:

token
↔
integer ID


Token ID:

integer index

dtype:
torch.long


Embedding:

nn.Embedding(
    vocab_size,
    embedding_dim
)


Embedding matrix:

(V, D)


Input:

(B, T)

Output:

(B, T, D)


Embedding is:

trainable parameter
+
lookup table


Important:

Token ID
!= semantic value

Embedding vector
= learned representation


Padding:

padding_idx


Transformer input:

Token Embedding
+
Position Information


Tokenizer
!=
Embedding


Tokenizer vocabulary
must match
model vocabulary.