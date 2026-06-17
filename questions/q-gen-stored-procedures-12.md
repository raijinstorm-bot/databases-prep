---
id: "q-gen-stored-procedures-12"
exam: ""
number: 12
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["stored-procedures"]
---

What distinguishes an INSTEAD OF trigger from an AFTER trigger, per the lecture?

- a) INSTEAD OF triggers can only be defined on functions
- b) AFTER triggers replace the original action, while INSTEAD OF triggers run before it
- c) AFTER triggers run after the action completes, while INSTEAD OF triggers run in place of the original action
- d) Both run only when no rows are affected

### Explanation

The lecture states AFTER triggers are called after an action (e.g. after a record is inserted), whereas INSTEAD OF triggers are called instead of the original action they are defined for (c). Option b reverses these roles.
