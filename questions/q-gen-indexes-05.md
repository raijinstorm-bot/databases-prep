---
id: "q-gen-indexes-05"
exam: ""
number: 05
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["a"]
pdfs: ["indexes"]
---

If a table has no clustered index, how are its records stored?

- a) As a heap, with no specified order
- b) Sorted by the primary key automatically
- c) In a separate B-tree that orders all records
- d) Alphabetically by the first text column

### Explanation

Without a clustered index, records are stored as a heap with no specified order. This can make inserts and updates faster, since no order must be preserved. The other options describe ordered storage that a heap does not impose.
