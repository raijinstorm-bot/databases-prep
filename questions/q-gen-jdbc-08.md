---
id: "q-gen-jdbc-08"
exam: ""
number: 08
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["jdbc"]
---

In the connection string `jdbc:oracle:thin:@localhost:1521:ORCL`, what does `1521` represent?

- a) The maximum number of pooled connections
- b) The network port on which the DBMS listens
- c) The Oracle driver version
- d) The session identifier of the connection

### Explanation

In the JDBC URL, `1521` is the TCP port on which the Oracle DBMS listens (its default), with `localhost` the host and `ORCL` the database/SID. It is not a pool size, driver version, or session id.
