---
id: "q-gen-oracle-storage-backup-20"
exam: ""
number: 20
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["oracle-storage-backup"]
---

What is the effect of setting `fast_start_mttr_target` to a very low value such as a few seconds?

- a) It has no effect on performance at all
- b) It can largely degrade instance performance because much time is spent writing dirty blocks to disk
- c) It guarantees the instance can never be recovered
- d) It disables ARCHIVELOG mode

### Explanation

A very low fast_start_mttr_target forces very frequent checkpoints, so a lot of instance time is spent writing dirty blocks to disk, degrading performance. The default of zero maximises performance at the cost of potentially long recovery; the parameter does not disable archiving or prevent recovery.
