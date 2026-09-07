import torch


x = torch.randn(
    4,
    4
)


x_fp32 = x.to(
    torch.float32
)

x_fp16 = x.to(
    torch.float16
)

x_bf16 = x.to(
    torch.bfloat16
)


print(
    x_fp32.dtype
)

print(
    x_fp16.dtype
)

print(
    x_bf16.dtype
)