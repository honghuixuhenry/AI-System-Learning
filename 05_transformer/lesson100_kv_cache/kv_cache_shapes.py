B = 1

NUM_Q_HEADS = 8
NUM_KV_HEADS = 2

HEAD_DIM = 16

CACHE_LEN = 100


q_new_shape = (
    B,
    NUM_Q_HEADS,
    1,
    HEAD_DIM
)


k_cache_shape = (
    B,
    NUM_KV_HEADS,
    CACHE_LEN,
    HEAD_DIM
)


v_cache_shape = (
    B,
    NUM_KV_HEADS,
    CACHE_LEN,
    HEAD_DIM
)


print(
    "Q new:",
    q_new_shape
)

print(
    "K cache:",
    k_cache_shape
)

print(
    "V cache:",
    v_cache_shape
)