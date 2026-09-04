Mini Language Model

Goal:
predict next token


Training pair:

current token
→
next token


Pipeline:

Text
→ Vocabulary
→ Token IDs
→ Dataset
→ Embedding
→ Hidden Layer
→ Vocabulary Logits
→ CrossEntropy


Shapes:

Input IDs:
(B,)

Embedding:
(B,D)

Logits:
(B,V)

Targets:
(B,)


Language modeling:
classification over vocabulary


Training:
raw logits
→ CrossEntropyLoss


Inference:
logits
→ argmax / softmax / sampling


Limitation:

Current model only sees
one current token.

It models approximately:

P(x_t+1 | x_t)

Real LLM:

P(x_t+1 | x_1 ... x_t)


Transformer:
uses sequence context.