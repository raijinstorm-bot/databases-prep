---
id: "q-gen-sql-select-15"
exam: ""
number: 15
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["sql-select"]
---

According to the presentation's two-step interpretation of a multi-table query, what is created **first**?

- a) The filtered result set satisfying the WHERE condition
- b) An index linking the two tables
- c) A Cartesian product of all combinations of records from the tables
- d) A temporary view of the joined data

### Explanation

The query-interpretation slides state that to answer a query referring to multiple tables, a Cartesian product (all possible combinations of records) is created first, and only afterwards is it filtered by the join condition.
