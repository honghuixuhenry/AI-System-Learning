Multi-Head Self-Attention

D = model dimension
H = number of heads
d_h = head dimension

D = H * d_h


Input:

X
(B,T,D)


Q/K/V projection:

(B,T,D)


Split heads:

(B,T,D)
→
(B,T,H,d_h)
→
(B,H,T,d_h)


Scores:

Q @ K^T

(B,H,T,d_h)
×
(B,H,d_h,T)

=

(B,H,T,T)


Scale:

scores / sqrt(d_h)


Softmax:

over Key dimension

dim = -1


Context:

weights @ V

(B,H,T,T)
×
(B,H,T,d_h)

=

(B,H,T,d_h)


Merge heads:

(B,H,T,d_h)
→
(B,T,H,d_h)
→
(B,T,D)


Output projection:

Linear(D,D)


Final:

(B,T,D)


Causal GPT attention:

Multi-Head
+
Causal Mask
+
Self-Attention