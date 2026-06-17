---
id: "q-gen-concurrency-13"
exam: ""
number: 13
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b"]
pdfs: ["concurrency"]
---

According to the presentation, which statements about the two MS SQL Server schema lock categories are correct?

- a) Schema stability locks ensure a db object will not be removed while used by another transaction
- b) Schema modification locks prevent access to db objects that are being modified
- c) Schema stability locks prevent any concurrent reads of the data
- d) Schema modification locks are placed automatically during every SELECT

### Explanation

Schema stability locks keep an object from being removed while in use (and are applied when compiling/executing queries, allowing concurrent data changes), while schema modification locks block access to objects being altered by DDL. Schema stability does not block data reads, and schema modification locks accompany DDL, not SELECTs.
