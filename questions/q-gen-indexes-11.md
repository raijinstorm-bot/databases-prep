---
id: "q-gen-indexes-11"
exam: ""
number: 11
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["indexes"]
---

Why does a unique index help the DBMS enforce uniqueness of a key efficiently?

- a) It deletes any duplicate rows automatically without checking
- b) It converts the table into a heap to avoid conflicts
- c) While updating the index, the DBMS can easily determine if another record already has the same key value
- d) It disables all other indexes during the check

### Explanation

With a unique index, the DBMS can quickly determine whether a conflicting key value already exists while updating the index, instead of scanning the whole table. It does not silently delete rows, convert to a heap, or disable other indexes.
