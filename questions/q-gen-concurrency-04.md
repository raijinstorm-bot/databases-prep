---
id: "q-gen-concurrency-04"
exam: ""
number: 04
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["d"]
pdfs: ["concurrency"]
---

A lost update anomaly occurs when:

- a) A transaction reads uncommitted data that is later rolled back
- b) A new row appears between two reads of the same query
- c) A single row returns different values on two reads
- d) Modifications made by one transaction are overwritten by another transaction unaware of those changes

### Explanation

Lost updates occur when more than one transaction reads the same data and the modifications made by one are overwritten by another that was unaware of the earlier change. The other options describe dirty reads, phantoms, and non-repeatable reads.
