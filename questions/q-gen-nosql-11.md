---
id: "q-gen-nosql-11"
exam: ""
number: 11
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["nosql"]
---

What does the lecture mean by an "implicit schema" in a schemaless data store?

- a) A schema that is formally declared to the DBMS before any data is written
- b) The data structure expected by the client application, even though no schema is reported to the DBMS
- c) A schema automatically inferred and enforced by the DBMS engine
- d) The absence of any assumptions about data structure whatsoever

### Explanation

Even without an explicit schema reported to the DBMS, the client application assumes a structure (e.g. that a column holds net income); this expected structure is the implicit schema (b). It is not declared to or enforced by the DBMS (a, c), and assumptions do exist (d is false).
