---
id: "q-gen-stored-procedures-07"
exam: ""
number: 07
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["d"]
pdfs: ["stored-procedures"]
---

In the sample `CalculateOrderCount` procedure, what mechanism is used to iterate over the customers of a given country one by one?

- a) A recursive function call
- b) A WHILE loop driven by a GROUP BY clause
- c) An INSTEAD OF trigger
- d) A CURSOR with FETCH NEXT in a WHILE @@FETCH_STATUS = 0 loop

### Explanation

The sample declares a CURSOR, opens it, and repeatedly FETCHes the next customer while `@@FETCH_STATUS = 0`, updating each customer's OrderCount (d). The procedure uses no recursion, GROUP-BY-driven loop, or trigger.
