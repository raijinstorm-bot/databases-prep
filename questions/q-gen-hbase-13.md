---
id: "q-gen-hbase-13"
exam: ""
number: 13
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b", "c"]
pdfs: ["hbase"]
---

According to the "HBase tables: discussion" slide, which statements are correct?

- a) Only column families are declared when creating a table
- b) Whether a column family always contains the same columns in each row is up to the client application
- c) Any cell is just an array of bytes from HBase's perspective, with no explicit data-type support
- d) Individual columns must be declared in advance like in an RDBMS
- e) Entire rows, not cells, are the unit inserted and retrieved

### Explanation

The slide states only column families are declared (a), column consistency across rows is the client's responsibility (b), and cells are byte arrays with no explicit typing (c). Columns are not pre-declared (d is false), and because a row may contain millions of columns, individual cells rather than whole rows are inserted/retrieved (e is false).
