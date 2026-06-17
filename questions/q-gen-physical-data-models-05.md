---
id: "q-gen-physical-data-models-05"
exam: ""
number: 05
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["physical-data-models"]
---

In a relational database, how is exactly one record selected for an UPDATE statement to modify?

- a) By referring to its physical position ("this" record) in the table
- b) By a condition referring to the value of a primary key
- c) By the order in which records were inserted
- d) By selecting the first record returned by the table scan

### Explanation

Relational databases have no concept of "this" record by physical position; to update exactly one record you use a condition referring to the value of its primary key. Insertion order and physical position are not valid ways to address a single row.
