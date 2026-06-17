---
id: "q-gen-concurrency-20"
exam: ""
number: 20
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "c", "d"]
pdfs: ["concurrency"]
---

According to the presentation's discussion of transaction execution time, which statements are correct?

- a) A typical (standard) transaction takes less than a second to complete
- b) Long-running transactions should rely on locks to protect data for many days
- c) Long-running transactions instead create a logical copy of the modified data
- d) Standard transactions should be kept short so as not to decrease throughput

### Explanation

Standard transactions impose locks, so they should be short (typically under a second) to preserve throughput. Long-running transactions cannot be lock-based, as that would block work (e.g. read-only access) for days; instead a logical copy of the modified data is created. Thus b is false.
