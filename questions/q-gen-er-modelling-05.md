---
id: "q-gen-er-modelling-05"
exam: ""
number: 05
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["er-modelling"]
---

Why does the presentation say referential integrity is "absolutely necessary" when a surrogate primary key is used?

- a) Because surrogate keys are never unique
- b) Because surrogate keys cannot be indexed
- c) Because if a referenced record (e.g. room_id 23215) were removed, nothing meaningful would be known from the surrogate value alone (e.g. the location of an asset)
- d) Because surrogate keys must always allow NULL

### Explanation

The presentation argues that with surrogate keys the foreign key value carries no real-world meaning, so if the referenced row were deleted (e.g. room_id=23215), nothing would be known about the asset's location. Referential integrity therefore must prevent such dangling references.
