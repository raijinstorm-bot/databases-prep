---
id: "q-gen-physical-data-models-03"
exam: ""
number: 03
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["physical-data-models"]
---

When an INSERT statement is executed without listing all column names and provides values for only some columns, what happens to the remaining columns?

- a) The statement is always rejected by the DBMS
- b) Default values such as NULL are attempted to be placed in the remaining columns
- c) The remaining columns are dropped from the table
- d) The previous record's values are copied into them

### Explanation

When only some columns are supplied, the DBMS attempts to place default values such as NULL in the remaining columns. The statement is not automatically rejected, columns are not dropped, and no prior record is copied.
