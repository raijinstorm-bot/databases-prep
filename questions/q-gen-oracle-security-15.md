---
id: "q-gen-oracle-security-15"
exam: ""
number: 15
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["oracle-security"]
---

What distinguishes the DB_EXTENDED setting of AUDIT_TRAIL from the plain DB setting?

- a) It writes the trail to the operating system instead of the database
- b) It disables auditing of the DBA
- c) It additionally saves the SQL statements with bind variables that generated the audit trail
- d) It encrypts the audit trail table

### Explanation

DB_EXTENDED behaves like DB but additionally records the SQL statements (with bind variables) that generated each audit record. It still writes to the database, does not disable DBA auditing, and does not encrypt the trail.
