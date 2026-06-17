---
id: "q-gen-sql-select-09"
exam: ""
number: 09
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["sql-select"]
---

Given the `rooms` table, what does the following query return?

```sql
SELECT building AS bld, room AS rm FROM rooms
```

- a) All columns of `rooms` with original names
- b) Two columns, `building` and `room`, renamed to `bld` and `rm` in the output
- c) An error, because `AS` cannot rename a column
- d) The `rooms` table sorted by building

### Explanation

`AS` assigns aliases to the selected columns, so the output has columns labelled `bld` and `rm`. The presentation also notes that SQL keywords like `AS` may be written in lower- or uppercase interchangeably.
