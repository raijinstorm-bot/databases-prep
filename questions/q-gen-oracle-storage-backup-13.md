---
id: "q-gen-oracle-storage-backup-13"
exam: ""
number: 13
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b", "c"]
pdfs: ["oracle-storage-backup"]
---

Which statements about online redo log files are correct?

- a) They are used in a circular fashion across groups
- b) A log switch occurs when the active group changes and causes a checkpoint
- c) Each group consists of one or more members that are mirror images of each other
- d) There is always exactly one group of redo log files per database

### Explanation

Online redo logs are reused circularly (a), a log switch between groups triggers a checkpoint (b), and each group has one or more mirror members (c). There must be at least two groups, so (d) is false.
