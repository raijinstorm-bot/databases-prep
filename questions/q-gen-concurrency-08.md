---
id: "q-gen-concurrency-08"
exam: ""
number: 08
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["concurrency"]
---

Which isolation level prevents dirty reads and non-repeatable reads but still allows phantoms?

- a) READ UNCOMMITTED
- b) READ COMMITTED
- c) REPEATABLE READ
- d) SERIALIZABLE

### Explanation

According to the isolation-level table, REPEATABLE READ blocks dirty reads and non-repeatable reads but phantom records can still happen. READ COMMITTED still allows non-repeatable reads, and SERIALIZABLE blocks phantoms too.
