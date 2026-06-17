---
id: "q-gen-jdbc-13"
exam: ""
number: 13
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["jdbc"]
---

According to the presentation, who creates the pool of connections that a DataSource provides access to?

- a) The JDBC driver automatically on first query
- b) An application server
- c) The DBMS itself for every client
- d) The client web browser

### Explanation

The slide states that a pool of connections is created by an application server, and the server maintains the pool as configured by the administrator. The DataSource is merely the JDBC object used to access those connections.
