---
id: "q-gen-oracle-storage-backup-02"
exam: ""
number: 02
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["oracle-storage-backup"]
---

Which files are needed for an Oracle instance to reach the NOMOUNT state?

- a) All control files
- b) Initialisation parameter files (init file or spfile)
- c) At least one redo log file in each group
- d) All on-line data files

### Explanation

To reach NOMOUNT the instance only needs the initialisation parameter file(s), which start the instance and establish the SGA. Control files are required for MOUNT, while redo log files and on-line data files are checked when entering OPEN.
