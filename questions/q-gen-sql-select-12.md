---
id: "q-gen-sql-select-12"
exam: ""
number: 12
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["d"]
pdfs: ["sql-select"]
---

The presentation states that text columns are sorted as text even when they contain numbers. Under `ORDER BY` on such a text column (ascending), which ordering is correct?

- a) `2` comes before `1000` because 2 < 1000
- b) `1000` and `2` are treated as equal
- c) Numbers in text are automatically converted to integers before sorting
- d) `'1000' < '2'`, so `1000` comes before `2`

### Explanation

The ORDER BY slide explicitly states that text columns are sorted as text even if they contain numbers, giving the example `'1000' < '2'`. Therefore `1000` sorts before `2` in ascending text order.
