---
id: "q-gen-indexes-06"
exam: ""
number: 06
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["indexes"]
---

In MS SQL Server, which type of index does `CREATE INDEX` create by default if neither CLUSTERED nor NONCLUSTERED is specified?

- a) A clustered index
- b) A unique index
- c) A nonclustered index
- d) A heap

### Explanation

By default a NONCLUSTERED index is created. CLUSTERED must be requested explicitly; uniqueness requires the UNIQUE keyword; a heap is the absence of a clustered index, not something CREATE INDEX produces.
