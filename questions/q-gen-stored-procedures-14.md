---
id: "q-gen-stored-procedures-14"
exam: ""
number: 14
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["stored-procedures"]
---

In the trigger syntax `CREATE TRIGGER TriggerName ON TableName {AFTER|INSTEAD OF} {INSERT,UPDATE,DELETE} AS TriggerCode`, what does the `ON TableName` clause specify?

- a) The schema in which the trigger code is compiled
- b) The table the trigger is associated with and whose modifications activate it
- c) The output parameter that the trigger returns
- d) The execution plan to be reused

### Explanation

The `ON TableName` clause binds the trigger to a specific table, so modifications to that table activate the trigger (b). It does not designate a schema, output parameter, or execution plan.
