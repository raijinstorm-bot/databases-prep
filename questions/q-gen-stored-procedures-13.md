---
id: "q-gen-stored-procedures-13"
exam: ""
number: 13
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b", "c"]
pdfs: ["stored-procedures"]
---

Based on the "Triggers - remarks" slide, which statements about triggers are correct?

- a) Trigger capabilities may depend on the SQL implementation
- b) On some DBMS platforms, triggers can be defined for views as well as tables
- c) A trigger can change the content of another or even the same table, potentially causing the DBMS to fire other triggers
- d) Triggers are guaranteed to behave identically across every DBMS platform

### Explanation

The lecture states trigger capabilities depend on the implementation (a), some platforms allow triggers on views (b), and a trigger modifying tables can cause other triggers to fire (c). Identical cross-platform behavior is contradicted by a, making d false.
