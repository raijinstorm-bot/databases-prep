---
id: "q-gen-concurrency-18"
exam: ""
number: 18
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b"]
pdfs: ["concurrency"]
---

Which practices does the presentation recommend to avoid deadlocks?

- a) Always lock resources in the same sequence across transactions
- b) For example, always lock the account with the lowest applicable number first, or always lock the account table before the customers table
- c) Always use the longest possible transactions to hold all locks at once
- d) Disable locking entirely

### Explanation

The slide advises issuing lock-acquiring statements in the same sequence in every transaction, giving examples such as locking the lowest account number first or the account table before the customers table. Long transactions worsen contention, and disabling locking is not a deadlock-avoidance strategy described.
