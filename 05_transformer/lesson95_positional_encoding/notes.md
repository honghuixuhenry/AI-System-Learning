Positional Information


Problem:

Self-Attention needs
sequence order information.


Token Embedding:

what token is this?


Position Embedding:

where is this token?


Learned position embedding:

nn.Embedding(
    max_seq_len,
    D
)


Position IDs:

0,1,2,...,T-1


Shapes:

token_ids:
(B,T)

token_embeddings:
(B,T,D)

position_ids:
(T,)

position_embeddings:
(T,D)


Combine:

x =
token_embeddings
+
position_embeddings


Result:

(B,T,D)


Learned Position:

trainable


Sinusoidal Position:

fixed mathematical encoding


Important:

Position mechanism
!= causal mask

Position:
where is this token?

Causal mask:
which tokens may it access?


Mini GPT:

Token IDs
↓
Token Embedding
+
Position Information
↓
Transformer Blocks
↓
Final Norm
↓
LM Head
↓
Logits
(B,T,V)