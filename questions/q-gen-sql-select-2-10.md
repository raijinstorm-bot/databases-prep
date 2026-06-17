---
id: "q-gen-sql-select-2-10"
exam: ""
number: 10
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["sql-select-2"]
---

With `GROUP BY Customer_ID, Delivery_City`, for which scope is each aggregate computed?

```sql
SELECT Customer_ID, Delivery_City,
       COUNT(*) AS order_count,
       SUM(order_value) AS total_order_value
FROM Orders
GROUP BY Customer_ID, Delivery_City
```

- a) For each `Customer_ID` only, ignoring city
- b) For each `Delivery_City` only, ignoring customer
- c) For each distinct combination of `Customer_ID` and `Delivery_City`
- d) Over the entire table as one group

### Explanation

The multiple-column GROUP BY slide states the aggregates are calculated for each group of records with the same Customer_ID and Delivery_City, i.e. for each distinct combination of the two grouping columns.
