---
id: "q-gen-oracle-storage-backup-08"
exam: ""
number: 08
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["oracle-storage-backup"]
---

Which tablespace category holds the image of data before modifications so that other users' queries can still be answered while the data is being changed?

- a) Permanent
- b) Temporary
- c) Undo
- d) System

### Explanation

Undo tablespaces hold the pre-modification image of data so concurrent queries can be answered consistently while data changes. Permanent tablespaces keep persistent schema objects, temporary ones hold sort/temporary-table data, and there can be many undo tablespaces but only one active at a time.
