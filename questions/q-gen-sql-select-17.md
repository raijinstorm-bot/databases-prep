---
id: "q-gen-sql-select-17"
exam: ""
number: 17
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["sql-select"]
---

The presentation asks how to obtain room 452 in the chemistry building in the result even though there are no assets in that room. Which JOIN achieves this when `Rooms` is the parent (left) table?

- a) INNER JOIN
- b) Old-style WHERE join on equality
- c) LEFT JOIN
- d) A plain `JOIN` keyword with no qualifier

### Explanation

A LEFT JOIN keeps all records from the parent table, using NULLs for the joined table's columns when there is no match. INNER JOIN (or the plain JOIN / old-style WHERE join) keeps only matching combinations, so the asset-less room would be dropped.
