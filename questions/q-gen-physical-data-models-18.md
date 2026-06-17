---
id: "q-gen-physical-data-models-18"
exam: ""
number: 18
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["physical-data-models"]
---

In the client-server approach to databases, what is primarily transferred over the network between client applications and the DBMS?

- a) The entire database files
- b) The raw data pages of all tables
- c) SQL statements and the results of queries
- d) The DBMS engine itself

### Explanation

In the client-server model, clients send SQL statements over the network and only the results of queries are transferred back. The full database files are not sent (improving scalability and security); the engine stays on the server.
