---
id: "q-gen-oracle-storage-backup-07"
exam: ""
number: 07
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b", "d"]
pdfs: ["oracle-storage-backup"]
---

Which statements about Oracle logical vs. physical storage are correct?

- a) The data of many tables may reside in one file
- b) The data of one table may reside in many files
- c) A logical table can only ever map to exactly one datafile
- d) Logical structures such as tables and indexes are independent from physical structures such as files

### Explanation

Logical and physical structures are managed largely independently: a single file can hold data from many tables (a), and one table's data can be spread across many files (b, d). Therefore the one-to-one mapping in (c) is false.
