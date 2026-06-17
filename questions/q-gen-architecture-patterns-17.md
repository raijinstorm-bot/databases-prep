---
id: "q-gen-architecture-patterns-17"
exam: ""
number: 17
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["d"]
pdfs: ["architecture-patterns"]
---

In the case study where a head office must have a complete list of regional invoices by the end of the next business day, why does the lecture favour transactional replication over distributed transactions?

- a) Distributed transactions cannot copy invoice data at all
- b) Replication guarantees stronger on-line consistency than distributed transactions
- c) Distributed transactions are not supported by Ms SQL Server
- d) With distributed transactions, no invoices could be issued once the central server became unavailable, whereas replication lets the local log-reader agent gather changes and deliver them once the connection is restored

### Explanation

The lecture notes the drawback of distributed transactions is that no invoices can be issued when the central server is unavailable, while transactional replication still gathers local changes and delivers them after reconnection (d). Distributed transactions offer stronger consistency, not replication, so b is false.
