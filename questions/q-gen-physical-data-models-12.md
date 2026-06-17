---
id: "q-gen-physical-data-models-12"
exam: ""
number: 12
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["physical-data-models"]
---

What is the main motivation for horizontal partitioning, i.e. splitting records into partitions?

- a) To store the most frequently used columns separately from the rest
- b) To avoid processing all rows when, most frequently, only the recent ones are queried
- c) To enforce referential integrity between tables
- d) To convert a relational table into a document store

### Explanation

Horizontal partitioning splits records into partitions to avoid processing all rows when typically only recent ones are queried. Separating columns is vertical partitioning; partitioning is not about integrity enforcement or document conversion.
