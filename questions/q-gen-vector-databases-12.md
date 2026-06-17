---
id: "q-gen-vector-databases-12"
exam: ""
number: 12
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["c"]
pdfs: ["vector-databases"]
---

In the presentation's text-querying example, cosine similarity is computed from cosine distance using which expression?

- a) `embedding <-> %s::vector`
- b) `embedding <=> %s::vector`
- c) `1 - (embedding <=> %s::vector)`
- d) `1 / (embedding <-> %s::vector)`

### Explanation

The presentation's query selects `1 - (embedding <=> %s::vector) AS cosine_similarity`, converting cosine distance into cosine similarity. The bare `<=>` operator returns the distance, not the similarity, and the other expressions are not used.
