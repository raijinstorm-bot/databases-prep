---
id: "q-gen-concurrency-17"
exam: ""
number: 17
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "c"]
pdfs: ["concurrency"]
---

According to the presentation, what defines a deadlock and how is it resolved?

- a) A combination of locks that prevents more than one transaction from executing
- b) A situation that the DBMS can always resolve without terminating any transaction
- c) It cannot be resolved without terminating (rolling back) one of the transactions
- d) It is automatically prevented by using READ UNCOMMITTED

### Explanation

A deadlock is a combination of locks blocking more than one transaction that cannot be resolved without terminating (ROLLBACK) one of them, which cancels its updates and should be avoided. It is not always resolvable without termination, and isolation level alone (e.g. READ UNCOMMITTED) does not prevent it.
