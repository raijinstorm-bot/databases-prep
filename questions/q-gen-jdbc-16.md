---
id: "q-gen-jdbc-16"
exam: ""
number: 16
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["jdbc"]
---

In the PreparedStatement example performing an `UPDATE`, which method executes the statement?

- a) `ps.executeQuery()`
- b) `ps.execute(ResultSet)`
- c) `ps.executeUpdate()`
- d) `ps.commit()`

### Explanation

For a data-modifying statement such as `UPDATE`, the example calls `ps.executeUpdate()` (followed by `con.commit()`). `executeQuery()` is used for SELECTs that return a ResultSet, and `commit()` is a Connection method, not the statement executor.
