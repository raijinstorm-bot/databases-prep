---
id: "q-gen-concurrency-19"
exam: ""
number: 19
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["concurrency"]
---

What does `ROLLBACK TRAN B` do when `B` is a savepoint created with `SAVE TRAN B`?

- a) It rolls back the entire transaction and releases all locks
- b) It rolls back only the changes executed after `SAVE TRAN B`, not the entire transaction
- c) It commits the changes up to the savepoint
- d) It creates a new nested transaction named B

### Explanation

A savepoint placed with `SAVE TRAN B` acts as a label; `ROLLBACK TRAN B` undoes only the changes made after that savepoint, not the whole transaction, so locks acquired earlier are kept. It does not commit anything or start a new transaction.
