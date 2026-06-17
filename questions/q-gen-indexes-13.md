---
id: "q-gen-indexes-13"
exam: ""
number: 13
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b", "c"]
pdfs: ["indexes"]
---

According to the guidelines, indexes should be considered when a large number of records is expected (>1000) and which conditions hold?

- a) The column(s) are frequently used in search/sort operations
- b) The size of the index key is short
- c) There is good selectivity of the index column(s)
- d) The column has only two or three distinct values

### Explanation

Indexes are worthwhile when columns are frequently searched/sorted (a), the index key is short to avoid huge trees (b), and selectivity is good (c). Very few distinct values mean poor selectivity, which is a reason to avoid an index, so (d) is wrong.
