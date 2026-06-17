---
id: "q-gen-oracle-storage-backup-18"
exam: ""
number: 18
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["oracle-storage-backup"]
---

Which statement about incremental backups is correct?

- a) They can be created using ordinary operating system copy commands
- b) They can be created with RMAN only, which determines which blocks changed
- c) They always contain complete data files
- d) They are always larger than full backups

### Explanation

Incremental backups copy only changed data blocks and can be created with RMAN only, since the OS does not know which blocks changed (b). A full backup always contains complete data files (c describes full, not incremental), incremental backups are usually smaller (d is false), and OS commands cannot create them (a is false).
