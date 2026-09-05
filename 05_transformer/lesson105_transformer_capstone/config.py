from dataclasses import dataclass


@dataclass
class ModelConfig:

    vocab_size: int

    dim: int = 128

    num_layers: int = 4

    num_q_heads: int = 8

    num_kv_heads: int = 2

    hidden_dim: int = 352

    max_seq_len: int = 64

    rope_base: float = 10000.0

    rms_eps: float = 1e-6


@dataclass
class TrainingConfig:

    batch_size: int = 8

    learning_rate: float = 3e-4

    epochs: int = 20

    weight_decay: float = 0.01