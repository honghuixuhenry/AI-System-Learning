from dataclasses import dataclass


@dataclass
class TrainingConfig:

    vocab_size: int = 256

    sequence_length: int = 32

    batch_size: int = 8

    d_model: int = 128

    num_heads: int = 4

    num_layers: int = 2

    learning_rate: float = 3e-4

    weight_decay: float = 0.1

    warmup_steps: int = 100

    max_steps: int = 1000

    gradient_accumulation_steps: int = 4

    max_grad_norm: float = 1.0

    checkpoint_interval: int = 100