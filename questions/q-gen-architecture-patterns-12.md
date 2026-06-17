---
id: "q-gen-architecture-patterns-12"
exam: ""
number: 12
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b"]
pdfs: ["architecture-patterns"]
---

The lecture warns of problems a distributed transaction must address. Which of the following are explicitly mentioned?

- a) Some participating DBMSs may be unavailable
- b) Some DBMSs may reject the requested changes, e.g. due to a constraint violation
- c) The two-phase commit protocol always finishes in a single network round-trip
- d) Distributed transactions remove the need for ACID guarantees

### Explanation

The lecture lists unavailable participating DBMSs (a) and DBMSs rejecting changes, e.g. constraint violations (b), as problems to address. The protocol involves significant overhead (not a single round-trip), and executing a DT means ensuring ACID, so c and d are false.
