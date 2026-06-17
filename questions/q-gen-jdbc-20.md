---
id: "q-gen-jdbc-20"
exam: ""
number: 20
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b", "d"]
pdfs: ["jdbc"]
---

According to the summary and discussion slides, which statements are correct?

- a) JDBC lets Java developers connect to a DBMS and submit SELECT, DML and DDL statements, and commit/rollback transactions
- b) ResultSet and Connection objects should be closed (or returned to the pool) as soon as possible to avoid resource leaks
- c) JDBC has been fully replaced by the Java Persistence API and is no longer used
- d) The Java Persistence API provides object-relational mapping, but JDBC remains the core standard on top of which layers can be built

### Explanation

JDBC enables connecting, running SELECT/DML/DDL, and managing transactions; resources should be released promptly to avoid leaks; and JPA adds object-relational mapping while JDBC remains the underlying core standard. The claim that JPA fully replaced JDBC contradicts the summary, which says JDBC remains foundational.
