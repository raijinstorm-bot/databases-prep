---
id: "q-gen-nosql-05"
exam: ""
number: 05
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b", "c"]
pdfs: ["nosql"]
---

Which statements about column-family databases are correct according to the lecture?

- a) The set of columns used can differ from row to row
- b) Columns are grouped into column families, which are groups frequently accessed together
- c) One column belongs to exactly one column family
- d) Column families are added very frequently and cheaply at runtime
- e) Every row must use the same fixed number of columns

### Explanation

In column-family stores, each row can use its own set and number of columns (a, so e is false), columns are grouped into families accessed together (b), and each column belongs to exactly one family (c). Column families are rarely added and doing so may even require stopping the database (so d is false).
