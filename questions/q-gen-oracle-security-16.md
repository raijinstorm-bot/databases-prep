---
id: "q-gen-oracle-security-16"
exam: ""
number: 16
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["oracle-security"]
---

For security reasons, what is required after changing the AUDIT_TRAIL parameter?

- a) Nothing; the change takes effect immediately
- b) The instance must be restarted for the change to take effect
- c) All user profiles must be recreated
- d) All audit views must be dropped and recreated

### Explanation

The presentation states that, for security reasons, the AUDIT_TRAIL setting cannot be changed without restarting the instance (hence it is set with scope=spfile). Recreating profiles or dropping audit views is not required.
