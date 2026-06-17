---
id: "q-gen-sql-select-16"
exam: ""
number: 16
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b"]
pdfs: ["sql-select"]
---

The presentation shows two query styles for linking tables. Which statements are correct?

```sql
-- Style 1
SELECT * FROM rooms, assets
WHERE rooms.bld_code = assets.bld_code AND rooms.room = assets.room

-- Style 2
SELECT * FROM rooms JOIN assets
ON rooms.bld_code = assets.bld_code AND rooms.room = assets.room
```

- a) Style 1 is the WHERE-based query style
- b) Style 2 is the JOIN-based query style
- c) Only Style 2 can express a join condition on two columns
- d) Style 1 uses the `ON` keyword to specify conditions

### Explanation

The presentation contrasts a WHERE-based style (tables listed in FROM, conditions in WHERE) with a JOIN-based style (using JOIN ... ON). Both can combine conditions with AND; `ON` belongs to the JOIN style, not the WHERE style.
