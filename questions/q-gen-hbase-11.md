---
id: "q-gen-hbase-11"
exam: ""
number: 11
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["hbase"]
---

In the sample measurements table, which command correctly creates a table with the two column families used in the lecture?

- a) create 'measurements','parameter','value'
- b) create 'measurements','results:parameter','time:timeStamp'
- c) create 'measurements','results','time'
- d) create 'measurements' with columns (parameter, value, precision)

### Explanation

When creating an HBase table only the column families are declared, not individual columns. The lecture uses `create 'measurements','results','time'` (c). Options a, b and d incorrectly include column qualifiers or RDBMS-style column declarations.
