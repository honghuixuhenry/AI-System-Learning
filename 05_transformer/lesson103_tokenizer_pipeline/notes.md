Tokenizer Pipeline


Raw text
↓
Tokenizer
↓
Tokens
↓
Vocabulary lookup
↓
Token IDs


Tokenizer:

Text ↔ Token IDs


Embedding:

Token IDs
→ learned vectors


Important:

Tokenizer != Embedding


Vocabulary size:

V

Embedding weight:
(V,D)

LM head output:
(B,T,V)


Special tokens:

PAD
BOS
EOS
UNK


BOS:

beginning of sequence


EOS:

end of sequence


Padding:

used to make variable-length
sequences into a dense batch.


input_ids:

(B,T)


attention_mask:

(B,T)

1:
valid token

0:
padding


Causal mask:

blocks future tokens.


Padding mask:

blocks padded positions.


Loss mask:

controls which target positions
contribute to cross entropy.


They solve different problems.


Training:

tokens:
(B,T+1)

input:
tokens[:, :-1]

target:
tokens[:, 1:]


Model:

(B,T)
→
(B,T,D)
→
(B,T,V)


Cross entropy:

(B*T,V)
vs
(B*T)


Inference:

Prompt Text
↓
Tokenizer
↓
Token IDs
↓
Prefill
↓
KV Cache
↓
Decode
↓
next token ID
↓
Tokenizer decode
↓
Text


Tokenizer affects:

sequence length
context usage
attention compute
KV cache
serving cost