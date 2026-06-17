---
id: "q-gen-indexes-04"
exam: ""
number: 04
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["indexes"]
---

What does defining a clustered index on a table cause?

- a) The DBMS creates an extra B-tree but leaves the table records in arbitrary order
- b) The table's columns are split into two separate tables
- c) The DBMS physically stores the table records in the specified order
- d) All other indexes on the table are automatically dropped

### Explanation

A clustered index makes the DBMS physically store the table records in the specified order (e.g. growing OrderId). It does not leave records arbitrary, split columns, or drop other indexes.
