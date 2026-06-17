---
id: "q-gen-sql-select-2-18"
exam: ""
number: 18
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["sql-select-2"]
---

After creating the `TotalSale` view, the query `SELECT * FROM TotalSale WHERE total_order_value < 250` is run. According to the presentation, what does the DBMS use to answer it?

- a) Data permanently stored inside the view
- b) Current data from the underlying `Orders` table, via the saved query
- c) A cached snapshot taken at view creation time
- d) Only the rows that existed when the view was created

### Explanation

The Views guidelines slide states that every time a query referring to a view is submitted, the data from the underlying tables are used by the DBMS to answer the query, because views do not store data by default.
