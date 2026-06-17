---
id: "q-gen-jdbc-12"
exam: ""
number: 12
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["jdbc"]
---

When a DataSource backed by a connection pool is used, what does calling `close()` on the obtained connection typically do?

- a) Permanently terminates the physical connection to the DBMS
- b) Rolls back all transactions of the application
- c) Releases the connection so it can be reused
- d) Shuts down the application server's pool

### Explanation

With a pooling DataSource, `getConnection()` usually returns an existing connection and `close()` releases it back to the pool for reuse rather than physically closing it. This reuse is what yields the dramatic performance improvements described.
