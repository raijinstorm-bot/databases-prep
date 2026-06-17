---
id: "q-gen-concurrency-12"
exam: ""
number: 12
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["concurrency"]
---

Under the default isolation level, what does an Exclusive lock (used for INSERT, UPDATE, DELETE) prevent?

- a) Only it prevents other transactions from reading, but allows modification
- b) Nothing; exclusive locks are advisory only
- c) Other transactions can neither modify nor (by default) read the locked data
- d) Only DDL statements on the table

### Explanation

The slide states an exclusive lock prevents other transactions from modifying the locked data, and under the default isolation level it also prevents them from reading data locked in exclusive mode. So both reads and writes by others are blocked.
