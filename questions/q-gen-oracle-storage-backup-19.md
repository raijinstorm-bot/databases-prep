---
id: "q-gen-oracle-storage-backup-19"
exam: ""
number: 19
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["oracle-storage-backup"]
---

Under which condition can an open (online) backup be performed?

- a) Only when the database is shut down
- b) Only in NOARCHIVELOG mode
- c) Only when the database runs in ARCHIVELOG mode
- d) Only when no temporary tablespaces exist

### Explanation

An online (open) backup can only be done when the database runs in ARCHIVELOG mode, because archived logs are needed to make the inconsistent online copy usable. A backup taken while shut down is a closed/offline backup, not an open one.
