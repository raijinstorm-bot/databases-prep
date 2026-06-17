---
id: "q-gen-concurrency-14"
exam: ""
number: 14
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["b", "c"]
pdfs: ["concurrency"]
---

The presentation notes that locks in MS SQL Server are applied and released automatically. What further consequences does it describe?

- a) Locks typically cause hard errors that abort statements
- b) Locks typically do not cause errors, but may suspend statements from other transactions
- c) Locks are released when a transaction terminates with COMMIT or ROLLBACK
- d) Locks must always be requested explicitly by the application

### Explanation

The slides state locks are applied and released automatically, typically do not cause errors but may suspend other transactions' statements, and are released when the transaction ends via COMMIT or ROLLBACK. They are not applied manually by the application in the normal case.
