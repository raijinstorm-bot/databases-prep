---
id: "q-gen-concurrency-07"
exam: ""
number: 07
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["concurrency"]
---

Under the READ COMMITTED isolation level in MS SQL Server, which anomalies are still possible?

- a) None of the anomalies are possible
- b) Dirty reads only
- c) Non-repeatable reads and phantoms
- d) Dirty reads, non-repeatable reads and phantoms

### Explanation

READ COMMITTED prevents dirty reads (only committed results are seen) but still allows non-repeatable reads and phantoms, since other transactions can commit during execution. It does not block all anomalies, and dirty reads are specifically prevented.
