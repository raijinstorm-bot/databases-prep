---
id: "q-gen-sql-select-2-16"
exam: ""
number: 16
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["sql-select-2"]
---

The presentation describes a view as:

```sql
CREATE VIEW TotalSale AS
SELECT Customer_ID, COUNT(*) AS order_count,
       SUM(order_value) AS total_order_value
FROM Orders GROUP BY Customer_ID
```

What is a view, according to the presentation?

- a) A physical copy of the query's result, refreshed nightly
- b) A renamed table stored separately on disk
- c) A saved query that can be used in further queries like a standard table
- d) An index over the grouping columns

### Explanation

The Views slide states a view can be treated as a saved query, and after defining it, it can be used in queries just like a standard table (though performance may be degraded).
