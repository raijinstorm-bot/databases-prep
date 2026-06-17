---
id: "q-gen-architecture-patterns-16"
exam: ""
number: 16
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["architecture-patterns"]
---

In transactional replication as described in the lecture, what are the roles of the log-reader agent and the distribution agent?

- a) The log-reader agent commits transactions; the distribution agent reads them
- b) The log-reader agent monitors changes via the transaction log and captures them into a distribution database; the distribution agent delivers the SQL INSERT/UPDATE/DELETE statements to the subscriber
- c) The distribution agent merges two databases; the log-reader agent rolls back failed transactions
- d) Both agents only operate on snapshots of full tables

### Explanation

The lecture states the log-reader agent monitors changes online through the transaction log and places them in a distribution database, while the distribution agent delivers the captured INSERT/UPDATE/DELETE statements to the subscriber periodically or online (b). The other options misassign these roles.
