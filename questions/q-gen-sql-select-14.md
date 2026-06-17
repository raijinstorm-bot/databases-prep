---
id: "q-gen-sql-select-14"
exam: ""
number: 14
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["sql-select"]
---

What does the `DISTINCT` clause produce in the following query?

```sql
SELECT DISTINCT type, floor FROM rooms WHERE floor >= 2
```

- a) Distinct values of `type` only, ignoring `floor`
- b) Unique combinations of the `type` and `floor` column values
- c) All rows, with duplicates marked but not removed
- d) Only rows where both columns have unique values across the whole table

### Explanation

The DISTINCT slide states that unique combinations of column values/expressions are obtained. DISTINCT applies to the whole selected tuple (`type`, `floor`), not to a single column.
