---
id: "q-gen-er-modelling-17"
exam: ""
number: 17
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["er-modelling"]
---

When a many-to-many relationship is moved from a conceptual model into a physical model for an RDBMS, the presentation recommends:

- a) Removing the relationship entirely
- b) Storing both sides as a list inside one column
- c) Adding an extra (associative) entity corresponding to an additional table with foreign keys to both original tables
- d) Making one side a surrogate key only

### Explanation

The presentation states that a many-to-many relationship (with "at most many" on both ends) is allowed in conceptual models but, for an RDBMS physical model, must be extended with an extra entity. That associative entity (e.g. VENDOR_PRODUCTS) becomes a table holding foreign keys to both original tables.
