Lesson 109
Pretraining Objective
& Causal Language Modeling


Objective:

P(
    x_t
    |
    x_<t
)


Training:

raw:
A B C D E

input:
A B C D

target:
B C D E


Shifted Target:
defines what to predict.

Causal Mask:
defines what information
each position may use.


Model:

input_ids
(B,T)

↓

logits
(B,T,V)


CrossEntropy:

reshape:

(B,T,V)
→
(B*T,V)

(B,T)
→
(B*T)


Loss:

L =
average negative log probability
of the correct next token.


CrossEntropy
expects raw logits.

Do NOT softmax first.


Per-token loss:

L_i =
-log p(correct token)


Average loss:

L =
1/N Σ L_i


Perplexity:

PPL = exp(L)


Important:

Perplexity comparisons
depend on compatible
tokenizer / dataset /
evaluation protocol.


Self-Supervised:

labels are generated
from the text itself.


Teacher Forcing:

training uses
ground-truth previous tokens.


Training:
parallel across T

Generation:
sequential autoregressive


Loss:
measures error

Backward:
computes gradients

Optimizer:
updates parameters


Padding / ignored labels:

ignore_index = -100


Validation:

use token-weighted average
when batches contain different
numbers of valid tokens.