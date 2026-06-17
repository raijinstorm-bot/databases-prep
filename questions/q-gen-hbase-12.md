---
id: "q-gen-hbase-12"
exam: ""
number: 12
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b"]
pdfs: ["hbase"]
---

In the HBase shell, what do the `scan` and `get` commands do in the lecture's examples?

- a) `scan 'measurements'` displays the entire table content
- b) `get 'measurements','1','results:value'` retrieves one or more specific column values
- c) `scan` deletes all rows after displaying them
- d) `get` can only ever return one column and never multiple
- e) `scan` declares new column families

### Explanation

In the examples, `scan` displays the entire table content (a) and `get` retrieves one or more specified column values for a row (b) — the lecture shows `get` returning two columns at once, so d is false. `scan` does not delete or declare anything (c, e are false).
