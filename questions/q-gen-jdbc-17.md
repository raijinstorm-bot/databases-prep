---
id: "q-gen-jdbc-17"
exam: ""
number: 17
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["jdbc"]
---

What is the root cause of the SQL injection vulnerability illustrated in the "Combining query text with user input" slides?

- a) Using a PreparedStatement with bind parameters
- b) Concatenating raw user input directly into the SQL query text
- c) Closing the ResultSet too early
- d) Using the Oracle thin driver instead of a thick driver

### Explanation

The vulnerability arises because raw user input is concatenated into the query string, letting an attacker inject SQL such as a `UNION SELECT` that changes the query's intent. Parametrized queries (the fix) are not the cause, and resource closing or driver type are unrelated.
