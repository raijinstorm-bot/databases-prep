---
id: "q-gen-concurrency-02"
exam: ""
number: 02
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["concurrency"]
---

Which anomaly occurs when a transaction reads data that has not yet been committed by another transaction?

- a) Lost update
- b) Phantom
- c) Dirty read
- d) Non-repeatable read

### Explanation

A dirty read happens when a transaction reads uncommitted data; if the other transaction later rolls back, the first transaction has read data that never really existed. Lost updates, phantoms and non-repeatable reads describe different scenarios.
