---
id: "q-gen-jdbc-18"
exam: ""
number: 18
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "c"]
pdfs: ["jdbc"]
---

What does the presentation say about SQL code injection and its mitigation?

- a) It can be attempted with any API (such as JDBC or ADO.NET) and any DBMS
- b) It is only possible with the Oracle thin driver
- c) Using parametrized queries (e.g. PreparedStatement) makes clear that a value, not SQL code, belongs in part of the statement
- d) It cannot occur in web applications

### Explanation

The slides state that SQL injection can be attempted with any API and any DBMS, is even easier with web applications, and is mitigated by parametrized queries that distinguish a value from SQL code. So the claims limiting it to one driver or excluding web apps are false.
