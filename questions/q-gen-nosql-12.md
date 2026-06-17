---
id: "q-gen-nosql-12"
exam: ""
number: 12
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["nosql"]
---

How do aggregate-based DBMSs typically deal with cross-aggregate queries, according to the lecture?

- a) By executing arbitrary multi-table JOINs at query time
- b) By forbidding such queries entirely
- c) By using materialised views, i.e. precomputed results for typical queries
- d) By converting the store into a relational database on the fly

### Explanation

The lecture says aggregate-based DBMSs may require materialised views — precomputed results for typical queries, updated online or periodically/on request (c). Aggregate-ignorant systems (including relational) handle cross-row, cross-table queries straightforwardly, but aggregate-based stores generally do not do arbitrary JOINs (a).
