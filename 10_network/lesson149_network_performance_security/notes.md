Lesson 149

Network Performance
&
Communication Security


Performance:

Latency
Bandwidth
Throughput
Jitter
Packet Loss
Availability


Bandwidth:

capacity


Throughput:

actual useful rate


Tail latency:

P95
P99


Network threats:

Eavesdropping
Tampering
Spoofing
MITM
Replay
DoS


TLS:

Confidentiality
Integrity
Authentication


TLS
!=
Authorization


Authentication:

who?


Authorization:

what action?


Replay:

reuse valid message


Idempotency:

avoid duplicate
side effect


Rate Limiting:

requests
tokens
concurrency
resources


Secure Pipeline:

TLS
↓
Authenticate
↓
Replay Check
↓
Validate
↓
Authorize
↓
Rate Limit
↓
Execute
↓
Audit


Authenticated
!=
Trusted


Secure Channel
!=
Secure Application


Performance telemetry
can also support
security monitoring.