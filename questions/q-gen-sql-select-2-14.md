---
id: "q-gen-sql-select-2-14"
exam: ""
number: 14
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["sql-select-2"]
---

According to the presentation, how should one test whether a column has no value?

- a) `WHERE Column_Name = NULL`
- b) `WHERE Column_Name IS NULL`
- c) `WHERE Column_Name == NULL`
- d) `WHERE NULL(Column_Name)`

### Explanation

The NULL slide gives the syntax `WHERE … Column_Name is [NOT] NULL …`. Equality comparisons against NULL do not work reliably, which is why the `IS NULL` form is required.
