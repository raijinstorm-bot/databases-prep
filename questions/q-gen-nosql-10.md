---
id: "q-gen-nosql-10"
exam: ""
number: 10
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["nosql"]
---

In an aggregate-based database, how are ACID transactions typically handled according to the lecture?

- a) They can span any number of records from any number of tables, just like a relational OLTP system
- b) They are fully unsupported, even within a single aggregate
- c) The data of one aggregate is modified under ACID rules; spanning multiple aggregates must be handled by the client application
- d) They are guaranteed automatically across the entire cluster regardless of aggregate boundaries

### Explanation

The lecture states that one aggregate's data is modified under ACID rules, while transactions across multiple aggregates are not supported by the DBMS directly and must be handled by the client application (c). Spanning arbitrary tables (a) describes relational OLTP, not aggregate-based stores.
