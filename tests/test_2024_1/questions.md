2. Please describe the way Apache Hadoop can be used for storing Big Data. Is Apache Hadoop a relational database management system? If not, what are the differences? What has to be specified to store data in Apache Hadoop?
   a. Please provide the answer below the test or on a separate sheet, stating the question number to which it relates.  
   b. For additional points, please describe the meaning of schema-on-read and schema-on-write and which of the two approaches results in higher data quality. Please justify your answer.  

3. A developer wants to run queries finding all buildings located no more than 100 meters from the nearest road, and at least partly contained no further than 500 meters from the nearest power grid line. If so:
   a. a GIS system is needed  
   b. a graph NoSQL platform is needed  
   c. vector layers should be used  
   d. raster layers should be used  
   e. data warehouse will be mandatory  

4. A one-to-many relation between table A and B:
   a. is represented by a foreign key in table A  
   b. is represented by a foreign key in table B  
   c. is represented by an extra table C with foreign keys pointing from it to tables A and B  
   d. is represented by an extra table C with two candidate keys  

5. The transaction is executed in SERIALIZABLE mode. We expect:
   a. improved performance compared to READ UNCOMMITTED  
   b. dirty reads  
   c. non-repeatable reads  
   d. possibly negative impact on the performance of the other transactions  

6. A client application implemented using .NET:
   a. can execute SQL SELECT queries on a remote database  
   b. can execute SQL INSERT statements on a remote database  
   c. can suffer from SQL code injection attempts  
   d. can execute parametrized queries, but this is not recommended  
   e. typically has to concatenate data provided by a user, such as the product name, with the text of the query sent to a database  

7. Fact record:
   a. can typically be found in a data warehouse table  
   b. can typically be found in GIS layer  
   c. can typically be found in a NoSQL table  
   d. typically refers to dimension records  

8. Data warehouse:
   a. typically relies on data retrieved from NoSQL platform(s)  
   b. typically relies on data retrieved from RDBMS platforms  
   c. is nowadays replaced with Big Data platforms such as Apache Hadoop  
   d. is nowadays replaced with NoSQL platforms, especially MongoDB, as MongoDB provides a higher quality of data  

9. Big Data is defined as:
   a. high value data  
   b. high quality data  
   c. high quantity data  
   d. high velocity data  
   e. high volume data  

10. Please describe what a data warehouse is and how data in a data warehouse is created.
   a. Please provide the answer below the test or on a separate sheet, stating the question number to which it relates.  
   b. For additional points, please clarify the difference between fact and dimension tables. Please justify your answer.  

11. Please compare the content of conceptual, logical and physical data models.
   a. Please provide the answer below the test or on a separate sheet, stating the question number to which it relates.  
   b. For additional points, please clarify the different purposes for which data models are used. Please justify your answer.  

12. A table in the first normal form:
   a. contains a primary key  
   b. can include one column for both the name and the surname of the person  
   c. contains many candidate keys, out of which one is selected as a primary key  
   d. is also a table in the second normal form  

13. A table has been defined. Next, the need to change its structure was observed. Such a change:
   a. can always be done with ALTER TABLE  
   b. may require the table to be dropped and recreated  
   c. will not be noticed by the users as it can always be done within no more than a second  
   d. can be potentially done with ALTER TABLE  

14. Profiles in Oracle databases can be used for:
   a. revoke unnecessary permissions  
   b. define requirements to be matched by user passwords  
   c. mitigate the risk of account takeover  
   d. find out whether a user queries individual tables  
   e. limit the use of server resources by a user  

15. A network connection from a remote client application to the Oracle database is attempted. A successful connection:
   a. requires a DBMS instance to be in the OPEN state  
   b. will not be possible, if SHUTDOWN IMMEDIATE operation is in progress  
   c. requires the listener process to be running  
   d. depends on whether a network connection with a listener can be established  

16. NoSQL platforms:
   a. are defined through mathematical theory  
   b. use SQL as a primary way of interacting with the data  
   c. do not use SQL as a primary way of interacting with the data  
   d. do not use SQL at all  
   e. are nowadays explained as “not only SQL” platforms  

17. A transaction has been rolled back. As a consequence:
   a. all updates made within the transaction were undone  
   b. all records inserted within the transaction were removed  
   c. other transactions running at the same time have been rolled back  
   d. uniqueness of a primary key might have been violated  

18. A developer decided to use optimistic locking. If so:
   a. records will be locked at the time of reading the data to show it on the screen  
   b. conflicts in updating the data can be detected at the time of submitting changes to a database  
   c. multiple users will be able to start editing the same data, such as customer record, in the user interface  
   d. only one user will be allowed to start editing the same data, such as customer record, other users will be suspended  

19. The benefits of creating an INSERT trigger for a table A compared to executing a batch of SQL statements by a client application include:
   a. improved performance  
   b. portability of the code among different DBMSs  
   c. the ability not to use SQL at all  
   d. the ability to execute custom code whenever a new record is inserted into the table A  
   e. the ability to execute custom code whenever a new record is inserted into any of the tables of the database  

20. CAP theorem states that:
   a. only two out of three features (Consistency, Availability, Partition tolerance) are possible at the same time  
   b. only one out of three features (Consistency, Availability, Portability tolerance) is possible at the same time  
   c. all three features (Consistency, Availability, Partition tolerance) are possible at the same time  
   d. all three features (Consistency, Availability, Portability) are possible at the same time  
   e. only two out of three features (Consistency, Availability, Portability) are possible at the same time  

21. A company wants to set up a system with which business users could generate figures based on integrated data from different databases. If so, the company should deploy:
   a. a Business Intelligence platform  
   b. a NoSQL platform  
   c. Apache Hadoop  
   d. a data warehouse  
   e. distributed transactions  