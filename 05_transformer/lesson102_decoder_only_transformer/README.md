Lesson 102
Decoder-Only Transformer


Goal:

Build a complete modern
decoder-only language model.


Pipeline:

input_ids
(B,T)

↓ token embedding

(B,T,D)

↓ N Transformer Blocks

(B,T,D)

↓ final RMSNorm

(B,T,D)

↓ LM head

(B,T,V)


Transformer Block:

x
↓
RMSNorm
↓
GQA + RoPE + Causal Attention
↓
Residual
↓
RMSNorm
↓
SwiGLU
↓
Residual


Attention:

Q:
(B,Hq,T,d_h)

K:
(B,Hkv,T,d_h)

V:
(B,Hkv,T,d_h)


Output:

(B,T,D)


Language modeling logits:

(B,T,V)


Training target:

input:
tokens[:, :-1]

target:
tokens[:, 1:]


Cross entropy:

logits:
(B*T,V)

targets:
(B*T)


Important:

No softmax before
CrossEntropyLoss.


Weight tying:

token embedding weight
and LM head weight
may optionally be shared.