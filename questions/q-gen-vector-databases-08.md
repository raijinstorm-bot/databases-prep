---
id: "q-gen-vector-databases-08"
exam: ""
number: 08
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "c"]
pdfs: ["vector-databases"]
---

According to the presentation, queries that find records with the most similar vectors can rely on which approaches? (Select all that apply.)

- a) Exact search, also known as k-nearest neighbor (kNN)
- b) Full table scan using SQL LIKE patterns
- c) Approximate vector search (approximate nearest neighbour)
- d) B-tree range scans over sorted vector values

### Explanation

The presentation states that similarity queries can rely on exact search (kNN), which can be expensive, or on approximate vector search (approximate nearest neighbour). LIKE-based pattern matching is contrasted as the old exact-match approach, and vectors are noted as not sortable, so B-tree range scans do not apply.
