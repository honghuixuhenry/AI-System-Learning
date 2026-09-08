# Lesson 142
# Model Security:
# Backdoors, Adversarial Inputs
# & Model Attacks

Model Security protects:

- model weights
- checkpoints
- tokenizer
- configuration
- adapters
- training data
- model repositories
- inference runtime

Backdoor:

hidden conditional model behavior
activated by a trigger.

Training Poisoning:

manipulation of training
or fine-tuning data.

Adversarial Input:

crafted inference-time input
that induces model failure.

Model Theft:

unauthorized extraction
of model capability or weights.

Important distinctions:

Backdoor
!=
Training Poisoning

Backdoor
!=
Adversarial Input

Backdoor
!=
Jailbreak

Training Poisoning
!=
RAG Poisoning

Model Artifact Integrity:

verify:
source
version
hash
signature
configuration

Hash verifies integrity
relative to a trusted reference.

Hash alone does not
establish trust.

Important principle:

Model Compromise
!=
Automatic System Compromise

Runtime authorization,
least privilege,
sandboxing,
and deterministic validation
can limit damage.