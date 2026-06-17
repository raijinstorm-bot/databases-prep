---
id: "q-gen-nosql-16"
exam: ""
number: 16
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["nosql"]
---

What is the role of "seed nodes" in a Cassandra cluster according to the lecture?

- a) They act as master nodes coordinating all writes
- b) They help other nodes learn the topology of their cluster
- c) They are the only nodes allowed to store replicas
- d) They enforce strict consistency across the ring

### Explanation

The lecture states there is no master, but some nodes may play the role of seed nodes, which help other nodes learn the cluster topology (b). They are not masters (a), not the only replica holders (c), and do not enforce strict consistency (d).
