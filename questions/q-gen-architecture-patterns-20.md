---
id: "q-gen-architecture-patterns-20"
exam: ""
number: 20
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["architecture-patterns"]
---

How does the lecture contrast active/passive and active/active cluster strategies?

- a) In active/passive both servers always share the load; in active/active one server is a standby
- b) In active/passive one server is normally passive and acts as a standby that handles requests only when the primary fails; in active/active two or more servers share the load
- c) Both strategies require all servers to be idle until a failover occurs
- d) Active/active means only one server may run at a time to avoid conflicts

### Explanation

The lecture defines active/passive as one server normally passive, acting as a standby that takes over when the primary fails, and active/active as two or more servers sharing the load (b). Option a swaps the definitions, and c and d misstate both strategies.
