---
id: "q-gen-indexes-16"
exam: ""
number: 16
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["indexes"]
---

When should a clustered index be considered, according to the guidelines?

- a) When you rarely access the table's records
- b) When the column has only a few distinct values
- c) When you frequently access groups of related records (e.g. multiple lines of one order)
- d) When you want to avoid keeping any data in sorted order

### Explanation

A clustered index is worth considering when you frequently access groups of related records, because they will be stored in the same part of the disk and read together. The other situations do not motivate a clustered index.
