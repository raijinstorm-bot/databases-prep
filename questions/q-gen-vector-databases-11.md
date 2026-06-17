---
id: "q-gen-vector-databases-11"
exam: ""
number: 11
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["vector-databases"]
---

In the pgvector example, which SQL clause is used to return the rows whose vectors are closest to a query vector?

- a) `WHERE embedding = '[3,2,2.5]'`
- b) `ORDER BY embedding <-> '[3,2,2.5]' LIMIT 2`
- c) `GROUP BY embedding HAVING distance < 1`
- d) `JOIN vectors ON embedding NEAR '[3,2,2.5]'`

### Explanation

The presentation queries similar vectors with `SELECT * FROM first_items ORDER BY embedding <-> '[3,2,2.5]' LIMIT 2`, ordering by the distance operator and limiting the number of rows. Exact equality, GROUP BY/HAVING, and a NEAR join operator are not used for similarity search.
