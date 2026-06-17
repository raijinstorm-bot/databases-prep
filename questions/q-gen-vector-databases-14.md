---
id: "q-gen-vector-databases-14"
exam: ""
number: 14
type: "single"
generated: true
tags: ["AI-generated"]
correct: ["b"]
pdfs: ["vector-databases"]
---

In the example, the table is created with `CREATE TABLE first_items (id serial PRIMARY KEY, embedding vector(3), name varchar(20));`. What does `vector(3)` specify?

- a) That up to 3 rows can be stored
- b) That the embedding column holds a 3-dimensional vector
- c) That 3 separate indexes will be created
- d) That the vector has 3 bytes of precision

### Explanation

In pgvector, `vector(3)` declares a column storing fixed-length 3-dimensional vectors; in the more realistic example the documents table uses `vector(384)` to match the 384-dimensional SBERT embeddings. It does not limit row counts, define indexes, or set byte precision.
