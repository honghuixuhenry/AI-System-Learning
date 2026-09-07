Lesson 106
LLM Pretraining Pipeline


Core Pipeline:

Raw Data
↓
Cleaning
↓
Filtering
↓
Deduplication
↓
Tokenization
↓
Token Stream
↓
Sequence Construction
↓
Batch
↓
Transformer
↓
Next-Token Loss
↓
Backward
↓
Optimizer
↓
Checkpoint


Raw Data != Training Data


Cleaning:
modify / normalize data

Filtering:
decide whether data should remain

Deduplication:
remove repeated or near-repeated content


Tokenizer:

Text
↓
Tokens
↓
Token IDs


Training shape:

input_ids:
(B,T)

logits:
(B,T,V)

targets:
(B,T)


Next-token objective:

P(
    x[t+1]
    |
    x[0:t]
)


Training example:

tokens:
A B C D E

input:
A B C D

target:
B C D E


LLM training memory:

Parameters
+
Gradients
+
Optimizer States
+
Activations
+
Temporary Buffers


Pretraining:

Large general corpus
↓
Base Model


Fine-tuning:

Base Model
+
Targeted Dataset
↓
Specialized Model


Important:

Tokenizer
must match
model vocabulary mapping.


LLM Engineering:

Model Architecture
+
Data Pipeline
+
Training System
+
Compute Infrastructure