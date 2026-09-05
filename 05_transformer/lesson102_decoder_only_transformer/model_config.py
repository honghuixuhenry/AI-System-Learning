from dataclasses import dataclass


@dataclass
class ModelConfig:

    vocab_size: int = 10000

    dim: int = 512

    num_layers: int = 8

    num_q_heads: int = 8

    num_kv_heads: int = 2

    hidden_dim: int = 1360

    max_seq_len: int = 2048

    rope_base: float = 10000.0

    rms_eps: float = 1e-6