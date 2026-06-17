---
id: "q-gen-oracle-storage-backup-03"
exam: ""
number: 03
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["d"]
pdfs: ["oracle-storage-backup"]
---

Which SHUTDOWN mode terminates the instance immediately, leaving uncommitted transactions not rolled back so that instance recovery is performed at the next startup?

- a) NORMAL
- b) TRANSACTIONAL
- c) IMMEDIATE
- d) ABORT

### Explanation

ABORT terminates the instance immediately (equivalent to a power failure), does not synchronise files and does not roll back uncommitted transactions, so instance recovery runs on the next open. NORMAL, TRANSACTIONAL and IMMEDIATE are orderly shutdowns that leave the database synchronised.
