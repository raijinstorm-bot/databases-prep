---
id: "q-gen-oracle-security-07"
exam: ""
number: 07
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["oracle-security"]
---

Which SQL statement is used to list user accounts together with their lock status?

- a) `select username, profile from dba_users`
- b) `select username, account_status from dba_users`
- c) `select * from dba_profiles where profile='DEFAULT'`
- d) `revoke execute on utl_file from public`

### Explanation

`select username, account_status from dba_users` lists accounts and whether they are open or locked. Querying username/profile shows profile assignments, the dba_profiles query shows profile limits, and the revoke statement changes a privilege.
