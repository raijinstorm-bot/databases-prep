---
id: "q-gen-jdbc-05"
exam: ""
number: 05
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["b", "c"]
pdfs: ["jdbc"]
---

What are the stated disadvantages of the first connection option (loading a driver explicitly)?

- a) The same API cannot be used to access different databases
- b) The JDBC driver name is hard coded in the application
- c) It takes time to establish and close a connection
- d) An application server is always required

### Explanation

The disadvantages listed are that the driver name is hard coded and that establishing/closing connections takes time (so pooling should be applied). Using the same API across databases is actually an advantage, and requiring an application server is a trait of the second (DataSource) option.
