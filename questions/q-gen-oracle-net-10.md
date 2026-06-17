---
id: "q-gen-oracle-net-10"
exam: ""
number: 10
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["oracle-net"]
---

What happens to connections when the listener process is terminated?

- a) All existing connections are immediately dropped
- b) New remote connections cannot be established, but already established connections continue to be handled
- c) Both new and existing connections continue to work normally
- d) The instance is automatically shut down

### Explanation

When a listener is terminated, no new remote connections can be established, but connections already set up will continue to be handled, because the listener only brokers the initial connection. Terminating the listener does not affect existing sessions or shut down the instance.
