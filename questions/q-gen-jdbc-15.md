---
id: "q-gen-jdbc-15"
exam: ""
number: 15
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "c"]
pdfs: ["jdbc"]
---

According to the presentation, when and why should a `PreparedStatement` be preferred over a regular `Statement`?

- a) When an SQL statement is to be executed a number of times
- b) Only for SELECT statements, never for modifications
- c) Because it creates a precompiled statement on the DBMS side, reducing execution time
- d) Because it cannot be used with bind parameters

### Explanation

A PreparedStatement should be preferred when a statement is executed repeatedly, because it creates a precompiled statement on the DBMS side that significantly reduces execution time. It works for both selecting and modifying data and supports bind parameters, so the other options are wrong.
