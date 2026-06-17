---
id: "q-gen-nosql-18"
exam: ""
number: 18
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["nosql"]
---

The lecture defines eventual consistency in a distributed data store as which of the following?

- a) A read always returns the most recently written data
- b) All replicas of the data will eventually become consistent, so reads during that time may return stale data
- c) The system refuses all reads until every replica is updated
- d) Consistency defined exactly as in ACID transactions

### Explanation

Eventual consistency means replicas become consistent after some time, so reads may temporarily return not-the-most-recent data (b). Returning the most recent data always describes strict consistency (a); the system stays available rather than refusing reads (c); and the lecture warns this consistency is not the same as ACID consistency (d).
