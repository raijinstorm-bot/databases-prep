---
id: "q-gen-sql-select-2-05"
exam: ""
number: 05
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["sql-select-2"]
---

Consider the "trivial example" query:

```sql
SELECT COUNT(*) AS order_count,
       SUM(order_value) AS total_order_value
FROM Orders
WHERE ShipCountry = 'France'
```

How many rows does this query return?

- a) One row per order in France
- b) Exactly one row, with the count and total for French orders
- c) One row per distinct `order_value`
- d) Zero rows, because there is no `GROUP BY`

### Explanation

With aggregate functions and no GROUP BY, first the rows matching the WHERE condition are found, then a single row of results is returned. The slide explicitly shows one result row (e.g. 42 / 37890).
