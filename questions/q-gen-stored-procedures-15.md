---
id: "q-gen-stored-procedures-15"
exam: ""
number: 15
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["stored-procedures"]
---

The example trigger `InsertOrder` uses `SET @customer = (SELECT CustomerId FROM inserted)`. What assumption does the lecture explicitly note about this code?

- a) That the Orders table has no primary key
- b) That the trigger is an INSTEAD OF trigger
- c) That only one order is inserted by the INSERT statement
- d) That OrderCount is recomputed from scratch every time

### Explanation

The lecture notes the code assumes one order is inserted per INSERT statement, warning that multiple rows can be inserted at once via INSERT ... SELECT (c). The trigger is AFTER INSERT and increments OrderCount rather than recomputing it.
