---
id: "q-gen-indexes-08"
exam: ""
number: 08
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["indexes"]
---

An index key is defined as `Country, City, Street, Address`. Which use is this index well suited to support?

- a) Filtering only by Address with no other column
- b) Sorting the customers by Country, City, Street, Address
- c) Speeding up inserts into the table
- d) Reducing the disk space used by the table

### Explanation

An index on Country, City, Street, Address can be used to sort customers in that order (and to filter by leading columns such as Country). It does not speed up inserts (indexes add write overhead) or reduce table disk space, and a trailing column like Address alone is not efficiently served by this key.
