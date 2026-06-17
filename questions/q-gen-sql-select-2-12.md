---
id: "q-gen-sql-select-2-12"
exam: ""
number: 12
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["sql-select-2"]
---

Given the grouped data for customer MAIN (Poznań total 100.00, Warszawa total 220.00) and the condition `HAVING SUM(order_value) > 150`, which rows remain?

```sql
GROUP BY Customer_ID, Delivery_City
HAVING SUM(order_value) > 150
```

- a) Both the Poznań and Warszawa rows
- b) Only the Poznań row
- c) Only the Warszawa row
- d) Neither row

### Explanation

The HAVING interpretation slide shows the Poznań group (total 100.00) fails `SUM(order_value)>150` and is removed, while the Warszawa group (total 220.00) satisfies it and is kept.
