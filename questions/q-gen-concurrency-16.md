---
id: "q-gen-concurrency-16"
exam: ""
number: 16
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["concurrency"]
---

In Example 4, Session #1 reads the same row twice under REPEATABLE READ while Session #2 tries to UPDATE that row. What is the outcome?

- a) Session #1 experiences a non-repeatable read
- b) Session #2 proceeds immediately and commits
- c) Session #2 is suspended, so non-repeatable reads are not possible in Session #1
- d) Both sessions are rolled back due to deadlock

### Explanation

Under REPEATABLE READ, the row read by Session #1 is protected, so Session #2's UPDATE is suspended until Session #1 finishes; this prevents non-repeatable reads. Contrast with Example 3, where READ COMMITTED allowed the update and thus the anomaly.
