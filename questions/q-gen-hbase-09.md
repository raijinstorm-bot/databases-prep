---
id: "q-gen-hbase-09"
exam: ""
number: 09
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["hbase"]
---

How is a column referred to in HBase using its fully qualified name?

- a) 'columnInFamily.family'
- b) 'family:columnInFamily'
- c) 'keyspace.table.column'
- d) 'row/column'

### Explanation

Since columns are grouped into column families, HBase columns are referred to with fully qualified names of the form 'family:columnInFamily' (b), e.g. results:value. The other forms are not the HBase notation.
