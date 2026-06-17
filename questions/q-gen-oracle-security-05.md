---
id: "q-gen-oracle-security-05"
exam: ""
number: 05
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["oracle-security"]
---

A permission is granted to the PUBLIC pseudo-user in Oracle. What is the effect?

- a) Only the DBA gains that permission
- b) All users of the database are granted that permission
- c) The permission is granted only to locked accounts
- d) The permission applies only to system-defined roles

### Explanation

Any permission granted to the PUBLIC pseudo-user is granted to all users of the database, which is why risky packages such as UTL_FILE should be revoked from PUBLIC. It is not limited to the DBA, locked accounts, or roles.
