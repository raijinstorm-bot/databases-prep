---
id: "q-gen-oracle-storage-backup-09"
exam: ""
number: 09
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "c"]
pdfs: ["oracle-storage-backup"]
---

Which statements about the Oracle database block size of a tablespace are correct?

- a) All datafiles of a tablespace share the same database block size
- b) You can freely change the database block size of an existing tablespace at any time
- c) Whenever data is read or changed, entire database blocks are read or saved
- d) The database block size must be smaller than the operating system block size

### Explanation

All datafiles in a tablespace share one block size (a), and I/O always works on whole blocks (c). The block size cannot be changed for an existing tablespace (b is false) and it should be a multiple of the OS block size, not smaller than it (d is false).
