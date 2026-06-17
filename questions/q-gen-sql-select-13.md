---
id: "q-gen-sql-select-13"
exam: ""
number: 13
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "c"]
pdfs: ["sql-select"]
---

Consider the query:

```sql
SELECT * FROM rooms ORDER BY type, floor
```

According to the presentation, which statements about this multi-column sort are correct?

- a) Ascending order is the default for both columns
- b) `floor` is the primary sort key and `type` the tie-breaker
- c) Rows with equal `type` are then ordered by `floor`
- d) `DESC` must be specified or the query is invalid

### Explanation

The ORDER BY slide states ascending is the default and that with multiple columns rows equal on the first column are compared by the second. So `type` is primary and `floor` breaks ties; `DESC` is optional, not required.
