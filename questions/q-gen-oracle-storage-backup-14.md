---
id: "q-gen-oracle-storage-backup-14"
exam: ""
number: 14
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["oracle-storage-backup"]
---

In ARCHIVELOG mode, which background process ensures that redo log files are archived before being overwritten?

- a) LGWR
- b) DBWn
- c) ARCn
- d) CKPT

### Explanation

When a database runs in ARCHIVELOG mode the ARCn processes (ARC0, ARC1, ...) copy inactive redo logs to archive logs before LGWR can overwrite them. LGWR writes redo, DBWn writes data blocks, and CKPT signals checkpoints.
