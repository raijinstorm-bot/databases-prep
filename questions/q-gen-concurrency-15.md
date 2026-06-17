---
id: "q-gen-concurrency-15"
exam: ""
number: 15
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["concurrency"]
---

In Example 1, Session #1 runs an UPDATE under READ COMMITTED while Session #2 runs a SELECT under READ UNCOMMITTED on the same row. What happens to Session #2?

- a) Session #2 is suspended until Session #1 completes
- b) Session #2 is not suspended, and dirty reads are possible since Session #1 may be cancelled
- c) Session #2 raises a deadlock error
- d) Session #2 sees only the committed data and never any anomaly

### Explanation

Because Session #2 uses READ UNCOMMITTED, it is not suspended and can read the uncommitted change; if Session #1 later rolls back, this becomes a dirty read. There is no deadlock, and the low isolation level explicitly allows the anomaly.
