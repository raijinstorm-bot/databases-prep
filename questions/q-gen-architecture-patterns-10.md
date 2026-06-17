---
id: "q-gen-architecture-patterns-10"
exam: ""
number: 10
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["architecture-patterns"]
---

According to the lecture, what protocol is typically used to coordinate a distributed transaction, and what are its phases?

- a) Three-phase locking: read, write, release
- b) Single-phase commit: immediate commit on all servers
- c) Two-phase commit: a prepare (voting) phase followed by a commit phase distributing the decision
- d) Snapshot isolation: capture then replay

### Explanation

The lecture states distributed transactions typically use the two-phase commit protocol, with a prepare phase in which all involved DBMS instances vote and a commit phase distributing the decision to apply or roll back (c). The other options misname the protocol or its phases.
