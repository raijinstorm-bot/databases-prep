---
id: "q-gen-relational-databases-19"
exam: ""
number: 19
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b", "d"]
pdfs: ["relational-databases"]
---

Once a foreign key constraint is enforced, which operations will the DBMS reject to preserve referential integrity?

- a) Inserting a record into the foreign-key table referring to a non-existing record in the primary-key table
- b) Removing a record from the primary-key table that is referenced by a foreign-key table
- c) Inserting a record into the primary-key table that is not yet referenced anywhere
- d) Modifying a primary or foreign key value so the foreign key would point to a non-existing record

### Explanation

The presentation lists the operations a DBMS will reject: inserting an orphan reference, deleting a referenced primary-key record, and modifying key values that would create a dangling reference. Inserting a primary-key record that nobody references yet is perfectly valid and is not rejected.
