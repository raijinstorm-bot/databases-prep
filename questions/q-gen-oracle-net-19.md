---
id: "q-gen-oracle-net-19"
exam: ""
number: 19
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b"]
pdfs: ["oracle-net"]
---

In the client-side tnsnames.ora file, which statements are correct?

- a) Each service name (alias) is mapped to a connect descriptor
- b) A service name does not need to match the instance name
- c) The service name must be identical to the SID of the instance
- d) The file is stored on the server and used by the listener to start instances

### Explanation

tnsnames.ora lists service names/aliases each mapped to a connect descriptor, and the service name need not match the instance name. It is a client-side file; the listener uses listener.ora, and there is no requirement that the alias equal the SID.
