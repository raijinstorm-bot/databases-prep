---
id: "q-gen-relational-databases-16"
exam: ""
number: 16
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["relational-databases"]
---

A table Order has primary key (customer_id, order_id) and also contains customer_city and customer_country. Which normal form does this violate, and why?

- a) 1NF, because the table contains repeating attributes
- b) 2NF, because customer_city depends only on part of the primary key (customer_id)
- c) 3NF, because customer_city depends on another non-key attribute
- d) 4NF, because of a multivalued dependency

### Explanation

This is the presentation's 2NF counter-example: customer_city and customer_country depend only on customer_id, which is part of the composite primary key, not the whole key. Partial dependence on the key violates 2NF; 3NF concerns dependencies between non-key attributes and 4NF concerns multivalued dependencies.
