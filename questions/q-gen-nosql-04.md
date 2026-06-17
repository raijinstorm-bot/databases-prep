---
id: "q-gen-nosql-04"
exam: ""
number: 04
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["nosql"]
---

In the asset inventory example with 30 types of assets, what limitation of the relational approach is highlighted?

- a) Relational databases cannot store more than 30 tables
- b) Adding new asset types may require adding more tables or forcing generic columns like NumberFeature1
- c) Relational databases cannot enforce referential integrity for assets
- d) Each asset type requires its own separate database instance

### Explanation

The example shows two awkward RDBMS options: 30 tables (requiring new tables for new types) or one table with generic columns such as NumberFeature1 reused across very different assets (b). This motivates NoSQL's flexible, schemaless model. The other statements are not claims made in the lecture.
