---
id: "q-gen-architecture-patterns-08"
exam: ""
number: 08
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["architecture-patterns"]
---

In the sample distributed-database architecture, how do the separate DBMS platforms most often communicate, and how do clients connect?

- a) Clients connect to a shared central server; DBMS platforms never communicate
- b) Clients connect over a VPN; DBMS platforms communicate over the LAN
- c) Clients most frequently communicate with their own local DBMS instance over a LAN, while DBMS platforms exchange data through secure connections such as a VPN
- d) Clients and DBMS platforms all share one transaction log

### Explanation

The lecture's callouts state that clients most frequently communicate with their own DBMS instance (via the local LAN), while the DBMS platforms exchange data through secure connections such as a VPN (c). The other options swap or misstate these roles.
