---
id: "q-gen-hbase-05"
exam: ""
number: 05
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["hbase"]
---

How does the lecture suggest treating a migration from an RDBMS to HBase?

- a) As a simple port achieved by swapping the JDBC driver
- b) As a complete redesign rather than a port
- c) As impossible, because HBase cannot store relational data
- d) As reversible at any time with no data-model changes

### Explanation

The lecture explicitly says an RDBMS application cannot be "ported" to HBase by merely changing a JDBC driver; moving should be considered a complete redesign (b). A simple driver swap (a) is exactly what it warns against, and the other options are not claims made in the slides.
