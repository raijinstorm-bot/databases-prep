---
id: "q-gen-oracle-security-12"
exam: ""
number: 12
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["oracle-security"]
---

How can imposing profile limits on a single user help prevent a form of Denial of Service?

- a) By encrypting that user's session traffic
- b) By preventing one user from consuming the majority of CPU or other resources via demanding queries
- c) By auditing the user's SELECT statements
- d) By locking the account after password expiry

### Explanation

A single user submitting particularly demanding queries could consume most of the CPU or other resources, making the DBMS unresponsive (a form of DoS); profile resource limits cap such consumption. Encryption, auditing, and password expiry do not address resource exhaustion.
