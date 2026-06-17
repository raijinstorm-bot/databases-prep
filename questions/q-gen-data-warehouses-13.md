---
id: "q-gen-data-warehouses-13"
exam: ""
number: 13
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["data-warehouses"]
---

A defining characteristic of a star schema is that:

- a) dimension tables refer to many other dimension tables
- b) there is no central fact table
- c) a fact table is surrounded by dimension tables that do not refer to other tables
- d) all tables are fully normalised

### Explanation

In a star schema a central fact table is surrounded by dimension tables, and those dimension tables do not refer to other tables (c). Dimensions referencing further tables would indicate a snowflake, not a star; and star schemas are typically denormalised.
