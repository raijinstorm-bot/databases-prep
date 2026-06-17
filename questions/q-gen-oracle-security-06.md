---
id: "q-gen-oracle-security-06"
exam: ""
number: 06
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["oracle-security"]
---

Why does the presentation specifically warn about the UTL_FILE package being granted to everyone?

- a) It allows users to lock other accounts
- b) It consumes excessive CPU resources
- c) It lets users read and write operating system text files, which can serve as a backdoor into the OS
- d) It bypasses all auditing settings

### Explanation

With UTL_FILE users can read and write operating system text files, so granting it broadly can turn the DBMS into a backdoor for breaking into the operating system. It is not about locking accounts, CPU usage, or bypassing auditing.
