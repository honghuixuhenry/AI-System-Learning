Lesson 147

TCP HTTP RPC API


Socket:

OS/application
network interface.


TCP:

reliable ordered
byte stream.


TCP does not preserve
application message boundaries.


HTTP:

request
+
response


HTTP message:

method
path
headers
body


API:

service interface.


REST:

resource-oriented
API style.


RPC:

call remote service
like a procedure.


Remote Call
!=
Local Call


Remote call includes:

serialization
network
queue
execution
response


gRPC:

RPC framework

often uses:

Protocol Buffers
HTTP/2


REST/JSON:

simple
readable
widely compatible


RPC/Protobuf:

typed
compact
good for many
internal services


Streaming
!=
WebSocket


Streaming options:

HTTP streaming
SSE
WebSocket
gRPC streaming


Timeout
Retry
Backoff
Idempotency


Retry
can duplicate
side effects.


Side-effecting Agent tools:

use:

tool_call_id
idempotency_key
deduplication


API Gateway:

authentication
routing
rate limiting
logging


Load Balancer:

distribute traffic.


API Schema
=
Communication Contract


Control Plane
!=
Data Plane