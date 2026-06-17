---
id: "q-gen-sql-select-19"
exam: ""
number: 19
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["sql-select"]
---

In the presentation's `EXISTS` example over `Rooms` and `Assets`, the query returns rooms that have at least one matching asset:

```sql
SELECT * FROM Rooms R WHERE EXISTS
(SELECT * FROM Assets A WHERE R.room_id = A.room_id)
```

Given rooms with `room_id` 7 and 15, and assets only for `room_id` 15 (and 18), which rooms appear in the output?

- a) Both room 7 and room 15
- b) Only room 15
- c) Only room 7
- d) No rooms

### Explanation

For each room the correlated subquery checks whether any asset shares its `room_id`. Room 7 has no matching assets so it is excluded; room 15 has two matching assets so it is included. Asset row 18 matches no listed room.
