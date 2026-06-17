---
id: "q-gen-sql-select-2-08"
exam: ""
number: 08
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["d"]
pdfs: ["sql-select-2"]
---

The following query is rejected according to the presentation. Why?

```sql
SELECT customer_id, delivery_city, …
FROM …
GROUP BY customer_id
```

- a) `GROUP BY` cannot be used with text columns
- b) `delivery_city` must be wrapped in `COUNT()`
- c) The `FROM` clause is incomplete, which is the only issue
- d) `delivery_city` is not in `GROUP BY`, and there may be many cities per customer, so which one to show is ambiguous

### Explanation

The GROUP BY discussion slide states only columns used in GROUP BY can appear in the SELECT list, because a non-grouped column (like delivery_city) may have many values per group, making the single output value ambiguous.
