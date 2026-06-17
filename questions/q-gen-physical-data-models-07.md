---
id: "q-gen-physical-data-models-07"
exam: ""
number: 07
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "c"]
pdfs: ["physical-data-models"]
---

Which statements about UPDATE and DELETE are correct according to the presentation?

- a) Referential integrity may cause some UPDATE or DELETE statements to fail
- b) Aliases for tables affected by UPDATE/DELETE are supported identically on every DBMS
- c) The value assigned in an UPDATE can be defined through an expression or even an embedded SELECT query
- d) DELETE can only remove a single record at a time

### Explanation

Referential integrity can make UPDATE/DELETE fail (a), and UPDATE values can come from expressions or embedded SELECTs (c). Alias support differs by vendor — allowed in Oracle but not MS SQL Server — and DELETE can remove many rows, so (b) and (d) are false.
