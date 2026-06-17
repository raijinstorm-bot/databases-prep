---
id: "q-gen-nosql-20"
exam: ""
number: 20
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "c", "d"]
pdfs: ["nosql"]
---

Which statements about graph databases are correct according to the lecture?

- a) Unlike other NoSQL categories, they are not oriented on clusters and the data is most likely kept on a single server
- b) They avoid ACID operations because graphs never need consistent multi-node updates
- c) They improve search performance largely at the cost of extra overhead when inserting data
- d) Neo4j allows Java objects to be added as properties of both nodes and edges
- e) They are primarily designed for simple single-key lookups rather than relationship searches

### Explanation

Graph databases are not cluster-oriented, usually run on a single server (a), and trade insert-time overhead for faster (often complex relationship) searches (c). Neo4j supports Java-object properties on nodes and edges (d). ACID operations are described as mandatory and easier to implement on a single server (so b is false), and they target complex relationship searches, not simple key lookups (so e is false).
