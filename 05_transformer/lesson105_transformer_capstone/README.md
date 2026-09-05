COMPLETE LANGUAGE MODEL PIPELINE


RAW TEXT

"I love AI"

        ↓

TOKENIZER

tokens
        ↓
token IDs

(B,T)

        ↓

TOKEN EMBEDDING

(B,T,D)

        ↓

TRANSFORMER BLOCK × L

RMSNorm
        ↓
Q / K / V

Q:
(B,Hq,T,d_h)

K/V:
(B,Hkv,T,d_h)

        ↓
RoPE

        ↓
Causal GQA Attention

        ↓
(B,T,D)

        ↓
Residual

        ↓
RMSNorm

        ↓
SwiGLU

        ↓
Residual

        ↓

FINAL RMSNorm

(B,T,D)

        ↓

LM HEAD

(B,T,V)

        ↓

TRAINING:

CrossEntropy
↓
Backward
↓
Optimizer


INFERENCE:

last-token logits
↓
temperature
↓
top-k / top-p
↓
softmax
↓
sampling
↓
next token
↓
repeat