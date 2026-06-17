---
id: "q-gen-oracle-storage-backup-05"
exam: ""
number: 05
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["oracle-storage-backup"]
---

During a normal shutdown, which process executes a checkpoint that forces the DBWn process to write all data from the buffer cache to the data files?

- a) PMON
- b) CKPT
- c) LGWR
- d) ARCn

### Explanation

During normal shutdown CKPT executes a checkpoint that forces DBWn to write dirty buffers to the data files. PMON rolls back incomplete transactions, LGWR writes log buffers to online redo logs, and ARCn archives inactive redo logs.
