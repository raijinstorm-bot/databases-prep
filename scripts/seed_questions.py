#!/usr/bin/env python3
"""
One-time seed: writes one Markdown file per question into questions/.
Each file has YAML frontmatter (machine-readable) + body (human-readable).
Answers / explanations / exam tags authored by hand.
The `pdfs` field is left empty here and filled in later by the
presentation-tagging pass. After this runs, the .md files are the source
of truth; scripts/build.py compiles them into the website data.
"""
import os, textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "questions")
os.makedirs(OUT, exist_ok=True)

# exam tag display labels live in scripts/build.py / exams metadata.
# Q = (exam_tag, number, type, stem, options[(letter,text)], correct[letters], explanation)
Q = []

def add(exam, num, typ, stem, options, correct, explanation):
    Q.append(dict(exam=exam, num=num, typ=typ, stem=stem.strip(),
                  options=options, correct=correct, explanation=explanation.strip()))

# ---------------------------------------------------------------------------
# EXAM 2023-1
# ---------------------------------------------------------------------------
E = "2023-1"
add(E, 1, "single",
    "Based on the result of an SQL `SELECT` query on tables containing 7 million records, 50 rows are obtained. The most efficient further processing of these rows should be expected when:",
    [("a","The result is repeatedly selected directly from the original 7-million-row tables"),
     ("b","The result is placed in a temporary table and further processing uses this table"),
     ("c","The result is processed only through a view"),
     ("d","The result is exported to a text file before processing")],
    ["b"],
    "Materialising the 50 rows into a temporary table lets later steps work on a tiny set instead of re-scanning the 7-million-row source tables each time. A view (c) re-runs the underlying query against the large tables, and (a)/(d) are clearly worse.")

add(E, 2, "single",
    "Creating a view with `CREATE VIEW testView AS SELECT * FROM Orders` causes:",
    [("a","A physical copy of the `Orders` table to be created"),
     ("b","The data from `Orders` to be permanently stored inside the view"),
     ("c","The definition of the view to be saved, and queries on the view use current data from `Orders`"),
     ("d","The `Orders` table to be replaced by `testView`")],
    ["c"],
    "A standard (non-materialised) view stores only its query definition; querying it executes that definition against the current base-table data. No data is copied or stored in the view itself.")

add(E, 3, "single",
    "Transaction A executes an SQL `UPDATE` command on a record. If transaction A encounters a lock established by transaction B modifying the same record:",
    [("a","Transaction A automatically cancels transaction B"),
     ("b","Transaction A ignores the lock and updates the record"),
     ("c","Transaction A must wait until transaction B finishes with `ROLLBACK` or `COMMIT`"),
     ("d","Transaction A always receives an error immediately")],
    ["c"],
    "A write lock blocks conflicting writers: A is suspended until B releases the lock by committing or rolling back. It does not cancel B, ignore the lock, or fail immediately (timeouts aside).")

add(E, 4, "single",
    "Normalizing a table to third normal form:",
    [("a","Requires, among other things, identifying the primary key"),
     ("b","Requires removing all indexes"),
     ("c","Requires deleting all foreign keys"),
     ("d","Requires replacing all tables with views")],
    ["a"],
    "Normalisation is about functional dependencies and keys; identifying the primary key is a prerequisite. It has nothing to do with deleting indexes, foreign keys, or using views.")

add(E, 5, "single",
    "The result of comparing `'abc' = NULL` is:",
    [("a","`TRUE`"),("b","`FALSE`"),("c","`0`"),("d","An empty string")],
    ["b"],
    "Under SQL three-valued logic any comparison with NULL yields UNKNOWN, never TRUE. None of the options is literally UNKNOWN; since the predicate is not true, a row would not be returned, so among the offered choices it behaves as FALSE.")

add(E, 6, "single",
    "The result of comparing `'abc' > NULL` is:",
    [("a","`TRUE`"),("b","`FALSE`"),("c","`1`"),("d","`'abc'`")],
    ["b"],
    "As with `=`, ordering comparisons against NULL evaluate to UNKNOWN (not true). The condition is not satisfied, so among the offered options it behaves as FALSE.")

add(E, 7, "single",
    "Normalizing a table to first normal form:",
    [("a","Requires, among other things, identifying the primary key"),
     ("b","Requires creating triggers"),
     ("c","Requires creating stored procedures"),
     ("d","Requires removing all constraints")],
    ["a"],
    "1NF requires atomic values and a key to identify each row; identifying the primary key is part of it. Triggers, stored procedures and removing constraints are unrelated.")

add(E, 8, "single",
    "Statistics stored in an Oracle database:",
    [("a","Should not be used because they slow down all queries"),
     ("b","Should be used because they help prepare better query execution plans"),
     ("c","Replace the need for indexes"),
     ("d","Replace transaction logs")],
    ["b"],
    "The cost-based optimiser uses table/column statistics (row counts, distribution, selectivity) to choose efficient execution plans. Statistics neither replace indexes nor transaction logs.")

add(E, 9, "multi",
    "Oracle database audit options allow:",
    [("a","Monitoring the use of individual SQL commands"),
     ("b","Monitoring successful connection attempts to an instance"),
     ("c","Monitoring unsuccessful connection attempts to an instance"),
     ("d","Replacing the process of granting table privileges")],
    ["a","b","c"],
    "Auditing records statement usage and both successful and failed logon attempts. It is a monitoring mechanism and does not replace privilege management (GRANT/REVOKE).")

add(E, 10, "multi",
    "In a database system with unacceptable performance for a frequently executed sequence of complex SQL `SELECT` queries, potentially beneficial actions include:",
    [("a","Adding new indexes"),
     ("b","Introducing a stored procedure and placing the SQL `SELECT` query code inside it"),
     ("c","Removing all primary keys"),
     ("d","Disabling statistics permanently")],
    ["a","b"],
    "Suitable indexes avoid full scans, and wrapping the queries in a stored procedure allows plan reuse and fewer round-trips. Removing primary keys and disabling statistics would hurt performance.")

add(E, 11, "multi",
    "In an Oracle database:",
    [("a","One connection may be handled by a permanently assigned server process"),
     ("b","One connection may be handled by a server process that also alternately handles other connections"),
     ("c","Backups and batch operations should be performed by a dedicated server process"),
     ("d","Every connection must always have its own listener process")],
    ["a","b","c"],
    "Dedicated server = one process per connection (a); shared server = processes rotate among connections (b); long-running batch/backup work is recommended to use a dedicated server (c). The listener only brokers new connections and is not per-connection (d).")

add(E, 12, "single",
    "The query `SELECT * FROM Customers WHERE EXISTS (SELECT * FROM Orders WHERE YEAR(OrderDate) = 1997)` is used to determine customers who placed orders in 1997. This query:",
    [("a","Correctly returns only customers who placed orders in 1997"),
     ("b","Does not correctly determine the customers satisfying the condition"),
     ("c","Returns no rows in every case"),
     ("d","Deletes customers without orders")],
    ["b"],
    "The subquery is not correlated to the outer Customers row, so EXISTS is true for every customer as long as *any* 1997 order exists — returning all customers. A correct version must correlate Orders to the current customer.")

add(E, 13, "multi",
    "Establishing a new network connection to an Oracle database:",
    [("a","Typically uses TCP/IP and port 1521"),
     ("b","Requires the presence of a listener process"),
     ("c","May automatically refer to different listener processes for fault tolerance"),
     ("d","Always requires manual copying of database files")],
    ["a","b","c"],
    "Oracle Net commonly uses TCP/IP on port 1521 and needs a running listener to broker the connection; client configuration can list several listeners for failover/HA. Copying database files is unrelated to connecting.")

add(E, 14, "single",
    "In a thick-client application running on 500 workstations and communicating directly with an Oracle database server, the recommended connection method is:",
    [("a","Dedicated server processes only"),
     ("b","Shared server processes"),
     ("c","No listener process"),
     ("d","A separate database for each workstation")],
    ["b"],
    "With many concurrent, often-idle client sessions, shared server processes conserve memory and server resources by multiplexing connections, whereas a dedicated process per connection would not scale well to 500 clients.")

add(E, 15, "single",
    "In the case of the `ROLLBACK` command:",
    [("a","Changes made in the current transaction are undone"),
     ("b","All database tables are deleted"),
     ("c","The transaction is permanently saved"),
     ("d","Indexes are rebuilt")],
    ["a"],
    "ROLLBACK discards all uncommitted changes of the current transaction, returning the data to its state before the transaction began.")

add(E, 16, "multi",
    "When using `READ UNCOMMITTED`, there is a risk of:",
    [("a","Dirty reads"),
     ("b","Deadlocks"),
     ("c","Non-repeatable reads"),
     ("d","Complete prevention of all concurrency issues")],
    ["a","c"],
    "READ UNCOMMITTED is the weakest isolation level: it permits dirty reads, and also non-repeatable reads and phantoms. It certainly does not prevent all anomalies (d).")

add(E, 17, "single",
    "The number of rows in the result of `SELECT * FROM TableA JOIN TableB ON 7 = 3 OR 7 > 1` will be equal to:",
    [("a","0"),
     ("b","The number of rows in `TableA`"),
     ("c","The number of rows in `TableB`"),
     ("d","The product of the number of rows in `TableA` and `TableB`")],
    ["d"],
    "The join condition `7=3 OR 7>1` is always TRUE, so every row of A matches every row of B — a Cartesian product of size |A| × |B|.")

add(E, 18, "multi",
    "The value `NULL` is:",
    [("a","A value indicating the absence of a date in a date-type field"),
     ("b","A value that should be allowed only when necessary"),
     ("c","Always equal to zero"),
     ("d","Always equal to an empty string")],
    ["a","b"],
    "NULL marks a missing/unknown value (e.g. an absent date) and should be permitted only where genuinely needed. It is not equal to zero or to an empty string — in fact it is not equal to anything.")

add(E, 19, "multi",
    "Layers in geographic information systems are divided into:",
    [("a","Raster layers"),
     ("b","Vector layers"),
     ("c","Transaction layers"),
     ("d","SQL layers")],
    ["a","b"],
    "GIS data is organised into raster layers (grids of cells, e.g. imagery) and vector layers (points, lines, polygons). 'Transaction' and 'SQL' layers are not GIS layer types.")

add(E, 20, "multi",
    "In a data cube, there is typically:",
    [("a","A time-type dimension"),
     ("b","A numeric measure such as sum"),
     ("c","Many dimensions"),
     ("d","Only one table without dimensions")],
    ["a","b","c"],
    "An OLAP cube has multiple dimensions (commonly including time) along which numeric measures (sums, counts, etc.) are aggregated. A single dimensionless table is the opposite of a cube.")

add(E, 21, "single",
    "In each row of a table, the list of used columns is different. It is also possible to insert a row with any new column names. This means the table was created:",
    [("a","In a relational system with strict schema"),
     ("b","In a NoSQL system"),
     ("c","Only in Oracle Database"),
     ("d","Only in MS SQL Server")],
    ["b"],
    "Per-row, flexible/dynamic columns are characteristic of schema-less NoSQL stores (e.g. wide-column or document databases). A strict relational schema fixes the columns for all rows.")

add(E, 22, "multi",
    "ER diagrams:",
    [("a","Contain entities"),
     ("b","Contain relationships"),
     ("c","Describe the meaning of relationships"),
     ("d","Contain only SQL queries")],
    ["a","b","c"],
    "Entity-Relationship diagrams model entities, the relationships between them, and the semantics/cardinality of those relationships. They are a conceptual model, not SQL.")

add(E, 23, "single",
    "A one-to-many relationship between table A and table B is represented by:",
    [("a","An additional foreign key in table B pointing to table A"),
     ("b","An additional foreign key in table A pointing to table B"),
     ("c","Deleting table B"),
     ("d","Creating a trigger only")],
    ["a"],
    "In a 1:N relationship the foreign key goes on the 'many' side (B), referencing the 'one' side (A). Each B row points to exactly one A row, while one A row can be referenced by many B rows.")

add(E, 24, "single",
    "A many-to-many relationship between table A and table B is represented by:",
    [("a","An additional table C with foreign keys pointing to tables A and B"),
     ("b","A single column with comma-separated values"),
     ("c","Removing primary keys from both tables"),
     ("d","Creating a view only")],
    ["a"],
    "An M:N relationship is resolved with a junction (associative) table C holding foreign keys to both A and B. Comma-separated lists violate atomicity/1NF.")

add(E, 25, "single",
    "Normalizing a table to second normal form:",
    [("a","Aims to eliminate anomalies resulting from redundancy"),
     ("b","According to good practices, may be skipped in OLTP systems"),
     ("c","Requires deleting all tables"),
     ("d","Requires storing all data in one column")],
    ["a"],
    "2NF removes partial dependencies on part of a composite key, reducing redundancy-driven anomalies. Normalisation is especially desirable in OLTP systems, so (b) is wrong.")

add(E, 26, "multi",
    "In Oracle databases:",
    [("a","Writing to transaction logs occurs before the client application receives confirmation of successful transaction completion"),
     ("b","Power failure causes the loss of changes made within a transaction that is still in progress"),
     ("c","Transaction logs are never used"),
     ("d","Transactions cannot be rolled back")],
    ["a","b"],
    "Write-ahead logging means redo is persisted before COMMIT is acknowledged (a). An in-progress, uncommitted transaction is lost on a crash/power failure (b). Logs are central to Oracle and rollback is supported, so (c)/(d) are false.")

add(E, 27, "multi",
    "Network connections to an Oracle database instance:",
    [("a","May automatically try another listener IP address if the primary one does not respond"),
     ("b","May use configuration files defining connection behavior, for example `load_balance`"),
     ("c","Never use TCP/IP"),
     ("d","Always require direct disk access to database files")],
    ["a","b"],
    "Client-side Oracle Net configuration supports failover to alternative listener addresses and options such as `LOAD_BALANCE`. TCP/IP is the usual protocol, and clients never touch the datafiles directly.")

add(E, 28, "multi",
    "Big Data solutions usually use data:",
    [("a","Of significant size, measured for example in bytes"),
     ("b","Of lower quality than in relational databases"),
     ("c","Of diverse forms, such as forum posts or web application logs"),
     ("d","Stored only in one normalized relational table")],
    ["a","b","c"],
    "Big Data is characterised by large volume, varied/less-curated data (lower quality than tightly validated RDBMS data), and many formats such as logs and posts. It is not confined to a single normalised table.")

add(E, 29, "multi",
    "Transaction log files in a transactional system:",
    [("a","Are necessary for the system to operate"),
     ("b","May be archived"),
     ("c","Are used during database recovery after failure"),
     ("d","Are used only for displaying reports")],
    ["a","b","c"],
    "Redo/transaction logs are essential for durability and crash recovery and can be archived for point-in-time recovery. They are not a reporting feature.")

add(E, 30, "single",
    "A database:",
    [("a","May support different national character sets simultaneously"),
     ("b","May use more than one national character set at the same time"),
     ("c","Must always use exactly one character set"),
     ("d","Cannot store multilingual text")],
    ["c"],
    "An Oracle database is created with a single (database) character set; a Unicode set such as AL32UTF8 already stores multilingual text. It does not run several character sets at once, so (a)/(b)/(d) are wrong.")

add(E, 31, "multi",
    "A trigger can:",
    [("a","Execute an SQL `UPDATE` command on another table"),
     ("b","Be executed as a result of data modifications made by different client applications"),
     ("c","Be automatically started after inserting a new record"),
     ("d","Be automatically started instead of inserting a record")],
    ["a","b","c","d"],
    "Triggers run server-side for any client that performs the triggering DML, can modify other tables, fire AFTER an operation, or replace it (INSTEAD OF). All four statements are true.")

add(E, 32, "single",
    "NoSQL-class systems are usually:",
    [("a","Based on a mathematical theory of NoSQL that negates relational theory"),
     ("b","Open-source systems"),
     ("c","Always relational systems"),
     ("d","Always based only on SQL tables")],
    ["b"],
    "Many prominent NoSQL systems are open source. There is no formal 'NoSQL theory'; they are not relational, and they do not rely solely on SQL tables.")

add(E, 33, "single",
    "`CREATE TABLE` commands:",
    [("a","May have different forms in different RDBMS systems, such as Oracle Database and MS SQL Server"),
     ("b","Are identical in every database system"),
     ("c","Can only be used in NoSQL databases"),
     ("d","Always create temporary tables only")],
    ["a"],
    "Although SQL is standardised, DDL details (data types, options, syntax extensions) differ between vendors such as Oracle and SQL Server.")

add(E, 34, "multi",
    "NoSQL solutions include systems storing data as:",
    [("a","Documents"),
     ("b","Graphs"),
     ("c","Rows described by columns that may differ in each row"),
     ("d","Only fully normalized relational tables")],
    ["a","b","c"],
    "NoSQL families include document stores, graph databases, and wide-column stores where each row can have different columns. Fully normalised relational tables are the relational model, not NoSQL.")

add(E, 35, "multi",
    "A polygon-type vector layer object is defined by:",
    [("a","A location in a selected coordinate system, described by vertex coordinates"),
     ("b","Descriptive attributes"),
     ("c","Only transaction logs"),
     ("d","Only SQL indexes")],
    ["a","b"],
    "A vector polygon has geometry (vertex coordinates in a coordinate reference system) plus descriptive (non-spatial) attributes. Transaction logs and indexes are storage mechanisms, not the object's definition.")

add(E, 36, "single",
    "From the point of view of performance for many users in a transactional system such as MS SQL Server, it is recommended to use:",
    [("a","Numerous short-duration transactions"),
     ("b","One very long transaction for all users"),
     ("c","No transactions"),
     ("d","Transactions that never commit")],
    ["a"],
    "Short transactions hold locks briefly, maximising concurrency and throughput. Long-running or never-committing transactions block others and bloat logs.")

add(E, 37, "multi",
    "In a cold-failover cluster:",
    [("a","Before failure, one server participates in SQL query processing"),
     ("b","After failure, at most one server participates in SQL query processing"),
     ("c","All servers always process the same SQL query simultaneously"),
     ("d","No server processes SQL queries before failure")],
    ["a","b"],
    "Cold failover is active/passive: exactly one node serves the database at a time. Before failure one node is active; after failover the standby takes over, so again at most one is active.")

add(E, 38, "multi",
    "Archiving Oracle transaction logs:",
    [("a","Is recommended in production systems"),
     ("b","Allows the database to be restored to any point in time"),
     ("c","Is never used in production"),
     ("d","Deletes all committed transactions")],
    ["a","b"],
    "ARCHIVELOG mode preserves filled redo logs, enabling point-in-time/media recovery and is standard in production. It preserves rather than deletes committed changes.")

add(E, 39, "multi",
    "The `ALTER TABLE` command:",
    [("a","Can change only some table properties"),
     ("b","Can be used to add a column"),
     ("c","Can be used to increase the length of a text column"),
     ("d","Can change absolutely every property of a table")],
    ["a","b","c"],
    "ALTER TABLE can add columns and widen text columns, but only a subset of changes are possible online; some structural changes require recreating the table, so it cannot change 'absolutely every' property.")

add(E, 40, "single",
    "The commands `BEGIN TRANSACTION`, `INSERT`, `UPDATE`, and `COMMIT` were executed successfully, and the server confirmed all commands. In this situation:",
    [("a","Both `INSERT` and `UPDATE` were executed successfully"),
     ("b","Only `INSERT` was executed successfully"),
     ("c","Only `UPDATE` was executed successfully"),
     ("d","Both commands were rolled back")],
    ["a"],
    "A confirmed COMMIT makes all statements in the transaction durable atomically, so both the INSERT and the UPDATE took effect.")

add(E, 41, "single",
    "In an employee database, each employee except the rector must be assigned a current supervisor who is another employee. To do this, one should:",
    [("a","Add a foreign key in the employee table that accepts `NULL`"),
     ("b","Create a separate database for supervisors"),
     ("c","Remove the employee primary key"),
     ("d","Store supervisors only in a text file")],
    ["a"],
    "A self-referencing foreign key (supervisor_id → employee_id) models the recursive relationship; allowing NULL lets the single rector have no supervisor.")

add(E, 43, "multi",
    "A connection pool is a way to:",
    [("a","Reduce server load caused by opening and closing connections"),
     ("b","Improve application performance"),
     ("c","Replace all SQL queries"),
     ("d","Disable transaction processing")],
    ["a","b"],
    "A pool reuses a set of already-open connections, avoiding the cost of repeatedly opening/closing them and improving throughput. It does not replace SQL or disable transactions.")

# ---------------------------------------------------------------------------
# EXAM 2024-A  (test_2024_1; numbering starts at 2 in the source)
# ---------------------------------------------------------------------------
E = "2024-A"
add(E, 2, "open",
    "Please describe the way Apache Hadoop can be used for storing Big Data. Is Apache Hadoop a relational database management system? If not, what are the differences? What has to be specified to store data in Apache Hadoop? (For additional points: explain schema-on-read vs schema-on-write and which yields higher data quality.)",
    [],
    [],
    "Apache Hadoop stores Big Data on **HDFS**, a distributed file system that splits large files into blocks and replicates them across many commodity nodes, providing fault tolerance and horizontal scalability. Processing is done by frameworks (originally MapReduce, later Spark, Hive, etc.) that move computation to the data.\n\nHadoop is **not** an RDBMS. It has no fixed relational schema, no SQL engine by default, no transactions/ACID guarantees, no referential integrity, and no indexes in the relational sense. To store data you essentially specify a **file name/path and a file format** (text, CSV, Avro, Parquet, ORC, …) — you do not predefine tables, columns, and column data types as you would in a relational database.\n\n**Schema-on-write** (relational DBs) validates and structures data against a schema *before* it is stored, so invalid data is rejected at load time. **Schema-on-read** (Hadoop) stores raw data as-is and applies structure only when the data is read/queried. Schema-on-write generally yields **higher data quality**, because constraints and types are enforced up front; schema-on-read trades that quality/validation for flexibility and the ability to ingest diverse, raw data quickly.")

add(E, 3, "multi",
    "A developer wants to run queries finding all buildings located no more than 100 meters from the nearest road, and at least partly contained no further than 500 meters from the nearest power grid line. If so:",
    [("a","a GIS system is needed"),
     ("b","a graph NoSQL platform is needed"),
     ("c","vector layers should be used"),
     ("d","raster layers should be used"),
     ("e","data warehouse will be mandatory")],
    ["a","c"],
    "Distance/proximity queries over discrete features (buildings, roads, power lines) are spatial queries best served by a GIS using vector layers, where geometry has exact coordinates. A graph store, raster layers, and a data warehouse are not required.")

add(E, 4, "single",
    "A one-to-many relation between table A and B:",
    [("a","is represented by a foreign key in table A"),
     ("b","is represented by a foreign key in table B"),
     ("c","is represented by an extra table C with foreign keys pointing from it to tables A and B"),
     ("d","is represented by an extra table C with two candidate keys")],
    ["b"],
    "The foreign key is placed on the 'many' side. Here B is the many side, so B carries a foreign key referencing A. A junction table (c/d) is for many-to-many relationships.")

add(E, 5, "single",
    "The transaction is executed in SERIALIZABLE mode. We expect:",
    [("a","improved performance compared to READ UNCOMMITTED"),
     ("b","dirty reads"),
     ("c","non-repeatable reads"),
     ("d","possibly negative impact on the performance of the other transactions")],
    ["d"],
    "SERIALIZABLE is the strictest isolation level; it prevents dirty and non-repeatable reads but increases locking/contention, which can reduce concurrency and hurt other transactions' performance.")

add(E, 6, "multi",
    "A client application implemented using .NET:",
    [("a","can execute SQL SELECT queries on a remote database"),
     ("b","can execute SQL INSERT statements on a remote database"),
     ("c","can suffer from SQL code injection attempts"),
     ("d","can execute parametrized queries, but this is not recommended"),
     ("e","typically has to concatenate data provided by a user, such as the product name, with the text of the query sent to a database")],
    ["a","b","c"],
    "A .NET client can run SELECT and INSERT against a remote DB and, if it builds SQL by string concatenation, is vulnerable to SQL injection. Parametrized queries are strongly recommended (so d is wrong), and concatenating user input is the unsafe practice to avoid (so e is wrong).")

add(E, 7, "multi",
    "Fact record:",
    [("a","can typically be found in a data warehouse table"),
     ("b","can typically be found in GIS layer"),
     ("c","can typically be found in a NoSQL table"),
     ("d","typically refers to dimension records")],
    ["a","d"],
    "Facts live in the fact table of a dimensional (data-warehouse) model and reference dimension records via foreign keys. They are not a GIS or NoSQL concept.")

add(E, 8, "single",
    "Data warehouse:",
    [("a","typically relies on data retrieved from NoSQL platform(s)"),
     ("b","typically relies on data retrieved from RDBMS platforms"),
     ("c","is nowadays replaced with Big Data platforms such as Apache Hadoop"),
     ("d","is nowadays replaced with NoSQL platforms, especially MongoDB, as MongoDB provides a higher quality of data")],
    ["b"],
    "Data warehouses are typically populated by ETL from operational RDBMS source systems. They are not replaced by Hadoop or MongoDB; those serve different needs.")

add(E, 9, "multi",
    "Big Data is defined as:",
    [("a","high value data"),
     ("b","high quality data"),
     ("c","high quantity data"),
     ("d","high velocity data"),
     ("e","high volume data")],
    ["d","e"],
    "The classic 'Vs' of Big Data are Volume and Velocity (and Variety). Volume (e) and Velocity (d) are the textbook defining characteristics here; Big Data is not defined by high quality, and 'value' is a later add-on rather than a defining characteristic.")

add(E, 10, "open",
    "Please describe what a data warehouse is and how data in a data warehouse is created. (For additional points: clarify the difference between fact and dimension tables.)",
    [],
    [],
    "A **data warehouse** is a central, subject-oriented, integrated, historical repository built for analysis and reporting (OLAP/Business Intelligence) rather than transaction processing. It consolidates data from many operational source systems into a consistent model optimised for querying and aggregation.\n\nData is created through an **ETL** process: data is **Extracted** from source databases, **Transformed** (cleansed, integrated, conformed to common definitions, often denormalised), and **Loaded** into the warehouse — typically on a periodic schedule. The warehouse usually uses a dimensional design (star/snowflake schema).\n\n**Fact tables** store the quantitative measurements of a business process (e.g. sales amount, quantity), are usually large, and contain foreign keys to dimensions. **Dimension tables** store the descriptive context (who/what/where/when — customer, product, store, time) used to slice and filter the facts. Facts are numeric and additive; dimensions provide the labels and hierarchies for analysis.")

add(E, 11, "open",
    "Please compare the content of conceptual, logical and physical data models. (For additional points: clarify the different purposes for which data models are used.)",
    [],
    [],
    "A **conceptual data model** is the most abstract: it captures the main entities and the relationships between them (e.g. an ER diagram at a high level), independent of any technology. Its purpose is to communicate with stakeholders and agree on scope and business meaning.\n\nA **logical data model** refines this into a technology-independent but detailed structure: entities become tables/relations with all attributes, primary and foreign keys, normalisation, and cardinalities — but still without vendor-specific details. Its purpose is precise design of the data structures.\n\nA **physical data model** maps the logical model onto a specific DBMS: exact table and column names, concrete data types and sizes, indexes, partitioning, storage parameters, and platform-specific options. Its purpose is implementation and performance. In short, the three models move from *what data means*, to *how it is structured*, to *how it is physically stored and optimised*.")

add(E, 12, "multi",
    "A table in the first normal form:",
    [("a","contains a primary key"),
     ("b","can include one column for both the name and the surname of the person"),
     ("c","contains many candidate keys, out of which one is selected as a primary key"),
     ("d","is also a table in the second normal form")],
    ["a","c"],
    "A relation has a key, one of possibly several candidate keys chosen as the primary key (a, c). Being in 1NF does not imply 2NF — partial dependencies may still exist (d is false). Storing name+surname in one column conflicts with atomicity, so (b) is not a desirable 1NF property.")

add(E, 13, "multi",
    "A table has been defined. Next, the need to change its structure was observed. Such a change:",
    [("a","can always be done with ALTER TABLE"),
     ("b","may require the table to be dropped and recreated"),
     ("c","will not be noticed by the users as it can always be done within no more than a second"),
     ("d","can be potentially done with ALTER TABLE")],
    ["b","d"],
    "Many changes are possible with ALTER TABLE (d), but not all — some restructurings require dropping and recreating the table (b). 'Always' (a) and 'always within a second / unnoticed' (c) are false; large changes can be slow and disruptive.")

add(E, 14, "multi",
    "Profiles in Oracle databases can be used for:",
    [("a","revoke unnecessary permissions"),
     ("b","define requirements to be matched by user passwords"),
     ("c","mitigate the risk of account takeover"),
     ("d","find out whether a user queries individual tables"),
     ("e","limit the use of server resources by a user")],
    ["b","c","e"],
    "Profiles enforce password rules (complexity, expiry, lockout) — which helps mitigate account takeover — and impose resource limits per user. Revoking privileges is done with REVOKE (a), and monitoring table access is auditing (d).")

add(E, 15, "multi",
    "A network connection from a remote client application to the Oracle database is attempted. A successful connection:",
    [("a","requires a DBMS instance to be in the OPEN state"),
     ("b","will not be possible, if SHUTDOWN IMMEDIATE operation is in progress"),
     ("c","requires the listener process to be running"),
     ("d","depends on whether a network connection with a listener can be established")],
    ["a","b","c","d"],
    "A normal user connection needs the database OPEN, a running listener that the client can reach over the network, and obviously fails while the instance is shutting down. All four conditions apply.")

add(E, 16, "multi",
    "NoSQL platforms:",
    [("a","are defined through mathematical theory"),
     ("b","use SQL as a primary way of interacting with the data"),
     ("c","do not use SQL as a primary way of interacting with the data"),
     ("d","do not use SQL at all"),
     ("e","are nowadays explained as “not only SQL” platforms")],
    ["c","e"],
    "'NoSQL' is now read as 'not only SQL': SQL is not the primary access method (c, e), though many such platforms offer SQL-like interfaces, so 'no SQL at all' (d) is false. There is no formal mathematical NoSQL theory (a), unlike the relational model.")

add(E, 17, "multi",
    "A transaction has been rolled back. As a consequence:",
    [("a","all updates made within the transaction were undone"),
     ("b","all records inserted within the transaction were removed"),
     ("c","other transactions running at the same time have been rolled back"),
     ("d","uniqueness of a primary key might have been violated")],
    ["a","b"],
    "ROLLBACK undoes every change of that transaction — updates reverted and inserts removed — restoring the prior state. It does not affect other transactions, and integrity constraints such as primary-key uniqueness remain enforced.")

add(E, 18, "multi",
    "A developer decided to use optimistic locking. If so:",
    [("a","records will be locked at the time of reading the data to show it on the screen"),
     ("b","conflicts in updating the data can be detected at the time of submitting changes to a database"),
     ("c","multiple users will be able to start editing the same data, such as customer record, in the user interface"),
     ("d","only one user will be allowed to start editing the same data, such as customer record, other users will be suspended")],
    ["b","c"],
    "Optimistic locking takes no lock while reading/editing, so several users may begin editing the same record (c); a conflict is detected only at save time, e.g. via a version/timestamp check (b). Locking at read time and blocking other editors (a, d) describe pessimistic locking.")

add(E, 19, "single",
    "The benefits of creating an INSERT trigger for a table A compared to executing a batch of SQL statements by a client application include:",
    [("a","improved performance"),
     ("b","portability of the code among different DBMSs"),
     ("c","the ability not to use SQL at all"),
     ("d","the ability to execute custom code whenever a new record is inserted into the table A"),
     ("e","the ability to execute custom code whenever a new record is inserted into any of the tables of the database")],
    ["d"],
    "A trigger guarantees that custom logic runs whenever a row is inserted into that specific table, regardless of which client did it (d). Triggers are tied to one table (not every table, e), are DB-specific (not portable, b), still use SQL/PLSQL (c), and do not inherently improve performance (a).")

add(E, 20, "single",
    "CAP theorem states that:",
    [("a","only two out of three features (Consistency, Availability, Partition tolerance) are possible at the same time"),
     ("b","only one out of three features (Consistency, Availability, Portability tolerance) is possible at the same time"),
     ("c","all three features (Consistency, Availability, Partition tolerance) are possible at the same time"),
     ("d","all three features (Consistency, Availability, Portability) are possible at the same time"),
     ("e","only two out of three features (Consistency, Availability, Portability) are possible at the same time")],
    ["a"],
    "CAP concerns Consistency, Availability and Partition tolerance, and states a distributed system can guarantee at most two of these three simultaneously. The options mentioning 'Portability' use the wrong term.")

add(E, 21, "multi",
    "A company wants to set up a system with which business users could generate figures based on integrated data from different databases. If so, the company should deploy:",
    [("a","a Business Intelligence platform"),
     ("b","a NoSQL platform"),
     ("c","Apache Hadoop"),
     ("d","a data warehouse"),
     ("e","distributed transactions")],
    ["a","d"],
    "Cross-database analytical reporting for business users is exactly what a data warehouse (integrated data) plus a BI platform (the reporting/analysis front end) provide. NoSQL, Hadoop and distributed transactions do not address this need directly.")

# ---------------------------------------------------------------------------
# EXAM 2024-B  (test_2024_2)
# ---------------------------------------------------------------------------
E = "2024-B"
add(E, 1, "single",
    "In the event of deletion of a record in Table A, the developer wants to document the fact of the deletion by writing a new record to another table B (while removing the record in Table A), but this change must be made in the database layer, not in the client application. The recommended solution is:",
    [("a","Use a periodically run stored procedure"),
     ("b","rely on a data warehouse for such functionality"),
     ("c","Use an AFTER DELETE trigger"),
     ("d","Use an INSTEAD OF INSERT trigger"),
     ("e","Use an AFTER UPDATE trigger")],
    ["c"],
    "An AFTER DELETE trigger on table A fires automatically in the database layer whenever a row is deleted, letting it insert the audit record into B. A periodic procedure would miss the exact event; INSTEAD OF INSERT and AFTER UPDATE respond to the wrong events.")

add(E, 2, "single",
    "The system stores data as documents. Such a system is:",
    [("a","a relational database management system"),
     ("b","a NoSQL system"),
     ("c","a relational data warehouse system"),
     ("d","Apache Hadoop")],
    ["b"],
    "Document-oriented storage (e.g. JSON/BSON documents as in MongoDB) is a NoSQL data model, distinct from relational systems and from Hadoop's file-based storage.")

add(E, 3, "single",
    "The way to get a deadlock is to:",
    [("a","use two transactions at the same time; irrespective of the changes requested in such transactions, a deadlock will happen"),
     ("b","use only two transactions between which there is a cyclical relationship; more transactions will never cause a deadlock"),
     ("c","generate lost updates; lost updates always result in deadlock"),
     ("d","use at least two, including more transactions, between which there is a cyclical relationship")],
    ["d"],
    "A deadlock requires a cycle of lock-wait dependencies among two or more transactions. Merely running two transactions concurrently does not cause it (a), it can involve more than two (b is false), and lost updates are a different anomaly (c).")

add(E, 4, "single",
    "The company intends to create a central Business Intelligence system. The system should enable the creation of cross-sectional analyses with the simultaneous use of data from various company databases – e.g. production, customer-relationship and sales. The recommended solution relies on:",
    [("a","a data warehouse that has a physical data model created as a sum of physical data models of source databases"),
     ("b","querying data directly from source databases"),
     ("c","a data warehouse that has a physical data model created based on the physical data models of source databases, though e.g. denormalisation is frequently applied compared to the source data models"),
     ("d","the use of one of the NoSQL platforms, such as Apache Cassandra, to store and provide data warehouse data")],
    ["c"],
    "A data warehouse integrates the source models into a new analytical model — informed by, but not a mere union of, the source physical models — and is typically denormalised (star schema) for query performance. Direct querying of sources and using Cassandra as the warehouse are not the recommended approach.")

add(E, 5, "open",
    "The Oracle database administrator wants to reduce the risk of time-consuming database recovery, while the DBMS instance can be stopped only once a month. What kind of backups should be created?",
    [],
    [],
    "Because the instance can be shut down only once a month, the DBA cannot rely on frequent cold (offline) backups. The database should run in **ARCHIVELOG mode** and use **online (hot) backups** taken with the instance OPEN — e.g. with RMAN — supplemented by **archived redo logs**.\n\nA practical strategy: a periodic **full online backup**, plus regular **incremental online backups** and continuous **archiving of redo logs**. The single monthly downtime can optionally be used for a full cold backup. This combination keeps recovery fast (recent incrementals + archived redo allow restoring to a point in time) without requiring the instance to be stopped, directly reducing the risk of long, costly recovery.")

add(E, 6, "multi",
    "NoSQL systems are typically:",
    [("a","Relational systems"),
     ("b","systems based on the formal theory of NoSQL, which is a refinement of the theory of relational systems"),
     ("c","systems based on the mathematical theory of NoSQL, which is a negation of the theory of relational systems"),
     ("d","open source systems"),
     ("e","systems developed in the twenty-first century"),
     ("f","systems based on the formal theory of NoSQL, though they do not rely on the relational systems")],
    ["d","e"],
    "Typical NoSQL systems are open source and emerged in the 21st century to handle web-scale data. There is no formal 'NoSQL theory' (so b, c, f are false), and they are not relational (a).")

add(E, 7, "multi",
    "Implementations of big data solutions are usually characterised by the use of data:",
    [("a","of significant size measured, e.g. in the number of bytes"),
     ("b","of higher quality than in relational databases"),
     ("c","of lower quality than in relational databases"),
     ("d","more carefully checked before placing in the system(s) keeping the data than in the case of data stored in RDBMS platforms")],
    ["a","c"],
    "Big Data is large in volume (a) and, because it is ingested raw with schema-on-read and little upfront validation, is generally of lower quality than tightly validated relational data (c). It is not more carefully checked (b, d are false).")

add(E, 8, "multi",
    "Vector layers:",
    [("a","are used in GIS systems"),
     ("b","enable the execution of spatial queries"),
     ("c","are preferred over raster layers because of the ease of analysing the data contained in these layers"),
     ("d","can rely on different coordinate systems, but these systems always rely on one approximation of the shape of the Earth")],
    ["a","b"],
    "Vector layers represent discrete features in a GIS and support spatial queries (distance, containment, intersection). Neither type is universally 'preferred' (c), and coordinate systems use different Earth models/datums and ellipsoids, so 'one approximation' (d) is false.")

add(E, 9, "open",
    "Can one transaction in a typical NoSQL columnar database running on a cluster of servers span changes in many records? Explain why transactional processing is implemented the way it is in such databases.",
    [],
    [],
    "In a typical wide-column NoSQL store (e.g. Apache Cassandra, HBase) a transaction usually **cannot freely span many records (rows) across the cluster** with full ACID guarantees. Atomicity is normally provided only at the level of a **single row (or single partition/key)**.\n\nThe reason is the distributed, partitioned, horizontally-scaled design. Rows are sharded across many nodes by their key, so a multi-row transaction would require coordinating locks/commits across several machines (e.g. distributed two-phase commit), which is expensive and harms availability and latency. Following the CAP trade-off, these systems prioritise **availability, partition tolerance and scalability** over strong multi-record consistency. Restricting atomic operations to a single row/partition keeps writes fast and the cluster highly available, at the cost of cross-record transactional guarantees (which applications are expected to design around).")

add(E, 10, "multi",
    "If the COMMIT command is successfully executed to commit transaction A, which is confirmed by Oracle DBMS:",
    [("a","the Oracle DBMS guarantees that the data changed as a part of the transaction has already been saved in the database files"),
     ("b","the Oracle DBMS guarantees that the data changed as a part of the transaction will not be lost because of the sudden termination of the DBMS instance in the ABORT mode"),
     ("c","Regardless of archiving (or not archiving) transaction logs, we will be able to recover the database in the future to a state that takes into account the changes made to the database by the transaction"),
     ("d","no other transaction was rolled back because of executing transaction A")],
    ["b","c","d"],
    "On COMMIT, Oracle guarantees durability by writing redo to the online redo logs, so committed changes survive an ABORT/instance crash (b) and are recoverable via crash recovery whether or not logs are archived (c); committing A does not roll back other transactions (d). However, the changed data blocks may still be only in the buffer cache, not yet written to the datafiles, so (a) is false.")

add(E, 11, "single",
    "There is a need to prevent excessive use of the computing power of the Oracle DBMS instance. For this task, one should:",
    [("a","use triggers"),
     ("b","use stored procedures"),
     ("c","use profiles"),
     ("d","use permissions"),
     ("e","use audit options")],
    ["c"],
    "Oracle profiles can impose resource limits (CPU per call/session, sessions, idle time, etc.) on users, directly capping resource consumption. Triggers, procedures, privileges and auditing do not limit resource usage.")

add(E, 12, "multi",
    "Establishing a new network connection to the Oracle database:",
    [("a","Requires the presence of a listener process"),
     ("b","can refer to various listener processes, and this solution promotes high availability"),
     ("c","can be implemented via different network interfaces and such a solution promotes high availability"),
     ("d","can benefit from client-side Oracle Net components")],
    ["a","b","c","d"],
    "A new connection needs a listener to broker it; configuring multiple listeners and multiple network interfaces improves availability, and client-side Oracle Net components handle name resolution, failover and load balancing. All four are correct.")

add(E, 13, "multi",
    "Normalisation of the table to the third normal form:",
    [("a","It is a theoretical process, omitted in practical applications"),
     ("b","Requires, among others, the identification of the primary key"),
     ("c","Does not allow the column value to depend on other columns that are not part of the primary key"),
     ("d","Allows non-atomic values in table columns"),
     ("e","Requires, among others, the identification of the candidate key")],
    ["b","c"],
    "3NF builds on 1NF/2NF: it needs a primary key (b) and forbids transitive dependencies, i.e. a non-key column depending on another non-key column (c). Normalisation is used in practice (a is false), non-atomic values violate 1NF (d is false), and while candidate keys matter conceptually, the option as phrased is not the intended requirement here.")

add(E, 14, "single",
    "A designer proposed a table of enrollment for elective classes with columns: lecture_ID, student_ID, lecture_name, student_name_and_surname, with the primary key consisting of the first two columns. This table:",
    [("a","is in the first normal form"),
     ("b","is in the second normal form"),
     ("c","is in the third normal form"),
     ("d","does not meet the requirements of any of the normal forms")],
    ["a"],
    "lecture_name depends only on lecture_ID and student_name depends only on student_ID — partial dependencies on part of the composite key. That violates 2NF, so the table is in 1NF only (it does satisfy 1NF, so d is false).")

add(E, 15, "multi",
    "In physical data models:",
    [("a","data types for individual columns are not defined"),
     ("b","tables are defined"),
     ("c","primary keys are defined"),
     ("d","indexes are defined")],
    ["b","c","d"],
    "A physical data model targets a specific DBMS and defines tables, primary keys, indexes and concrete column data types. So (a) is false — data types are precisely defined at the physical level.")

add(E, 16, "multi",
    "The data scientist must be able to read the data of all Oracle database tables. If so:",
    [("a","It should be assumed that the person does not abuse their powers, because a data scientist is a person of special trust, and there are no mechanisms dedicated to such a situation"),
     ("b","audit mechanisms should be used for higher security"),
     ("c","distributed transactions should be used to reduce the risk of unjustified reading of data"),
     ("d","fine-grained auditing can be of potential use"),
     ("e","profiles should be used to mitigate the risk of account takeover")],
    ["b","d"],
    "Granting broad read access calls for monitoring: standard auditing (b) and fine-grained auditing (d) track who reads which data. Blind trust (a) and distributed transactions (c) are wrong; profiles address passwords/resources, not the monitoring of legitimate-but-broad read access (e).")

add(E, 17, "multi",
    "In order to store data in the Apache Hadoop platform, assuming the use of only this platform, it is necessary to:",
    [("a","Specify the structure of the table in which the data will be saved, including the names of columns and data types for these columns"),
     ("b","Specifying the name and path to the file in which the data is to be saved"),
     ("c","Select the file format in which the data should be saved, as it is not imposed by Apache Hadoop"),
     ("d","Specify only the type of layer (raster vs. vector), as this is an obligatory feature of all data saved in Apache Hadoop")],
    ["b","c"],
    "Hadoop/HDFS is schema-on-read file storage: you specify a file name/path (b) and choose a file format (c), since Hadoop does not impose one. You do not predefine relational table columns/types (a), and raster/vector layers are a GIS concept (d).")

add(E, 18, "multi",
    "An index:",
    [("a","should be created always for the primary key (or it can be created automatically by the DBMS system)"),
     ("b","should be created always on columns taking three distinct values"),
     ("c","should be created always on foreign key columns — one index for each foreign key column of a given table, assuming high selectivity of the foreign key"),
     ("d","can slow down SQL UPDATE statements"),
     ("e","can speed up SQL UPDATE statements")],
    ["a","d","e"],
    "A primary key is backed by an index, usually created automatically (a). Indexes add maintenance cost on writes, slowing UPDATEs (d), yet can also speed up an UPDATE by quickly locating the rows in its WHERE clause (e). Indexing a column with only three distinct values is low-selectivity and generally unhelpful (b), and 'always' index every FK (c) is too absolute.")

add(E, 19, "multi",
    "Higher resiliency to various system failures in which a client application connects to an Oracle database instance over a network connection can be provided by:",
    [("a","using multiple listener processes"),
     ("b","listening carried out by the listener process on various network interfaces"),
     ("c","appropriate entries in client-side Oracle Net configuration file making client components attempt to connect to various listener processes"),
     ("d","using profiles")],
    ["a","b","c"],
    "Availability is improved by redundancy in the connection path: multiple listeners, listening on several network interfaces, and client-side configuration that fails over among listeners. Profiles govern passwords/resources, not connection resiliency (d).")

# ---------------------------------------------------------------------------
# write files
# ---------------------------------------------------------------------------
def slug_num(n):
    return f"{n:02d}"

def yaml_list(items):
    if not items:
        return "[]"
    return "[" + ", ".join(f'"{i}"' for i in items) + "]"

count = 0
for q in Q:
    qid = f"q-{q['exam']}-{slug_num(q['num'])}".lower()
    fname = os.path.join(OUT, qid + ".md")
    lines = []
    lines.append("---")
    lines.append(f'id: "{qid}"')
    lines.append(f'exam: "{q["exam"]}"')
    lines.append(f'number: {q["num"]}')
    lines.append(f'type: "{q["typ"]}"')
    lines.append(f'tags: {yaml_list([q["exam"]])}')
    lines.append(f'correct: {yaml_list(q["correct"])}')
    lines.append("pdfs: []")
    lines.append("---")
    lines.append("")
    lines.append(q["stem"])
    lines.append("")
    if q["typ"] == "open":
        lines.append("### Answer")
        lines.append("")
        lines.append(q["explanation"])
        lines.append("")
    else:
        for letter, text in q["options"]:
            lines.append(f"- {letter}) {text}")
        lines.append("")
        lines.append("### Explanation")
        lines.append("")
        lines.append(q["explanation"])
        lines.append("")
    with open(fname, "w") as f:
        f.write("\n".join(lines))
    count += 1

print(f"Wrote {count} question files to {OUT}")
