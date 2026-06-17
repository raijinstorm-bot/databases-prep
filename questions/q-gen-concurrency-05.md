---
id: "q-gen-concurrency-05"
exam: ""
number: 05
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["concurrency"]
---

In the Account 456 example without locking, Transaction A adds 500 then rolls back while Transaction B subtracts 100. What wrong final balance results, and why?

- a) 900 USD, which is correct
- b) 1500 USD, because the rollback was ignored
- c) 1400 USD instead of 900 USD, because A's uncommitted change affected B
- d) 1000 USD, because both transactions cancelled out

### Explanation

The slide shows the balance ending at 1400 USD instead of the correct 900 USD, because Transaction A's update (+500) influenced Transaction B's computation before A rolled back. The correct isolated result would have been 1000 - 100 = 900.
