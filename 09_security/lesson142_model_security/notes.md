Lesson 142

Model Security


Model Supply Chain:

Training Data
↓
Training
↓
Checkpoint
↓
Fine-Tuning
↓
Adapter
↓
Quantization
↓
Repository
↓
Deployment


Backdoor:

hidden conditional
model behavior.


Trigger
↓
unexpected behavior


Training Poisoning:

corrupt training
or fine-tuning data.


Poisoning
!=
Backdoor


Adversarial Input:

crafted inference input
causes failure.


Backdoor:
compromised model

Adversarial:
crafted input


Prompt Injection:
context trust problem

Backdoor:
model integrity problem


RAG Poisoning:
runtime knowledge changes

Training Poisoning:
learned parameters change


Model artifacts:

weights
tokenizer
config
chat template
adapter
runtime


Weights Alone
!=
Complete Behavior


Integrity:

hash
signature
version
source


Hash
!=
Trust


LoRA / Adapter
can significantly
change behavior.


Quantized Model
is a new artifact.


Model repository
is part of
software supply chain.


Other model risks:

Model Theft
Model Extraction
Membership Inference
Model Inversion
Resource Abuse


Security evaluation:

Clean Performance
+
Attack Performance


Backdoor metrics:

Clean Accuracy
Attack Success Rate


Layered evaluation:

Model
↓
Runtime
↓
System


Model Compromise
!=
System Compromise


Trusted Model
!=
Authorization Authority


Core principle:

Assume model
can be wrong.

Limit what
wrong decisions
can do.