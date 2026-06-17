---
id: "q-gen-jdbc-06"
exam: ""
number: 06
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["jdbc"]
---

In the sample code, how are individual rows of a query result iterated and read?

- a) Using a `for` loop over `statement.getRows()`
- b) Calling `rs.fetch()` repeatedly until it returns null
- c) Calling `rs.next()` in a loop and reading columns with methods like `rs.getString(...)`
- d) Calling `con.readRow()` for each record

### Explanation

Results are accessed via a ResultSet object: `rs.next()` advances to each row and column values are read with accessors such as `rs.getString("title_name")`. The other methods do not appear in the JDBC examples.
