import torch


batch = 2
heads = 4
cached_length = 10
head_dim = 32


k_cache = torch.randn(
    batch,
    heads,
    cached_length,
    head_dim
)

v_cache = torch.randn(
    batch,
    heads,
    cached_length,
    head_dim
)


q_new = torch.randn(
    batch,
    heads,
    1,
    head_dim
)

k_new = torch.randn(
    batch,
    heads,
    1,
    head_dim
)

v_new = torch.randn(
    batch,
    heads,
    1,
    head_dim
)


k_all = torch.cat(
    [k_cache, k_new],
    dim=2
)

v_all = torch.cat(
    [v_cache, v_new],
    dim=2
)


print("Q:", q_new.shape)
print("K:", k_all.shape)
print("V:", v_all.shape)