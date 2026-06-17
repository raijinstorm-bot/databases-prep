---
id: "q-gen-oracle-net-09"
exam: ""
number: 09
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "c"]
pdfs: ["oracle-net"]
---

Which statements about the Oracle Net Listener are correct?

- a) One listener can service multiple database instances identified by service names
- b) The listener is a part of the DBMS instance
- c) The listener resides on the server and establishes network communication between clients and the DBMS
- d) Each client connection requires its own dedicated listener for its entire lifetime

### Explanation

A single listener can service multiple instances by service name, and it resides on the server to broker client-server communication. The listener is explicitly not part of the instance, and after the connection is established the listener is no longer involved, so a per-connection listener is wrong.
