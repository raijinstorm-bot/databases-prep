---
id: "q-gen-concurrency-01"
exam: ""
number: 01
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["concurrency"]
---

Why are transactions executed in parallel rather than strictly serialised, according to the presentation?

- a) Serial execution is impossible in modern DBMSs
- b) Complete isolation through serialisation would diminish DBMS performance
- c) Parallel execution guarantees that no anomalies can ever occur
- d) The ACID properties forbid serial execution

### Explanation

The presentation states that full isolation would require serialised execution, which would diminish performance, so a balance between performance and isolation is sought by running transactions in parallel. Parallel execution actually allows anomalies, so c is wrong, and ACID does not forbid serial execution.
