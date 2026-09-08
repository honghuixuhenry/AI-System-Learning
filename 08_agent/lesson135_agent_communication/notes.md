Lesson 135
Agent Communication & Coordination


Multi-Agent communication
should use structured messages.


Message:

sender
receiver
message_id
message_type
task_id
payload


Message ID
identifies one message.

Task ID
groups messages
for one task.


Common message types:

TASK_REQUEST
TASK_RESULT
STATUS_UPDATE
ERROR
CANCEL
ACK
TASK_HANDOFF


Message Envelope:

routing/control metadata

Payload:

actual application data


Communication patterns:

direct messaging
request-response
publish/subscribe
broadcast
fan-out/fan-in


Message Bus:

decouples sender
from receiver implementation.


Message Bus
!=
Shared State

Message Bus:
communication

Shared State:
current system state


Message
!=
Memory


Task Handoff:

transfers responsibility
from one agent
to another.


Handoff should track:

old owner
new owner
task id
result
next instruction


ACK
!=
Task Complete


Distributed messaging
may have:

duplicates
loss
timeouts
retries


Side-effecting tasks
need idempotency.


At-least-once delivery
may cause duplicate execution.


Use:

idempotency keys
processed task IDs


Coordination problems:

deadlock
livelock
infinite handoffs
unbounded messaging


Use limits:

max messages
max handoffs
timeout
cost budget


Agent status may include:

IDLE
RUNNING
WAITING
FINISHED
FAILED


Task status may include:

PENDING
ASSIGNED
RUNNING
COMPLETED
FAILED


Heartbeat:

checks liveness.

Heartbeat
!=
progress.


Security:

Agent output
is not automatically trusted.

Validate:

sender
schema
message type
task
permissions
payload


Authentication
!=
Authorization


Separate:

data-plane messages

from

control-plane messages.


LLM-generated text
must not automatically
be treated as
trusted control commands.


Agent communication
is fundamentally
a distributed systems
and security problem.