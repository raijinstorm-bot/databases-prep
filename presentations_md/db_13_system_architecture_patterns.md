# The architecture of database systems (Architektura systemów baz danych)

## Slide 1: Title

dr hab. inż. Maciej Grzenda
M.Grzenda@mini.pw.edu.pl
http://www.mini.pw.edu.pl/~grzendam

Politechnika Warszawska
Wydział Matematyki i Nauk Informacyjnych

Architektura systemów baz danych
The architecture of database systems

## Slide 2: Project acknowledgement

MSc program in Data Science has been developed as a part of task 10 of the project "NERW PW. Science - Education - Development - Cooperation" co-funded by European Union from European Social Fund.

## Slide 3: Objectives

- Frequently more than one instance of a DBMS exists in one organisation
- This is for many reasons such as:
  - Different database applications require different DBMS platforms or different versions of these platforms
  - Key enterprise systems may run on their own instances to increase stability and simplify system management
  - Standby servers may be used to ensure high availability of the systems
- Hence, how multiple instances of DBMS platforms are managed in terms of data management is a vital aspect of data management

## Slide 4: A bit of history: File-based approach

Diagram:

```
   +-------------+      +-------------+   ......   +-------------+
   |    Sales    |      |  Inventory  |            | Accounting  |
   +-------------+      +-------------+            +-------------+
   | DBMS Engine |      | DBMS Engine |            | DBMS Engine |
   +-------------+      +-------------+            +-------------+
          ^                    ^                          ^
           \                   |                         /
            \         Network communication             /
             \                 |                        /
              \                v                       /
   +======================================================+
   | File server                +-------------+          |
   | (e.g. Ms Windows,          | Database(s) |          |
   |  UNIX, Linux etc.)         +-------------+          |
   +======================================================+
```

(Arrows: each application's DBMS Engine connects bidirectionally to the central Database(s) cylinder on the file server, labelled "Network communication".)

Callout: All database applications access the database (being just a collection of files) through embedded DBMS engine, being a software library.

## Slide 5: Why not file-based approach for multi-user systems?

- Applications access the database by using embedded libraries, thus:
  - The data is typically transferred over the network to be updated and queried on the users' workstations,
  - Poor scalability of the solution is observed when databases get larger due to:
    - Possible network congestion,
    - Increased demand for CPU time on client workstations since data processing occurs on client workstations,
  - Limited security of the data:
    - usu. data files can be easily copied and/or modified by the users
    - Network problems may result in partial updates and/or damaged file structure.
- While file-based approach can still be observed for some small-scale systems, we will focus on more demanding (and complex) settings in this lecture

## Slide 6: When to use file-based i.e. serverless approach?

- File-based approach, i.e. serverless databases can be used for specific use cases, when a local lightweight database solution is needed. This includes running databases on:
  - Mobile phones,
  - Cameras,
  - Vehicles,
  - Remote sensors,
  - Drones,
  - Medical devices and other Internet of Things devices,
  - But also to enable local data analysis, e.g. in JupyterLab
- A very popular serverless solution is SQLite (https://sqlite.org), which is an in-process library that can be used to manage local data as a relational database, query and modify it using SQL. All the source code of SQLite is defined with one file in C language.
- The size of the library is typically less than 1MB.

Note that typically, only user will access a serverless database at a time. Still, the database library can offer transactional processing.

## Slide 7: SQLLite examples

```python
import sqlite3
conn = sqlite3.connect("/Users/…/my_database.db")
df = pd.read_sql_query("select count(*),Autor_ID from \
                       (select distinct Job,Autor_ID from papers) group by Autor_Id \
         having count(*)>1", conn)
df

cursor = conn.cursor()
cursor.execute("update grants set Department=TRIM(\
      SUBSTR(\
        Project_Manager,\
        INSTR(Project_Manager, '(')+1,\
        INSTR(Project_Manager, ')')-1 - INSTR(Project_Manager, '(') \
      )\
  );")
conn.commit()
```

Annotations:
- "Rather than connecting to a service, we open a file" (points to `sqlite3.connect(...)`)
- "A dataframe can be created out of SQL result set" (points to `pd.read_sql_query(...)`)
- "Transactional processing is supported" (points to `conn.commit()`)

A sample tool to manage different databases including SQLLite is Dbeaver https://dbeaver.io

## Slide 8: Distributed databases (Rozproszone bazy danych)

- Distributed databases are databases composed of multiple databases
- Example: country-wide tax database can be a sum of regional databases
- Distributed databases are used:
  - For mission-critical systems - when stable connection to the remote server can not be provided local database may be added
  - To decrease response time
  - To provide for autonomous maintenance of software systems
  - When different software systems in an organisation require their own DBMS platforms (heterogeneous distributed databases)
  - When most of the time access to local database only is sufficient

## Slide 9: Distributed databases – sample architecture

Diagram:

```
   +---------------+                         +---------------+
   |    Client     |                         |    Client     |
   | applications  |                         | applications  |
   +---------------+                         +---------------+
   [===== LAN =====]                         [===== LAN =====]
   +---------------+                         +---------------+
   |   Database    |                         |   Database    |
   |   Server#1    |       . . .             |   Server#n    |
   +---------------+                         +---------------+
          ^                                          ^
          | (up/down)   [============ VPN ===========]   | (up/down)
          v                                          v
   ( Database#1 )                             ( Database#n )
```

Callout (left): Most frequently, client applications communicate with their own DBMS instance.

Callout (right): DBMS platforms may exchange their data through secure connections e.g. over Virtual Private Network (VPN)

## Slide 10: Distributed transactions (Transakcje rozproszone)

- Distributed transactions (DTs) are transactions that require multiple databases or multiple DBMSs to participate in
- If every database has its own private transaction log, then even a transaction that affects two different databases on the same database server requires a distributed transaction
- To execute a distributed transaction means to ensure ACID properties, which is more difficult in a distributed setting

## Slide 11: What is a distributed transaction?

- DT requires significant overhead: typically two phase commit protocol (dwufazowy protokół potwierdzeń) is involved. This protocol relies on two phases:
  - Prepare phase: voting made by all involved DBMS instances
  - Commit phase: distribution of decision to all involved DBMS instances, which have to apply commit to their part of overall changes or roll back their part of the changes
- A coordinating service is required to manage the two stages. In the case of Ms SQL Server, such a service is named Microsoft Distributed Transaction Coordinator
- Notice that the following problems must be addressed:
  - Some of participating DBMSs may be not available,
  - Some of DBMSs may not accept requested changes e.g. due to constraint violation

## Slide 12: Distributed transaction – an example

Callout (top): This batch of SQL statements is submitted to one of participating servers

```sql
DELETE FROM
KRAKOW_OFFICE.Sales.dbo.Customers
WHERE CustomerId='1020'

INSERT INTO
POZNAN_OFFICE.Sales.dbo.Customers
VALUES ('1020','Top Company',….)
```

Diagram:

```
   +---------------+                         +---------------+
   |    Client     |                         |    Client     |
   | applications  |                         | application   |
   +---------------+                         +---------------+
   [===== LAN =====]                         [===== LAN =====]
   +---------------+                         +---------------+
   | KRAKOW_OFFICE |                         | POZNAN_OFFICE |
   +---------------+                         +---------------+
          ^                                          ^
          | (up/down)   [============ VPN ===========]   | (up/down)
          v                                          v
   (   Database   )                           (   Database   )
```

## Slide 13: Example - discussion

- A DT may be submitted to one of participating DBMS servers
- In the case of Ms SQL Server, it starts with:
  `BEGIN DISTRIBUTED { TRAN | TRANSACTION }`
- The transaction coordinator must communicate with both DBMSs to:
  - Confirm updates are possible e.g. there is no 1025 customer in POZNAN_OFFICE DBMS
  - Transactionally execute updates to both servers

## Slide 14: Data synchronisation in distributed databases

| Method | Short description | Remarks |
| --- | --- | --- |
| Distributed transactions | • Updates are made to all participating servers at the same time<br>• Transaction processing is stopped whenever any of the servers is not available | • The only method that guarantees on-line consistency of participating databases<br>• Major processing overhead results in reduced performance |
| Replication | • The updates to monitored tables are transferred to other participating servers.<br>• Can be used to constantly update the data in stand-by servers. | • Accepts latency in data transfer<br>• Updates to participating databases are postponed, thus the system as a whole may accept user's input even if one of the servers does not respond |

## Slide 15: Replication overview

Diagram:

```
                  +-----------------------+
                  | Replication categories |
                  +-----------------------+
                     /         |          \
                    v          v           v
   +-------------+  +-------------+  +-------------+
   |Transactional|  |  Snapshot   |  |    Merge    |
   | replication |  | replication |  | replication |
   +-------------+  +-------------+  +-------------+
```

- Transactional replication: Updates to monitored tables are monitored. Complete SQL statements are transmitted to another DBMS
- Snapshot replication: Copies of table content are transmitted to another DBMS
- Merge replication: The content from two DBMS is merged on regular basis

Key Ms SQL Server replication categories have been described. For details see https://docs.microsoft.com/en-us/sql/relational-databases/replication/types-of-replication?view=sql-server-ver15

## Slide 16: Transactional replication

Diagram:

```
                          +----------+
                          |  DBMS#1  |
                          +----------+
                          /          \
                         v            v
   +------------+   ( Transaction )   ( Database )
   | Log-reader |<--(    log     )
   |   agent    |   
   +------------+
         |
         v
   +--------------+
   | Distribution |---- SQL statements ---->  +----------+
   |    agent     |                           |  DBMS#2  |
   +--------------+                           +----------+
                                              /          \
                                             v            v
                                  ( Transaction )   ( Database )
                                  (     log     )
```

Numbered flow within DBMS#1:
- (1) Transaction is submitted
- (2) The information on transaction is saved (to Transaction log)
- (3) The database is updated

Callout: Ms SQL Server solutions have been described

## Slide 17: Transactional replication

- Can be treated as a kind of add-on functionality to the core of DBMS:
  - Log reader agent monitors on-line all the changes to some of the tables (say: customers) by using transaction logs
  - It captures the changes to place them in a distribution database
  - Distribution agent delivers the SQL statements (namely INSERT, UPDATE and DELETE made on Customers table) to the subscriber periodically (e.g. every night) or on-line

## Slide 18: Transactional replication – case study

- Task: the head office must have a complete list of invoices issued by a regional office by the end of the next business day. Both offices have their own DBMS instances.
- Solution #1:
  - Using distributed transactions, apply at the same time all the updates made on a regional server also on the central server
  - Drawback: no invoices can be issued once the central server gets unavailable
- Solution #2:
  - Set up transactional replication (also on-line replication)
  - In case the central server is not available, all the changes to invoices tables in a local database are still gathered by the log-reader agent and delivered later – once the connection between the servers is re-established

## Slide 19: Snapshot and merge replication

- Snapshot replication:
  - Can be used to periodically replace the content of subscriber's table(s) with new content, without tracking individual changes
  - Example: publication of price list from the company's headquarter
- Merge replication:
  - Can be used to periodically merge the content of two different databases
  - Example: table of customers existing on the central server and mobile workstations of sales representatives. Central database is merged with new customers' data from mobile computers.

## Slide 20: High availability (HA)

- In case of IT systems means that the system is available all the time (24x7)
- In practice, distinction between 99%, 99.9% and higher availability is made
- Typical HA architectures typically involve:
  - Redundant devices:
    - Redundant power supplies,
    - RAID (Redundant Array of Inexpensive Disks),
    - Multiple network interface cards,
    - Redundant network connections,
  - Clusters of servers.

## Slide 21: HA: clusters

- Cluster: two or more similar interconnected servers usu. sharing the same set of disks (disk array)
- Different strategies exist. Examples:
  - Active/passive: one of the servers is ready to accept the requests, but normally passive. It plays the role of a standby server. Its role is to handle requests when the primary one fails
  - Active/active: both servers (or more than 2) share the load

## Slide 22: Cold failover cluster

Diagram:

```
BEFORE FAILOVER
                                              
  SQL statements --->  [ Server#1 (green) ]        [ Server#2 (orange) ]
                       Up and running,             Up and running,
                       answering queries           but idle
                                \                  /
                                 \                /
                                  (  Database  )
```

```
AFTER FAILOVER

  [ Server#1 (red) ]                          [ Server#2 (green) ]  <--- SQL statements
  Not functioning. When recovered,            Up and running,
  still does not receive SQL statements       answering queries
                        \                     /
                         \                   /
                          (   Database   )
```

(Before failover: Server#1 receives SQL statements; Server#2 is up but idle. After failover: Server#1 is dead/red and even when recovered does not receive SQL statements; Server#2 now receives the SQL statements and answers queries.)

## Slide 23: Hot failover cluster

Diagram:

```
BEFORE FAILOVER

  SQL statements --->  [ Server#1 (green) ]
  SQL statements ------------------------------>  [ Server#2 (green) ]
                              \                    /
                               \                  /
                                (   Database   )
                       All cluster servers are working and handle requests
```

```
AFTER FAILOVER

  [ Server#1 (red) ]                          [ Server#2 (green) ]  <--- SQL statements
  Not functioning. When recovered,            All not failed servers are
  can join other servers to                   working and handle requests
  handle requests
                        \                     /
                         \                   /
                          (   Database   )
```

(Before failover: both Server#1 and Server#2 receive SQL statements; all cluster servers are working and handle requests. After failover: Server#1 is dead/red and when recovered can join other servers to handle requests; Server#2 keeps receiving SQL statements; all not failed servers are working and handle requests.)

## Slide 24: Summary

- Most frequently, multiple DBMS instances are used by an organisation
- This is because of:
  - Variety of database applications and DBMS platforms they need
  - Spatial distribution of organisations
  - High availability needs
- Most advanced platforms such as Oracle Real Applications Clusters (RAC) take advantage of a cluster of DBMS instances to combine high availability with high performance

## Slide 25: Pytania ?

Information Sensitivity: General\External

Pytania ?

Zapraszam w trakcie wykładu i w trakcie konsultacji

Miejsce i termin konsultacji - na stronie: https://pages.mini.pw.edu.pl/~grzendam/pl/dydaktyka.html

## Slide 26: Questions?

I am looking forward to your questions during the lectures (including now) and during my office hours

For details on my office hours, please check my website: https://pages.mini.pw.edu.pl/~grzendam/eng/dydaktyka_eng.html

## Slide 27: Project acknowledgement

MSc program in Data Science has been developed as a part of task 10 of the project "NERW PW. Science - Education - Development - Cooperation" co-funded by European Union from European Social Fund.
