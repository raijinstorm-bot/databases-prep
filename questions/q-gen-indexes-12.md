---
id: "q-gen-indexes-12"
exam: ""
number: 12
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["indexes"]
---

A column `study_type` takes only two values: 'Bachelor of Science' and 'Master Of Science'. Why is indexing this column generally a poor idea?

- a) Two-value columns cannot be indexed by any DBMS
- b) It has very poor selectivity, so the DBMS is unlikely to use the index yet must still maintain it
- c) Indexes can only be created on numeric columns
- d) It would force the table to become a clustered table

### Explanation

A column with only two values has very poor selectivity — on average it filters out only half the records, so the DBMS is unlikely to use the index yet still has to update it, possibly increasing processing time. The other claims are not true.
