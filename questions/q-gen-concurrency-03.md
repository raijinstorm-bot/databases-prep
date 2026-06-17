---
id: "q-gen-concurrency-03"
exam: ""
number: 03
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["concurrency"]
---

According to the presentation, a phantom is best described as:

- a) A row whose value changes between two reads in the same transaction
- b) A new row that matches the search criteria but was not initially seen
- c) A modification overwritten by another transaction
- d) An uncommitted row read by another transaction

### Explanation

A phantom is a row that matches the search criteria but is not initially seen: if transaction 2 inserts a matching row and transaction 1 re-runs the query, it gets a different set of rows. The other descriptions correspond to non-repeatable reads, lost updates, and dirty reads respectively.
