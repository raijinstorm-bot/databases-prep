---
id: "q-gen-jdbc-11"
exam: ""
number: 11
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["jdbc"]
---

In the servlet example, how is the DataSource obtained?

- a) By instantiating it directly with `new OracleDataSource()`
- b) By a JNDI lookup, e.g. `ic.lookup("jdbc/DBTestDS")` via an `InitialContext`
- c) By calling `DriverManager.getDataSource(...)`
- d) By reading it from an environment variable at runtime

### Explanation

The servlet creates an `InitialContext` and performs a JNDI lookup `ic.lookup("jdbc/DBTestDS")` to obtain the DataSource, so the real connection configuration is no longer hard coded. The other approaches are not used in the example.
