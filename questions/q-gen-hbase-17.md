---
id: "q-gen-hbase-17"
exam: ""
number: 17
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["hbase"]
---

The lecture notes that, using the HBase shell, different column values of a row get different timestamps by default. How can all column values of a row share the same timestamp?

- a) By using the `scan` command instead of `get`
- b) By using the API to insert the entire row at the same time
- c) By creating the table with a single column family
- d) It is impossible; shell and API both always assign distinct timestamps

### Explanation

The shell puts one value at a time, so columns get different timestamps; the lecture states the API can insert an entire row at once, in which case all column values share the same timestamp (b). The choice of command (a), number of families (c), or claiming it is impossible (d) do not achieve this.
