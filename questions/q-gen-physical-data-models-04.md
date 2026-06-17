---
id: "q-gen-physical-data-models-04"
exam: ""
number: 04
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["physical-data-models"]
---

An INSERT statement can take a SELECT statement in place of the VALUES clause. Which condition must hold for this form to work?

- a) The SELECT must return exactly one row
- b) The SELECT must query the same table that is being inserted into
- c) The number and types of output columns must correspond to the table definition and the list of column names if used
- d) The SELECT must not contain a WHERE clause

### Explanation

When inserting from a SELECT, the number and types of the output columns must match the target table definition (and the column list, if given). It may insert as many rows as the query returns, can query other tables, and may include any WHERE clause.
