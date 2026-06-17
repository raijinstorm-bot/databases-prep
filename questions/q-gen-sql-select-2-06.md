---
id: "q-gen-sql-select-2-06"
exam: ""
number: 06
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["sql-select-2"]
---

In the query below, for what scope are the aggregate values computed?

```sql
SELECT Customer_ID,
       COUNT(*) AS order_count,
       SUM(order_value) AS total_order_value
FROM Orders
GROUP BY Customer_ID
```

- a) Over the whole `Orders` table as a single group
- b) Per individual order row
- c) Independently for every group of records sharing the same `Customer_ID`
- d) Only for the customer with the most orders

### Explanation

The GROUP BY example states that all aggregate function values are calculated for every group of records with the same `Customer_ID` independently, producing one output row per customer.
