# Database Quiz

## 2016 — Polish Computer Science

### 1. Based on the result of an SQL `SELECT` query on tables containing 7 million records, 50 rows are obtained. The most efficient further processing of these rows should be expected when:

- [ ] a) The result is repeatedly selected directly from the original 7-million-row tables
- [ ] b) The result is placed in a temporary table and further processing uses this table
- [ ] c) The result is processed only through a view
- [ ] d) The result is exported to a text file before processing

---

### 2. Creating a view with `CREATE VIEW testView AS SELECT * FROM Orders` causes:

- [ ] a) A physical copy of the `Orders` table to be created
- [ ] b) The data from `Orders` to be permanently stored inside the view
- [ ] c) The definition of the view to be saved, and queries on the view use current data from `Orders`
- [ ] d) The `Orders` table to be replaced by `testView`

---

### 3. Transaction A executes an SQL `UPDATE` command on a record. If transaction A encounters a lock established by transaction B modifying the same record:

- [ ] a) Transaction A automatically cancels transaction B
- [ ] b) Transaction A ignores the lock and updates the record
- [ ] c) Transaction A must wait until transaction B finishes with `ROLLBACK` or `COMMIT`
- [ ] d) Transaction A always receives an error immediately

---

### 4. Normalizing a table to third normal form:

- [ ] a) Requires, among other things, identifying the primary key
- [ ] b) Requires removing all indexes
- [ ] c) Requires deleting all foreign keys
- [ ] d) Requires replacing all tables with views

---

### 5. The result of comparing `'abc' = NULL` is:

- [ ] a) `TRUE`
- [ ] b) `FALSE`
- [ ] c) `0`
- [ ] d) An empty string

---

### 6. The result of comparing `'abc' > NULL` is:

- [ ] a) `TRUE`
- [ ] b) `FALSE`
- [ ] c) `1`
- [ ] d) `'abc'`

---

### 7. Normalizing a table to first normal form:

- [ ] a) Requires, among other things, identifying the primary key
- [ ] b) Requires creating triggers
- [ ] c) Requires creating stored procedures
- [ ] d) Requires removing all constraints

---

### 8. Statistics stored in an Oracle database:

- [ ] a) Should not be used because they slow down all queries
- [ ] b) Should be used because they help prepare better query execution plans
- [ ] c) Replace the need for indexes
- [ ] d) Replace transaction logs

---

### 9. Oracle database audit options allow:

- [ ] a) Monitoring the use of individual SQL commands
- [ ] b) Monitoring successful connection attempts to an instance
- [ ] c) Monitoring unsuccessful connection attempts to an instance
- [ ] d) Replacing the process of granting table privileges

---

### 10. In a database system with unacceptable performance for a frequently executed sequence of complex SQL `SELECT` queries, potentially beneficial actions include:

- [ ] a) Adding new indexes
- [ ] b) Introducing a stored procedure and placing the SQL `SELECT` query code inside it
- [ ] c) Removing all primary keys
- [ ] d) Disabling statistics permanently

---

### 11. In an Oracle database:

- [ ] a) One connection may be handled by a permanently assigned server process
- [ ] b) One connection may be handled by a server process that also alternately handles other connections
- [ ] c) Backups and batch operations should be performed by a dedicated server process
- [ ] d) Every connection must always have its own listener process

---

### 12. The query

`SELECT * FROM Customers WHERE EXISTS (SELECT * FROM Orders WHERE YEAR(OrderDate) = 1997)`  
is used to determine customers who placed orders in 1997. This query:

- [ ] a) Correctly returns only customers who placed orders in 1997
- [ ] b) Does not correctly determine the customers satisfying the condition
- [ ] c) Returns no rows in every case
- [ ] d) Deletes customers without orders

---

### 13. Establishing a new network connection to an Oracle database:

- [ ] a) Typically uses TCP/IP and port 1521
- [ ] b) Requires the presence of a listener process
- [ ] c) May automatically refer to different listener processes for fault tolerance
- [ ] d) Always requires manual copying of database files

---

### 14. In a thick-client application running on 500 workstations and communicating directly with an Oracle database server, the recommended connection method is:

- [ ] a) Dedicated server processes only
- [ ] b) Shared server processes
- [ ] c) No listener process
- [ ] d) A separate database for each workstation

---

### 15. In the case of the `ROLLBACK` command:

- [ ] a) Changes made in the current transaction are undone
- [ ] b) All database tables are deleted
- [ ] c) The transaction is permanently saved
- [ ] d) Indexes are rebuilt

---

### 16. When using `READ UNCOMMITTED`, there is a risk of:

- [ ] a) Dirty reads
- [ ] b) Deadlocks
- [ ] c) Non-repeatable reads
- [ ] d) Complete prevention of all concurrency issues

---

### 17. The number of rows in the result of

`SELECT * FROM TableA JOIN TableB ON 7 = 3 OR 7 > 1`  
will be equal to:

- [ ] a) 0
- [ ] b) The number of rows in `TableA`
- [ ] c) The number of rows in `TableB`
- [ ] d) The product of the number of rows in `TableA` and `TableB`

---

### 18. The value `NULL` is:

- [ ] a) A value indicating the absence of a date in a date-type field
- [ ] b) A value that should be allowed only when necessary
- [ ] c) Always equal to zero
- [ ] d) Always equal to an empty string

---

### 19. Layers in geographic information systems are divided into:

- [ ] a) Raster layers
- [ ] b) Vector layers
- [ ] c) Transaction layers
- [ ] d) SQL layers

---

### 20. In a data cube, there is typically:

- [ ] a) A time-type dimension
- [ ] b) A numeric measure such as sum
- [ ] c) Many dimensions
- [ ] d) Only one table without dimensions

---

## 2015 — Polish Computer Science

### 21. In each row of a table, the list of used columns is different. It is also possible to insert a row with any new column names. This means the table was created:

- [ ] a) In a relational system with strict schema
- [ ] b) In a NoSQL system
- [ ] c) Only in Oracle Database
- [ ] d) Only in MS SQL Server

---

### 22. ER diagrams:

- [ ] a) Contain entities
- [ ] b) Contain relationships
- [ ] c) Describe the meaning of relationships
- [ ] d) Contain only SQL queries

---

### 23. A one-to-many relationship between table A and table B is represented by:

- [ ] a) An additional foreign key in table B pointing to table A
- [ ] b) An additional foreign key in table A pointing to table B
- [ ] c) Deleting table B
- [ ] d) Creating a trigger only

---

### 24. A many-to-many relationship between table A and table B is represented by:

- [ ] a) An additional table C with foreign keys pointing to tables A and B
- [ ] b) A single column with comma-separated values
- [ ] c) Removing primary keys from both tables
- [ ] d) Creating a view only

---

### 25. Normalizing a table to second normal form:

- [ ] a) Aims to eliminate anomalies resulting from redundancy
- [ ] b) According to good practices, may be skipped in OLTP systems
- [ ] c) Requires deleting all tables
- [ ] d) Requires storing all data in one column

---

### 26. In Oracle databases:

- [ ] a) Writing to transaction logs occurs before the client application receives confirmation of successful transaction completion
- [ ] b) Power failure causes the loss of changes made within a transaction that is still in progress
- [ ] c) Transaction logs are never used
- [ ] d) Transactions cannot be rolled back

---

### 27. Network connections to an Oracle database instance:

- [ ] a) May automatically try another listener IP address if the primary one does not respond
- [ ] b) May use configuration files defining connection behavior, for example `load_balance`
- [ ] c) Never use TCP/IP
- [ ] d) Always require direct disk access to database files

---

### 28. Big Data solutions usually use data:

- [ ] a) Of significant size, measured for example in bytes
- [ ] b) Of lower quality than in relational databases
- [ ] c) Of diverse forms, such as forum posts or web application logs
- [ ] d) Stored only in one normalized relational table

---

### 29. Transaction log files in a transactional system:

- [ ] a) Are necessary for the system to operate
- [ ] b) May be archived
- [ ] c) Are used during database recovery after failure
- [ ] d) Are used only for displaying reports

---

### 30. A database:

- [ ] a) May support different national character sets simultaneously
- [ ] b) May use more than one national character set at the same time
- [ ] c) Must always use exactly one character set
- [ ] d) Cannot store multilingual text

---

### 31. A trigger can:

- [ ] a) Execute an SQL `UPDATE` command on another table
- [ ] b) Be executed as a result of data modifications made by different client applications
- [ ] c) Be automatically started after inserting a new record
- [ ] d) Be automatically started instead of inserting a record

---

### 32. NoSQL-class systems are usually:

- [ ] a) Based on a mathematical theory of NoSQL that negates relational theory
- [ ] b) Open-source systems
- [ ] c) Always relational systems
- [ ] d) Always based only on SQL tables

---

### 33. `CREATE TABLE` commands:

- [ ] a) May have different forms in different RDBMS systems, such as Oracle Database and MS SQL Server
- [ ] b) Are identical in every database system
- [ ] c) Can only be used in NoSQL databases
- [ ] d) Always create temporary tables only

---

### 34. NoSQL solutions include systems storing data as:

- [ ] a) Documents
- [ ] b) Graphs
- [ ] c) Rows described by columns that may differ in each row
- [ ] d) Only fully normalized relational tables

---

### 35. A polygon-type vector layer object is defined by:

- [ ] a) A location in a selected coordinate system, described by vertex coordinates
- [ ] b) Descriptive attributes
- [ ] c) Only transaction logs
- [ ] d) Only SQL indexes

---

### 36. From the point of view of performance for many users in a transactional system such as MS SQL Server, it is recommended to use:

- [ ] a) Numerous short-duration transactions
- [ ] b) One very long transaction for all users
- [ ] c) No transactions
- [ ] d) Transactions that never commit

---

### 37. In a cold-failover cluster:

- [ ] a) Before failure, one server participates in SQL query processing
- [ ] b) After failure, at most one server participates in SQL query processing
- [ ] c) All servers always process the same SQL query simultaneously
- [ ] d) No server processes SQL queries before failure

---

### 38. Archiving Oracle transaction logs:

- [ ] a) Is recommended in production systems
- [ ] b) Allows the database to be restored to any point in time
- [ ] c) Is never used in production
- [ ] d) Deletes all committed transactions

---

### 39. The `ALTER TABLE` command:

- [ ] a) Can change only some table properties
- [ ] b) Can be used to add a column
- [ ] c) Can be used to increase the length of a text column
- [ ] d) Can change absolutely every property of a table

---

### 40. The commands `BEGIN TRANSACTION`, `INSERT`, `UPDATE`, and `COMMIT` were executed successfully, and the server confirmed all commands. In this situation:

- [ ] a) Both `INSERT` and `UPDATE` were executed successfully
- [ ] b) Only `INSERT` was executed successfully
- [ ] c) Only `UPDATE` was executed successfully
- [ ] d) Both commands were rolled back

---

### 41. In an employee database, each employee except the rector must be assigned a current supervisor who is another employee. To do this, one should:

- [ ] a) Add a foreign key in the employee table that accepts `NULL`
- [ ] b) Create a separate database for supervisors
- [ ] c) Remove the employee primary key
- [ ] d) Store supervisors only in a text file

---

### 42. Transaction A executes an SQL `UPDATE` command on a record. If transaction A encounters a lock established by transaction B modifying the same record:

- [ ] a) Transaction A must wait until transaction B finishes with `ROLLBACK` or `COMMIT`
- [ ] b) Transaction A automatically overwrites transaction B
- [ ] c) Transaction A deletes the locked record
- [ ] d) Transaction A ignores the lock

---

### 43. A connection pool is a way to:

- [ ] a) Reduce server load caused by opening and closing connections
- [ ] b) Improve application performance
- [ ] c) Replace all SQL queries
- [ ] d) Disable transaction processing