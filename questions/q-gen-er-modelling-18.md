---
id: "q-gen-er-modelling-18"
exam: ""
number: 18
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["er-modelling"]
---

The presentation states that vague relationship labels such as "have" or "are associated with" should be avoided because:

- a) They make the diagram render incorrectly in CASE tools
- b) They make the meaning unclear (e.g. "have parts" could mean spare parts or composed-of parts)
- c) They are reserved keywords in SQL
- d) They prevent generating CREATE TABLE statements

### Explanation

The presentation argues that a good data model yields precision, with unambiguous symbols and terms. A vague label like "have" leaves the meaning unclear ("have spare parts?", "are composed of parts?"), so such labels should be avoided in favour of precise ones like "is composed of."
