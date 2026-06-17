---
id: "q-gen-oracle-storage-backup-04"
exam: ""
number: 04
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b", "c"]
pdfs: ["oracle-storage-backup"]
---

Which of the following are considered "normal" (orderly) shutdown modes in Oracle?

- a) NORMAL
- b) TRANSACTIONAL
- c) IMMEDIATE
- d) ABORT
- e) RESTRICT

### Explanation

NORMAL, TRANSACTIONAL and IMMEDIATE are collectively referred to as normal shutdown modes, in which PMON rolls back incomplete transactions and a checkpoint flushes the buffer cache before files are closed. ABORT is the disorderly shutdown, and RESTRICT is a startup option, not a shutdown mode.
