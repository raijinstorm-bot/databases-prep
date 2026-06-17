---
id: "q-gen-oracle-security-18"
exam: ""
number: 18
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "b"]
pdfs: ["oracle-security"]
---

Which statements about trigger-based (value-based) auditing are correct?

- a) It offers the greatest flexibility for tracking the actual values inserted into or used to update a table
- b) It will not help when SQL SELECT statements have to be monitored
- c) It is the recommended way to monitor read access to confidential data
- d) It has no impact on database performance

### Explanation

Trigger-based auditing gives the greatest flexibility for capturing the actual values used in inserts/updates (a), but triggers do not fire on SELECT, so it cannot monitor reads (b). It is therefore not suited to monitoring read access (c), and it may negatively affect performance (d is false).
