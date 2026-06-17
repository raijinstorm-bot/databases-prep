---
id: "q-gen-jdbc-07"
exam: ""
number: 07
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b"]
pdfs: ["jdbc"]
---

In the first sample `ConnectionTester`, which checked exceptions are caught?

- a) `ClassNotFoundException`
- b) `SQLException`
- c) `NamingException`
- d) `IOException`

### Explanation

The code catches `ClassNotFoundException` (from loading the driver via `Class.forName`) and `SQLException` (from JDBC operations). `NamingException` and `IOException` appear only in the later servlet/DataSource example, not in this one.
