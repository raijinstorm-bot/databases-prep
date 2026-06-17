---
id: "q-gen-relational-databases-18"
exam: ""
number: 18
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["relational-databases"]
---

Why is redundancy (e.g. repeating a customer's address in many order records) considered a problem?

- a) It always makes queries impossible to execute
- b) It may cause inconsistency if the value is updated in only some of the records
- c) It violates the definition of a primary key
- d) It prevents foreign keys from being defined

### Explanation

The presentation explains that redundancy may cause inconsistency: for example, if a customer's address is updated in only one of many order records, the records disagree. This is the motivation behind 2NF and 3NF decomposition. Redundancy does not by itself block queries, keys, or foreign keys.
