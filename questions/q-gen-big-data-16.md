---
id: "q-gen-big-data-16"
exam: ""
number: 16
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["big-data"]
---

What is a key advantage of Hadoop's architecture beyond just storing large volumes of data?

- a) It enforces a strict relational schema on all stored files
- b) It centralises all processing on a single master node
- c) Individual data chunks can be processed locally by individual servers (e.g. with MapReduce tasks)
- d) It guarantees ACID transactions across the whole cluster

### Explanation

Hadoop processes individual data chunks locally on the servers that store them (e.g. with MapReduce), giving unprecedented cluster performance (c). It does not impose a relational schema (a), does not centralise processing (b), and does not provide cluster-wide ACID transactions (d).
