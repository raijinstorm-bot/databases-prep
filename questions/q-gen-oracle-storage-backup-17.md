---
id: "q-gen-oracle-storage-backup-17"
exam: ""
number: 17
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["d"]
pdfs: ["oracle-storage-backup"]
---

A whole backup in Oracle contains all data files for permanent tablespaces, one copy of the control file, and the spfile. Which files are NOT copied?

- a) Permanent tablespace data files
- b) The control file
- c) The spfile
- d) Online redo log files and temporary tablespace data files

### Explanation

Online redo log files are not copied (they are protected by multiplexing and archiving), and data files for temporary tablespaces are not copied either. A whole backup does include permanent data files, a control file copy and the spfile.
