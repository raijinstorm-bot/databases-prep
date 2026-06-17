---
id: "q-gen-indexes-14"
exam: ""
number: 14
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["indexes"]
---

Why does the presentation recommend creating an index on the columns of a foreign key?

- a) Foreign keys cannot be defined without an index
- b) It physically stores the child table in the order of the parent key
- c) Otherwise, removing or modifying a parent key value, and every JOIN, would require scanning the child table
- d) It guarantees the foreign key values are unique

### Explanation

Without an index on a foreign key, every deletion/modification of a referenced parent key, and every JOIN, would require scanning the child table. Indexing the foreign key speeds up referential integrity checking and joins. It does not enforce uniqueness or change physical storage of the child.
