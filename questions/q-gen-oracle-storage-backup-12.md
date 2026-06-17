---
id: "q-gen-oracle-storage-backup-12"
exam: ""
number: 12
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["oracle-storage-backup"]
---

Which background process writes log buffers to the online redo log files?

- a) DBWn
- b) LGWR
- c) PMON
- d) SMON

### Explanation

LGWR (Log Writer) writes the log buffers to the online redo log files. DBWn writes dirty buffers to data files, PMON cleans up failed processes/rolls back transactions, and SMON handles instance recovery.
