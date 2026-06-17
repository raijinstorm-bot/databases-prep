---
id: "q-gen-relational-databases-17"
exam: ""
number: 17
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["relational-databases"]
---

An Order entity contains customer_id, order_id, employee_id, employee_name and employee_email. According to the presentation, what is the problem?

- a) employee_id is non-atomic and violates 1NF
- b) employee_id depends only on part of the primary key, violating 2NF
- c) employee_email depends on the employee rather than on the order, violating 3NF
- d) There is no problem; the table is already in 3NF

### Explanation

This is the presentation's 3NF counter-example. While employee_id relates to the order, attributes such as employee_email are really features of the employee, not the order, so they depend on a non-key attribute. This violates 3NF and causes redundancy and potential inconsistency.
