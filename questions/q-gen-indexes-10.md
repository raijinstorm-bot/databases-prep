---
id: "q-gen-indexes-10"
exam: ""
number: 10
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["indexes"]
---

What is a negative impact of creating indexes on a table?

- a) They prevent the table from being queried with SELECT
- b) They can increase the time needed to complete INSERT/UPDATE/DELETE statements
- c) They make primary keys impossible to define
- d) They permanently corrupt the heap structure

### Explanation

Because the DBMS must keep index trees consistent with table content, CRUD statements can become slower and may require many index trees to be rebuilt. Indexes do not block SELECTs, prevent primary keys, or corrupt anything.
