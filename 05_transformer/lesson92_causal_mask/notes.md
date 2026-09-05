Causal Attention Mask

Goal:

prevent a token from
attending to future tokens.


For T = 4:

1 0 0 0
1 1 0 0
1 1 1 0
1 1 1 1


Causal mask:

shape = (T,T)


Attention scores:

shape = (B,T,T)


Apply:

future score
→ -inf


Then:

softmax(-inf)
→ 0


Correct order:

QK^T
→ scale
→ mask
→ softmax
→ weighted sum


Causal Mask:

blocks future


Padding Mask:

blocks padding tokens


Loss Mask:

blocks selected positions
from CrossEntropy


Important:

padding_idx
does not replace
padding attention mask.


Training:

whole sequence can be
processed in parallel
with causal masking.


Generation:

still autoregressive
one token at a time.