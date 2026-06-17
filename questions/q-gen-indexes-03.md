---
id: "q-gen-indexes-03"
exam: ""
number: 03
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["indexes"]
---

How many clustered indexes can a single table have?

- a) Exactly zero
- b) At most one
- c) Exactly one for every column
- d) Unlimited, like nonclustered indexes

### Explanation

There can be at most one clustered index per table, because the entire table records are physically stored in that order. A table may also have zero clustered indexes (then it is a heap), so "exactly zero" and the other options are wrong.
