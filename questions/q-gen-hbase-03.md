---
id: "q-gen-hbase-03"
exam: ""
number: 03
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["hbase"]
---

According to the lecture's guidance on when to use HBase, roughly how much data justifies choosing it over a traditional RDBMS?

- a) A few thousand rows
- b) A few million rows
- c) Hundreds of millions or billions of rows
- d) Any amount of data, since HBase always outperforms an RDBMS

### Explanation

The lecture advises that HBase is a good candidate when you have hundreds of millions or billions of rows (c). With only a few thousand or million rows an RDBMS may be better, since the data might end up on one or two nodes leaving the cluster idle (a, b are wrong), and HBase is not universally superior (d is false).
