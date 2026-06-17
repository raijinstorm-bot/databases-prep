---
id: "q-gen-indexes-07"
exam: ""
number: 07
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b", "c"]
pdfs: ["indexes"]
---

Which statements about nonclustered indexes are correct?

- a) A single table can have many nonclustered indexes
- b) Every nonclustered index has a separate structure requiring its own extra space on disk
- c) A nonclustered index can be created on a heap or on a clustered table
- d) A nonclustered index determines the physical storage order of the entire table

### Explanation

A table can have many nonclustered indexes (a), each in its own on-disk structure (b), and they can be created on a heap or on a clustered table (c). Determining the table's physical storage order is the role of a clustered index, so (d) is false.
