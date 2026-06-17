---
id: "q-gen-jdbc-09"
exam: ""
number: 09
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["jdbc"]
---

If the `ConnectionTester` example needed to connect to a different DBMS instead of Oracle, what would have to change?

- a) Nothing, JDBC code is fully DBMS-independent including the driver
- b) The Java language version
- c) A different JDBC driver would be needed
- d) The `ResultSet` interface would have to be reimplemented

### Explanation

The slide explicitly notes that the Oracle JDBC driver is used and that another driver would be needed to access another DBMS. The JDBC API itself stays the same, so the application code is largely portable, but the driver is DBMS-specific.
