---
id: "q-gen-nosql-19"
exam: ""
number: 19
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b", "d"]
pdfs: ["nosql"]
---

Which statements about the CAP theorem as presented in the lecture are correct?

- a) Only two of the three properties (Consistency, Availability, Partition tolerance) can be guaranteed at the same time
- b) Because network problems are unavoidable, in practice one must choose between consistency and availability
- c) CA systems are the most useful choice in real-life deployments
- d) Cassandra basically belongs to AP systems, also referred to as BASE systems
- e) The theorem was formulated by E. Codd

### Explanation

CAP (by Eric Brewer) says only two of the three properties hold simultaneously, and since partition tolerance is needed, the real trade-off is consistency vs availability (a, b). Cassandra is an AP/BASE system (d). CA systems are described as not really useful since partition tolerance is needed (c is false), and Codd did not formulate CAP (e is false).
