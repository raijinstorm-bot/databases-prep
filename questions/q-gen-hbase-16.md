---
id: "q-gen-hbase-16"
exam: ""
number: 16
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b", "d"]
pdfs: ["hbase"]
---

Which statements about versioning in HBase are correct according to the lecture?

- a) When a cell is updated, the old value is not removed but kept with its own timestamp
- b) By default, the most recent version (by timestamp) is returned
- c) Only the current value is ever stored; history is discarded
- d) More than one version of a cell's data can be requested
- e) Versioning applies to entire rows as a unit, never to individual cells

### Explanation

HBase keeps the old cell value with its own timestamp (a), returns the most recent version by default (b), and lets you request multiple versions (d). History is not discarded (c is false), and versioning is per cell (row+column combination), not whole rows (e is false).
