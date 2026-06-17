---
id: "q-gen-stored-procedures-11"
exam: ""
number: 11
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["stored-procedures"]
---

According to the lecture, if a single CRUD statement affects multiple records, how many times is an associated trigger activated?

- a) Once for every affected record
- b) Only once, for the whole group of affected records
- c) Twice: once before and once after the statement
- d) It depends on the number of columns modified

### Explanation

The lecture explicitly notes that when multiple records are affected by one CRUD statement, the trigger is activated only once, for the whole group of records (b). It is not fired per row or per column.
