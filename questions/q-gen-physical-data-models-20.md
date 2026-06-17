---
id: "q-gen-physical-data-models-20"
exam: ""
number: 20
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["physical-data-models"]
---

The presentation describes the ANSI_NULLS setting in MS SQL Server. When ANSI_NULLS is ON, how is a comparison of the form `ColumnName = NULL` treated?

- a) Rows with NULL in ColumnName match the condition
- b) Rows with NULL values in ColumnName do not match the condition
- c) The query is rejected with a syntax error
- d) All rows match regardless of the column value

### Explanation

With ANSI_NULLS ON, rows with NULL in the column do not match `ColumnName = NULL`; setting ANSI_NULLS OFF changes this behaviour so such rows can match. The comparison is not a syntax error and does not match all rows.
