---
id: "q-gen-indexes-19"
exam: ""
number: 19
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b"]
pdfs: ["indexes"]
---

What does MS SQL Server's automated tuning (introduced in 2017, present in Azure SQL Database) do?

- a) Identifies problematic query execution plans and fixes them, e.g. by restoring previous better plans when plan regression is detected
- b) Identifies indexes that should be added and indexes that should be removed
- c) Eliminates the need for any query execution plans
- d) Stops the database from ever updating statistics

### Explanation

Automated tuning identifies and fixes problematic plans (e.g. restoring better ones after regression) (a) and recommends adding/removing indexes (b). It does not eliminate execution plans or stop statistics updates; it relies on learning the SQL workload characteristics.
