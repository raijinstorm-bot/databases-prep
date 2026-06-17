---
id: "q-gen-jdbc-19"
exam: ""
number: 19
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["jdbc"]
---

Regarding try-with-resources in JDBC, what caution does the presentation raise about the `Connection` object?

- a) Connection does not implement `AutoCloseable`, so it cannot be used there at all
- b) Statements and ResultSets must never be declared in try-with-resources
- c) Closing a Connection automatically can be risky because it may close before the transaction status is resolved
- d) try-with-resources commits the transaction automatically before closing

### Explanation

Connection implements `AutoCloseable`, but the slide warns that auto-closing it can be risky: if there is an active transaction, the JDBC standard says the results are implementation-defined, so the connection might close before the transaction is committed or rolled back. Statements and ResultSets, by contrast, are safe to declare there.
