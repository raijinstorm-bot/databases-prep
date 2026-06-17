---
id: "q-gen-nosql-17"
exam: ""
number: 17
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["nosql"]
---

According to the Cassandra data-organisation hierarchy, what is a partition?

- a) A separate Cassandra instance hosting many keyspaces
- b) A synonym for a keyspace
- c) A set of rows sharing the same value of the partition key, making up a table
- d) A single atomic column value within a row

### Explanation

In Cassandra, a table is composed of partitions, where a partition is the rows sharing the same partition-key value (c). A keyspace is more like a database (a, b are wrong), and a partition is a group of rows, not a single column value (d).
