---
id: "q-gen-indexes-15"
exam: ""
number: 15
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["indexes"]
---

What is the fundamental reason an index improves the performance of an SQL statement?

- a) It compresses the SQL text so the parser runs faster
- b) It decreases the number of disk blocks that must be read to execute the statement
- c) It moves the table entirely into CPU registers
- d) It rewrites the query to avoid using the WHERE clause

### Explanation

The true advantage of an index comes from decreasing the number of disk blocks that must be read: the DBMS reads the small index structure plus some records, instead of scanning the whole table. The other options misdescribe how indexes work.
