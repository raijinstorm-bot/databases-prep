---
id: "q-gen-oracle-storage-backup-10"
exam: ""
number: 10
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["oracle-storage-backup"]
---

Which parameter, set in the init file or spfile, defines the location of the control files?

- a) FAST_START_MTTR_TARGET
- b) CONTROL_FILES
- c) ORACLE_SID
- d) DB_BLOCK_SIZE

### Explanation

The init file or spfile defines control file locations through the CONTROL_FILES parameter; the control files in turn point to data files and redo log files. FAST_START_MTTR_TARGET tunes recovery time, ORACLE_SID identifies the database, and DB_BLOCK_SIZE sets the block size.
