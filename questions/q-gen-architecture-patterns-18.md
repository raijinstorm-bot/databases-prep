---
id: "q-gen-architecture-patterns-18"
exam: ""
number: 18
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b"]
pdfs: ["architecture-patterns"]
---

How does the lecture distinguish snapshot replication from merge replication?

- a) Snapshot replication periodically replaces the subscriber's table content with new content without tracking individual changes
- b) Merge replication periodically merges the content of two different databases
- c) Snapshot replication transmits complete SQL statements for each individual change
- d) Merge replication is used only to publish a read-only price list from headquarters

### Explanation

The lecture describes snapshot replication as periodically replacing subscriber table content without tracking individual changes (a), and merge replication as periodically merging two databases, e.g. central customers with mobile reps' data (b). Transmitting complete SQL statements per change is transactional replication (c), and the price-list publication example is snapshot, not merge (d).
