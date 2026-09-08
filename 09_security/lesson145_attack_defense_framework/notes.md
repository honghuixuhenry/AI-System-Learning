Lesson 145

AI Security Capstone


Threat Model
↓
Security Invariants
↓
Attack Library
↓
Benchmark
↓
SUT
↓
Defense Stack
↓
Execution Trace
↓
Evaluator
↓
Metrics


Attack:

Source
↓
Propagation
↓
Sink


Prevention:

stop attack
before propagation.


Containment:

limit impact
after manipulation.


Defense in Depth:

multiple independent
security controls.


Security Invariant:

property that
must always hold.


Property-Centric Testing:

multiple attacks
against same invariant.


Layered Metrics:

ASR_model
ASR_plan
ASR_tool
ASR_system


Security
+
Utility


Benchmark needs:

benign cases
attack cases
repeatability
versioning
traces
replay


Security Regression:

model update
tool update
policy update
runtime update
↓
rerun benchmark


Important:

Model output
is untrusted proposal.

Retrieved
!=
Trusted

Remembered
!=
Authorized

Available
!=
Permitted

Proposed
!=
Executable

Information
!=
Authority


Goal:

A component
may fail

without causing
system compromise.