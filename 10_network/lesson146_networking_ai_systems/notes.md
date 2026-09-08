Lesson 146

Computer Networking
for AI Systems


AI systems are often
distributed.


Agent
↓
HTTP / RPC
↓
TCP / QUIC
↓
IP
↓
Ethernet / Wi-Fi
↓
Server


IP:

where is the host?


Port:

which service?


Endpoint:

protocol
host
port
path


TCP:

reliable ordered
byte stream.


UDP:

lighter transport
without TCP semantics.


Application Message
!=
Packet


Bandwidth:

how much data
per second?


Latency:

how long?


Transfer time:

data size
/
bandwidth


AI latency:

network
+
queue
+
compute
+
serialization


Streaming:

earlier delivery

not necessarily
faster generation.


Distributed Training:

Compute
+
Communication


Scale-Up:

inside server


Scale-Out:

between servers


Agent Systems:

multiple network calls
may amplify latency.


Security:

bind address
ports
firewall
authentication
TLS


0.0.0.0
!=
localhost