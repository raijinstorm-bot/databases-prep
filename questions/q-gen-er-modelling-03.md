---
id: "q-gen-er-modelling-03"
exam: ""
number: 03
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["er-modelling"]
---

To enforce entity integrity, what structure is typically created automatically by the DBMS together with the primary key?

- a) A foreign key
- b) A trigger that logs all changes
- c) A unique index (a tree-like structure for quickly checking existing PK values)
- d) A separate audit table

### Explanation

The presentation explains that typically a unique index — a tree-like structure used to quickly check which primary key values already exist — is automatically created by the DBMS. The DBMS then monitors create and update operations to reject duplicate primary key values.
