---
id: "q-gen-oracle-storage-backup-01"
exam: ""
number: 01
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["oracle-storage-backup"]
---

In which instance state does Oracle first check that all control files listed in the initialisation parameters exist and are identical?

- a) NOMOUNT
- b) SHUTDOWN
- c) MOUNT
- d) OPEN

### Explanation

MOUNT adds, on top of NOMOUNT, the check that all control files exist and are identical; if at least one is missing or damaged the instance stays in NOMOUNT. NOMOUNT only starts the instance and SGA, SHUTDOWN has no processes, and OPEN happens only after control files are already verified at MOUNT.
