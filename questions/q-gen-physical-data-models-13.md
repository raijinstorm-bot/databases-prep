---
id: "q-gen-physical-data-models-13"
exam: ""
number: 13
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["physical-data-models"]
---

Why might a designer of a physical data model add a redundant column whose value could be calculated from other columns?

- a) Because relational databases require all derived data to be stored
- b) To violate normalisation rules deliberately as a standard
- c) Because recalculating the value each time would be too time-consuming
- d) Because indexes cannot exist without redundant columns

### Explanation

The presentation states redundant columns may be added when computing the value from other columns would be too time-consuming, a performance trade-off. It is not required by relational databases, not a goal in itself, and unrelated to indexes existing.
