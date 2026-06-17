---
id: "q-gen-stored-procedures-08"
exam: ""
number: 08
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "c"]
pdfs: ["stored-procedures"]
---

According to the comparison of stored procedures versus direct query processing, which statements are correct?

- a) With direct processing, each query and its result is a separate round-trip between client and DBMS
- b) Stored procedures require one round-trip per internal statement, just like direct processing
- c) Using stored procedures can significantly reduce network communication overhead
- d) Direct query processing performs all loops internally on the server with a single request

### Explanation

In the standard pattern each SQL query/result is its own client-DBMS round-trip (a), whereas a stored procedure executes internally and returns its result in a single round-trip, cutting network overhead (c). Statements b and d invert these facts.
