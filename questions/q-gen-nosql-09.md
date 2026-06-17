---
id: "q-gen-nosql-09"
exam: ""
number: 09
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["nosql"]
---

Why is the notion of an aggregate useful in aggregate-based databases according to the lecture?

- a) It allows the DBMS to support full multi-table JOINs efficiently
- b) The DBMS can use it to store and distribute data, e.g. placing an entire order on the same cluster node (sharding)
- c) It guarantees strict consistency across all cluster nodes
- d) It removes the need for any client-side data structure

### Explanation

Knowing the aggregate lets the DBMS decide which data belongs on the same node, so all data of one aggregate (e.g. an order) is stored together, supporting sharding (b). Aggregate-based stores generally do not support JOINs (a), do not guarantee strict consistency (c), and clients still assume an implicit schema (d).
