---
id: "q-gen-oracle-net-17"
exam: ""
number: 17
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["oracle-net"]
---

Which Oracle Net configuration file defines the overall NET configuration, including which naming methods are used to resolve network names?

- a) tnsnames.ora
- b) sqlnet.ora
- c) listener.ora
- d) names.ora

### Explanation

sqlnet.ora holds the overall NET configuration, such as `NAMES.DIRECTORY_PATH=(TNSNAMES, EZCONNECT)`, controlling which naming methods are used. tnsnames.ora maps local names to connect descriptors, and listener.ora defines the listeners and the instances they handle.
