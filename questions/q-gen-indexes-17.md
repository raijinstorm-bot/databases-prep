---
id: "q-gen-indexes-17"
exam: ""
number: 17
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b", "c"]
pdfs: ["indexes"]
---

Which statements about a query execution plan are correct?

- a) It is an algorithm describing how the DBMS will execute the statement
- b) Its steps may include scanning index trees and table content
- c) It can be investigated to identify and eliminate bottlenecks in data processing
- d) It guarantees every query runs in constant time regardless of table size

### Explanation

A query execution plan is the algorithm for executing a statement (a), its steps include scanning indexes and tables (b), and it can be analysed to find bottlenecks (c). Scanning large tables without a suitable index can give unacceptable response time, so (d) is false.
