---
id: "q-gen-hbase-06"
exam: ""
number: 06
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["hbase"]
---

The lecture notes that even HDFS does not perform well below a certain number of DataNodes. What number is given, and why?

- a) 2, because of the NameNode requirement
- b) 3, because of CQL replication
- c) 5, because HDFS block replication defaults to 3 (plus a NameNode)
- d) 10, because of the column-family limit

### Explanation

The lecture states even HDFS does not do well with fewer than 5 DataNodes, due to factors such as HDFS block replication defaulting to 3, plus a NameNode (c). The other counts and reasons are not what the slide gives.
