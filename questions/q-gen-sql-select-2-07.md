---
id: "q-gen-sql-select-2-07"
exam: ""
number: 07
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["sql-select-2"]
---

According to the GROUP BY interpretation slides, what is obtained **first** when answering a GROUP BY query (after applying WHERE)?

- a) The aggregate values for the largest group
- b) The unique list of values of the grouping column(s)
- c) The final sorted result set
- d) A Cartesian product of the table with itself

### Explanation

The step-I interpretation slide states that to answer a query with GROUP BY, a unique list of column values is retrieved (e.g. the unique list of CUSTOMER_ID), and then aggregates are computed per group.
