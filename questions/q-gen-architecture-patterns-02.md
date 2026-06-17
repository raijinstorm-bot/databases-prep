---
id: "q-gen-architecture-patterns-02"
exam: ""
number: 02
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["architecture-patterns"]
---

In the file-based approach described in the lecture, how do database applications access the data?

- a) Through a dedicated server process that performs all data processing centrally
- b) Through a REST API exposed by a middle-tier application server
- c) Through an embedded DBMS engine (a software library) reading the database, which is just a collection of files
- d) Through a distributed transaction coordinator

### Explanation

The lecture states that in the file-based approach, applications access the database (just a collection of files) through an embedded DBMS engine that is a software library (c). There is no central server process; that is the server-based model the file-based approach lacks.
