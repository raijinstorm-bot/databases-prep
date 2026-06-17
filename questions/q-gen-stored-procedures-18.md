---
id: "q-gen-stored-procedures-18"
exam: ""
number: 18
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["stored-procedures"]
---

The lecture explains how stored procedures can be faster than equivalent ad hoc statements. What mechanism does it cite?

- a) They bypass the DBMS and run directly on the operating system
- b) They automatically create indexes on all referenced tables
- c) The DBMS can maintain a cached execution plan for the whole SP, compiled and analysed beforehand
- d) They convert all SELECT statements into materialised views

### Explanation

The lecture states an SP can take advantage of an execution plan: the DBMS caches the best predicted method of accessing data for the entire SP, compiled and analysed beforehand (c). It does not bypass the DBMS, auto-create indexes, or build materialised views.
