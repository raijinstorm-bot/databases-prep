---
id: "q-gen-architecture-patterns-14"
exam: ""
number: 14
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "c"]
pdfs: ["architecture-patterns"]
---

The lecture compares distributed transactions and replication as data-synchronisation methods. Which statements are correct?

- a) Distributed transactions are the only method that guarantees on-line consistency of participating databases
- b) Replication updates all participating servers at exactly the same instant with no latency
- c) Replication accepts latency, so the system may still accept user input even if one server does not respond
- d) Distributed transactions continue processing normally even when one server is unavailable

### Explanation

The lecture states distributed transactions are the only method guaranteeing on-line consistency (a) but stop processing when any server is unavailable, contradicting d. Replication accepts latency and lets the system accept input despite an unresponsive server (c), which contradicts the no-latency claim in b.
