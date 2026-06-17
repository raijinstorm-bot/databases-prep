---
id: "q-gen-concurrency-11"
exam: ""
number: 11
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["concurrency"]
---

In MS SQL Server, a Shared lock is used for which kind of operation?

- a) INSERT, UPDATE and DELETE
- b) Read operations that do not change data, i.e. SQL SELECT
- c) DDL statements that modify a table
- d) Compiling and executing queries on a table structure

### Explanation

A Shared lock is used for read operations that do not change data, i.e. SELECT, and during it no other transaction can modify the data. Exclusive locks cover INSERT/UPDATE/DELETE, while schema modification and schema stability locks cover DDL and query compilation respectively.
