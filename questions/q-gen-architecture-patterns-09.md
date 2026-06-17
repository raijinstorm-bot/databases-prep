---
id: "q-gen-architecture-patterns-09"
exam: ""
number: 09
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["architecture-patterns"]
---

The lecture notes a subtle case in which even a transaction touching two databases on the same server is still a distributed transaction. Why?

- a) Because the server has more than one CPU
- b) Because each database has its own private transaction log
- c) Because the two databases use different SQL dialects
- d) Because the server runs both an active and a passive node

### Explanation

The lecture states that if every database has its own private transaction log, then even a transaction affecting two databases on the same server requires a distributed transaction (b). The reasoning is about separate logs, not CPUs, dialects, or clustering.
