Token IDs
(B,T)
↓
Embedding
(B,T,D)
↓
[Norm → Attention → Residual]
↓
[Norm → FFN → Residual]
↓
repeat N times
↓
Final Norm
↓
Linear(D,V)
↓
Logits
(B,T,V)