1. Data cube:
   a. is used in GIS  
   b. is created in order to make it easier to browse raw data  
   c. contains date dimension  
   d. contains date measure  
   e. typically built on top of the data present in a data warehouse  

2. A transaction is executed in READ UNCOMMITTED mode. When executing this transaction the programmer reads the balance contained in a certain bank account record. This means:
   a. The balance of this account is guaranteed not to change during the transaction  
   b. The record with the balance can be not committed yet, dirty reads can be observed  
   c. Another isolation level should be used, due to the possible use of wrong data in the transaction  
   d. Another isolation level should be used to speed up data processing  

3. A connection from a remote client application to Oracle database is attempted. This always requires:
   a. the use of Oracle listener  
   b. the use of user and password  
   c. satisfying conditions defined by the user profile  

4. A table has been defined. Next, the need to change its structure was observed. Such a change:
   a. can be always done with ALTER TABLE  
   b. may require the table to be dropped and recreated  
   c. is not possible without disconnecting all users  

5. Oracle database has been successfully running in NOARCHIVE mode and suggested backups were created. After the failure of disk containing data files:
   a. The database can be recovered to the moment of the last whole backup of a database  
   b. The database can be recovered till the moment immediately preceding disk failure  
   c. Backup is not needed to recover the database  
   d. Online logs will not be used to recover a database  

6. Data warehouse:
   a. contains all columns present in OLTP database  
   b. is nowadays replaced by Business Intelligence platforms  
   c. has higher quality data than Big Data resources  
   d. typically contains data from multiple relational databases  
   e. typically contains data for recent weeks only to speed up analytical processing  

7. A table contains 500 000 records and columns: A taking 500 000 unique values and B taking 3 unique values. Both columns are frequently used for filtering, but not together:
   a. An index should be created with an index key composed of column A  
   b. An index should be created with an index key composed of column B  
   c. An index should be created with an index key composed of both columns A and B  

8. A foreign key pointing from table A to table B (teachers) and relying on a single column has been defined. The column of the foreign key was set as a NOT NULL column. This means:
   a. For every teacher there is at least one lecture, but possibly more  
   b. For every teacher there is exactly one lecture  
   c. For every lecture there is possibly more than one teacher assigned  
   d. For every lecture there is exactly one teacher assigned  
   e. For some lectures there may be no teacher assigned  
   f. Some lectures may refer to teachers that have been already removed from the table of teachers  

9. Some of the tables of Oracle database contain confidential data that should be browsed only by some of the system users. Occasionally, a database administrator may also have to browse it. Please describe how to reduce the risk that unauthorised users will read the data and how to detect reading the confidential data by users allowed to do so, but overusing their permissions.
   a. Please provide your answer below the test or on a separate page.  
   b. To get extra points, please describe how SQL injection attack can be performed and how it is related to the unauthorised use of data.  

10. A table in the first normal form:
   a. contains primary key  
   b. can include values such as “London, Downing Street, 10”  
   c. can contain a composite primary key  
   d. can include columns that depend on a part of a primary key only  

11. Big Data is defined as:
   a. high value data  
   b. high quality data  
   c. high volume data  
   d. high velocity data  

12. Please describe the logical organisation of Oracle database.
   a. Please provide your answer below the test or on a separate page.  
   b. To get extra points, please describe how to use tablespaces and backups to quickly restore, after the failure, the data of one e.g. 20 tables of a database first. This is to let users work with the core functionality of a system without waiting for the data of the remaining tables to be restored.  

13. A one-to-many relation has been identified between tables A and B. This means:
   a. Foreign keys have to be added to both of the tables  
   b. A new table with one foreign key is needed  
   c. A new table with two foreign keys is needed  
   d. A new table without foreign keys is needed  
   e. A foreign key should be added to table B  
   f. A foreign key should be added to table A  

14. To recover Oracle database, the following files will be useful:
   a. whole backup  
   b. online transaction logs  
   c. vector layers  
   d. archived transaction logs  
   e. raster layers  

15. NoSQL cluster platform has been proposed to store the data. This means:
   a. SQL queries will not be possible  
   b. SQL queries may not be possible  
   c. improved support for transactions compared to RDBMS can be expected  

16. Please describe in points the differences between a table in RDBMS such as MS SQL Server and a table in Apache HBase.
   a. Please put your answer below the test or on a separate page.  
   b. To get extra points, please describe whether dedicated mechanisms of the platforms (one or both of them) exist with which multiple versions of data present in a row can be stored, whether this means storing multiple versions of entire rows and how the number of versions can be set.  

17. The company needs a system that should easily answer queries such as finding all water supply pipes located at least partly in the city area defined by a polygon. This means that the company needs:
   a. GIS system  
   b. NoSQL system  
   c. RDBMS system  
   d. Apache HBase  

18. A utility company has decided to use GIS system. It can expect return on investment:
   a. because of just buying and installing GIS system  
   b. because of running spatial queries on raster labelling of its network  
   c. because of just using GIS and mathematical modelling of its network  
   d. because of making better decisions thanks to GIS system and mathematical modelling  

19. Sample NoSQL platforms include:
   a. Apache HBase  
   b. ESRI ArcGIS  
   c. MS SQL Server  
   d. MongoDB  

20. A table of products has been designed, which includes a primary key and a column with a list of countries in which a product is sold. Individual country names in this column are comma separated. Such a table:
   a. is in the first normal form  
   b. is in the second normal form  
   c. is in the third normal form  
   d. is not normalised  

21. A table in the third normal form:
   a. contains primary key  
   b. can include non-atomic values  
   c. can include one column for all address data i.e. (city, street, house number)  
   d. can contain a composite primary key  
   e. is also a table in the second normal form  
   f. can include columns that depend on a part of a primary key only  

22. Before the list of columns for the tables planned in the relational database is developed:
   a. System scope should be defined  
   b. Normalization should be performed  
   c. Possible high-level integration with other databases should be identified  
   d. The objectives for creating the database should be specified  

23. Big Data is:
   a. typically used with schema-on-write approach  
   b. typically data of higher quality than data present in data warehouses  
   c. typically carefully modelled before being placed in a system, typically being a relational database management system  
   d. frequently stored in Apache Hadoop  

24. The benefits of using a stored procedure compared to executing a batch of SQL statements include:
   a. improved performance  
   b. portability of the code among different DBMSs  
   c. the ability to reduce the overhead of client-server network communication  

25. There is a need to put new orders into a local database and into a central database of a company. The orders can be placed in the central database with some latency in case of network connectivity issues which occasionally happen. The suggested solution is to:
   a. use distributed transactions  
   b. use replication from the local database to the central database  
   c. put new records directly from the local application into the central database  