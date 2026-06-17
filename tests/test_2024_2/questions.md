1. In the event of deletion of a record in Table A, the developer wants to document the fact of the deletion by writing a new record to another table B (while removing the record in Table A), but this change must be made in the database layer, not in the client application. The recommended solution is:
   a. Use a periodically run stored procedure  
   b. rely on a data warehouse for such functionality  
   c. Use an AFTER DELETE trigger  
   d. Use an INSTEAD OF INSERT trigger  
   e. Use an AFTER UPDATE trigger  

2. The system stores data as documents. Such a system is:
   a. a relational database management system  
   b. a NoSQL system  
   c. a relational data warehouse system  
   d. Apache Hadoop  

3. The way to get a deadlock is to:
   a. use two transactions at the same time; irrespective of the changes requested in such transactions, a deadlock will happen  
   b. use only two transactions between which there is a cyclical relationship; more transactions will never cause a deadlock  
   c. generate lost updates; lost updates always result in deadlock  
   d. use at least two, including more transactions, between which there is a cyclical relationship  

4. The company intends to create a central Business Intelligence system. The system should enable the creation of cross-sectional analyses with the simultaneous use of data from various company databases – e.g. production, customer-relationship and sales. The recommended solution relies on:
   a. a data warehouse that has a physical data model created as a sum of physical data models of source databases  
   b. querying data directly from source databases  
   c. a data warehouse that has a physical data model created based on the physical data models of source databases, though e.g. denormalisation is frequently applied compared to the source data models  
   d. the use of one of the NoSQL platforms, such as Apache Cassandra, to store and provide data warehouse data  

5. The Oracle database administrator wants to reduce the risk of time-consuming database recovery of a database, while the DBMS instance can be stopped only once a month. If so, what kind of backups should be created?

6. NoSQL systems are typically:
   a. Relational systems  
   b. systems based on the formal theory of NoSQL, which is a refinement of the theory of relational systems  
   c. systems based on the mathematical theory of NoSQL, which is a negation of the theory of relational systems  
   d. open source systems  
   e. systems developed in the twenty-first century  
   f. systems based on the formal theory of NoSQL, though they do not rely on the relational systems  

7. Implementations of big data solutions are usually characterised by the use of data:
   a. of significant size measured, e.g. in the number of bytes  
   b. of higher quality than in relational databases  
   c. of lower quality than in relational databases  
   d. more carefully checked before placing in the system(s) keeping the data than in the case of data stored in RDBMS platforms  

8. Vector layers:
   a. are used in GIS systems  
   b. enable the execution of spatial queries  
   c. are preferred over raster layers because of the ease of analysing the data contained in these layers  
   d. can rely on different coordinate systems, but these systems always rely on one approximation of the shape of the Earth  

9. Can one transaction in a typical NoSQL columnar database running on a cluster of servers span changes in many records? Please provide the answer below the test or on a separate sheet, stating the question number to which it relates. Please explain why transactional processing is implemented in the way you describe (i.e. allowing multi-row transactions or not) in such databases.

10. If the COMMIT command is successfully executed to commit transaction A, which is confirmed by Oracle DBMS:
   a. the Oracle DBMS guarantees that the data changed as a part of the transaction has already been saved in the database files  
   b. the Oracle DBMS guarantees that the data changed as a part of the transaction will not be lost because of the sudden termination of the DBMS instance in the ABORT mode  
   c. Regardless of archiving (or not archiving) transaction logs, we will be able to recover the database in the future to a state that takes into account the changes made to the database by the transaction  
   d. no other transaction was rolled back because of executing transaction A  

11. There is a need to prevent excessive use of the computing power of the Oracle DBMS instance. For this task, one should:
   a. use triggers  
   b. use stored procedures  
   c. use profiles  
   d. use permissions  
   e. use audit options  

12. Establishing a new network connection to the Oracle database:
   a. Requires the presence of a listener process  
   b. can refer to various listener processes, and this solution promotes high availability  
   c. can be implemented via different network interfaces and such a solution promotes high availability  
   d. can benefit from client-side Oracle Net components  

13. Normalisation of the table to the third normal form:
   a. It is a theoretical process, omitted in practical applications  
   b. Requires, among others, the identification of the primary key  
   c. Does not allow the column value to depend on other columns that are not part of the primary key  
   d. Allows non-atomic values in table columns  
   e. Requires, among others, the identification of the candidate key  

14. A designer proposed a table of enrollment for elective classes with columns: lecture_ID, student_ID, lecture_name, student_name_and_surname, with the primary key consisting of the first two columns. This table:
   a. is in the first normal form  
   b. is in the second normal form  
   c. is in the third normal form  
   d. does not meet the requirements of any of the normal forms  

15. In physical data models:
   a. data types for individual columns are not defined  
   b. tables are defined  
   c. primary keys are defined  
   d. indexes are defined  

16. The data scientist must be able to read the data of all Oracle database tables. If so:
   a. It should be assumed that the person does not abuse their powers, because a data scientist is a person of special trust, and there are no mechanisms dedicated to such a situation  
   b. audit mechanisms should be used for higher security  
   c. distributed transactions should be used to reduce the risk of unjustified reading of data  
   d. fine-grained auditing can be of potential use  
   e. profiles should be used to mitigate the risk of account takeover  

17. In order to store data in the Apache Hadoop platform, assuming the use of only this platform (i.e. without simultaneous use of, for example, NoSQL platforms), it is necessary to:
   a. Specify the structure of the table in which the data will be saved, including the names of columns and data types for these columns  
   b. Specifying the name and path to the file in which the data is to be saved  
   c. Select the file format in which the data should be saved, as it is not imposed by Apache Hadoop  
   d. Specify only the type of layer (raster vs. vector), as this is an obligatory feature of all data saved in Apache Hadoop  

18. An index:
   a. should be created always for the primary key (or it can be created automatically by the DBMS system)  
   b. should be created always on columns taking three distinct values  
   c. should be created always on foreign key columns — one index for each foreign key column of a given table, assuming high selectivity of the foreign key  
   d. can slow down SQL UPDATE statements  
   e. can speed up SQL UPDATE statements  

19. Higher resiliency to various system failures in which a client application connects to an Oracle database instance over a network connection can be provided by:
   a. using multiple listener processes  
   b. listening carried out by the listener process on various network interfaces  
   c. appropriate entries in client-side Oracle Net configuration file making client components attempt to connect to various listener processes  
   d. using profiles  