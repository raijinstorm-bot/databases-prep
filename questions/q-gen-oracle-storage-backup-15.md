---
id: "q-gen-oracle-storage-backup-15"
exam: ""
number: 15
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["oracle-storage-backup"]
---

Why should any production database run in ARCHIVELOG mode rather than NOARCHIVELOG mode?

- a) It eliminates the need to ever take backups
- b) It allows recovery to the point in time immediately before a failure, including the last committed transaction
- c) It removes the need for control files
- d) It makes online redo log files unnecessary

### Explanation

ARCHIVELOG mode preserves archived redo logs so a database can be recovered to immediately before failure (or any chosen time), including the last committed transaction. Backups, control files and online redo logs are all still required, so the other options are false.
