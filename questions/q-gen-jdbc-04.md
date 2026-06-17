---
id: "q-gen-jdbc-04"
exam: ""
number: 04
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["jdbc"]
---

In the first connection option, which method call is used to load a specified JDBC driver?

- a) `DriverManager.load(...)`
- b) `Class.forName(...)`
- c) `con.loadDriver(...)`
- d) `Statement.register(...)`

### Explanation

In the sample code, the driver is loaded with `Class.forName("oracle.jdbc.driver.OracleDriver")`. `DriverManager.getConnection(...)` then establishes the connection, but it does not load the driver, and the other methods do not exist in the example.
