---
id: "q-gen-concurrency-09"
exam: ""
number: 09
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["concurrency"]
---

How does the SNAPSHOT isolation level work, according to the presentation?

- a) It blocks all reads until other transactions finish
- b) A transaction sees the content of the database as it was at the start of the transaction
- c) It permits dirty reads to maximise performance
- d) It only prevents phantoms but allows dirty reads

### Explanation

The table states that under SNAPSHOT a transaction sees the content of the database as it was at the start of the transaction, preventing dirty reads, non-repeatable reads, and phantoms. It does not block reads or permit dirty reads.
