---
id: "q-gen-physical-data-models-06"
exam: ""
number: 06
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["d"]
pdfs: ["physical-data-models"]
---

Consider the statement: `UPDATE Customers SET City='Cracow' WHERE Country='Poland'`. What is the effect?

- a) It updates exactly one record
- b) It deletes all customers from Poland
- c) It fails because no primary key is referenced
- d) It can update possibly many records matching the condition

### Explanation

A WHERE condition that is not on a primary key can match many rows, so this UPDATE can modify many records at once. It does not delete anything, and an UPDATE does not require a primary key in the condition to be valid.
