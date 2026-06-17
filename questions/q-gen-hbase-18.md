---
id: "q-gen-hbase-18"
exam: ""
number: 18
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b", "c"]
pdfs: ["hbase"]
---

According to the lecture, at which levels can a delete operation be performed in HBase?

- a) At cell and timestamp level (a specific version)
- b) At cell level (all versions of a column value)
- c) At row level (all data of a row, e.g. via deleteall)
- d) At column-family level for the whole table at once
- e) At keyspace level

### Explanation

The lecture states delete can be performed at cell&timestamp, cell, and row level (a, b, c) — the examples show deleting a specific version, a whole cell, and `deleteall` for an entire row. Deleting an entire column family table-wide (d) and a keyspace level (e, a Cassandra concept) are not listed.
