---
id: "q-gen-sql-select-2-13"
exam: ""
number: 13
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "c"]
pdfs: ["sql-select-2"]
---

According to the slide on NULL values and comparisons, which statements are correct?

- a) To test for NULL one should use `Column_Name IS [NOT] NULL`
- b) NULL can be reliably compared using `Column_Name = NULL`
- c) `MIN()`, `MAX()` and `SUM()` can produce non-obvious results when NULLs appear in the aggregated expression
- d) Aggregate functions always treat NULL as zero

### Explanation

The slide instructs using `IS [NOT] NULL` for NULL comparisons (not `= NULL`) and warns that MIN/MAX/SUM may yield non-obvious results with NULLs in the expression. It does not state NULL is universally treated as zero.
