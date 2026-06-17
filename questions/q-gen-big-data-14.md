---
id: "q-gen-big-data-14"
exam: ""
number: 14
type: "multi"
generated: true
tags: ["AI-generated"]
correct: ["a", "c"]
pdfs: ["big-data"]
---

Comparing the RDBMS shared-disk approach with the sharding approach, which statements are correct?

- a) The RDBMS shared-disk approach ensures referential integrity but incurs significant communication overhead
- b) The sharding approach typically guarantees referential integrity
- c) The sharding approach reduces communication overhead and can scale to hundreds or thousands of servers
- d) Shared-disk installations of 1000 servers are common, with 50 being small
- e) Sharding cannot scale beyond about 10 servers

### Explanation

Shared-disk RDBMS ensures referential integrity at the cost of communication overhead and uses few servers (50 is large) (a). Sharding usually offers no referential integrity (b false), reduces overhead, and scales to 100s-1000s of servers (c), well beyond 10 (e false); 1000-server shared-disk setups are not typical (d false).
