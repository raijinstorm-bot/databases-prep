# Programowanie DBMS i procedury składowane / DBMS programming and stored procedures

**dr hab. inż. Maciej Grzenda**
M.Grzenda@mini.pw.edu.pl
http://www.mini.pw.edu.pl/~grzendam
Politechnika Warszawska
Wydział Matematyki i Nauk Informacyjnych

## Slide 1: Title

Programowanie DBMS i procedury składowane
DBMS programming and stored procedures

dr hab. inż. Maciej Grzenda
M.Grzenda@mini.pw.edu.pl
http://www.mini.pw.edu.pl/~grzendam
Politechnika Warszawska
Wydział Matematyki i Nauk Informacyjnych

## Slide 2: Project funding

MSc program in Data Science has been developed as a part of task 10 of the project „NERW PW. Science - Education - Development - Cooperation" co-funded by European Union from European Social Fund.

## Slide 3: Challenges related to querying and modifying data

- What if our data processing cannot be (easily) done with one SQL SELECT and/or INSERT/UPDATE/DELETE statement?
- Can we develop some longer chains of queries and/or data modification statements?
- Can we rely on some loops, e.g. to calculate income generated from different products, when calculating it for one product requires multiple steps?
- Can we execute some code e.g. to recalculate the value of taxes every time an invoice is modified?

To address these and other challenges, stored procedures, i.e. the procedures executed within the DBMS platform are used.

## Slide 4: Objectives

- DBMSs typically continuously run on high performance servers
- Hence, DBMS provides the best environment for high performance processing of relational data
- Stored procedures and functions can be used to efficiently process data present in relational databases
- This lecture is focused on Transact-SQL capabilities i.e. the capabilities of the language extending SQL and available in Ms SQL Server

## Slide 5: DBMS programming: Ms SQL Server options

Hierarchy diagram of server-side procedures:

- **Server-side procedures**
  - **Stored procedures**
    - Standard SP
    - Triggers
    - Extended SP
    - System SP
  - **Functions**
    - Parametrised views
    - Returning scalar values

(Note: in the diagram, "Server-side procedures" branches into "Stored procedures" and "Functions". "Stored procedures" branches into "Standard SP", "Triggers", "Extended SP", and "System SP". "Functions" branches into "Parametrised views" and "Returning scalar values".)

> Ms SQL Server capabilities only. Diverse capabilities can be found in different DBMS.

## Slide 6: Stored procedures / Procedury składowane

- The procedures defined in SQL-like language, executed by DBMS
- Allow to speed up the execution of resource-intensive processing e.g. complex updates affecting thousands of records
- System SP (procedury systemowe) provide means to configure DBMS and set some of the DBMS options not available through SQL statements
- Extended SP (procedury rozszerzone) are defined in DLLs making it possible to extend Ms SQL Server functionality with arbitrary code

## Slide 7: Stored procedure – basic syntax

```sql
CREATE PROCEDURE ProcedureName 
[@parameterName ParameterType [OUTPUT]  ,…]
 AS
 procedureCode
```

```sql
EXECUTE PROCEDURE ProcedureName 
[@variableName|Value,…]
```

- The syntax comes from Ms SQL Server
- Multiple arguments of different types can be specified
- The procedure can return multiple values through OUTPUT parameters

## Slide 8: Sample stored procedure

```sql
CREATE PROCEDURE CalculateOrderCount @country varchar(100)
AS
DECLARE @customer varchar(100)
DECLARE custom CURSOR LOCAL FOR SELECT CustomerId FROM 
Customers WHERE country=@country
OPEN custom
FETCH NEXT FROM custom INTO @customer
WHILE @@FETCH_STATUS=0
BEGIN
 
UPDATE Customers SET OrderCount=(SELECT COUNT(*) FROM 
Orders WHERE CustomerId=@customer) WHERE 
CustomerId=@customer
 
FETCH NEXT FROM custom INTO @customer
END
CLOSE custom
DEALLOCATE custom
```

The procedure affects multiple records

## Slide 9: Stored procedures vs. direct query processing

Comparison diagram of two communication patterns between Client and DBMS:

**STANDARD** (direct query processing):
- Client → DBMS: SQL query#1
- DBMS → Client: query result#1
- Client → DBMS: SQL query#n
- DBMS → Client: query result#n

(Each query and its result is a separate round-trip between the client and the DBMS.)

**STORED PROC.** (stored procedure processing):
- Client → DBMS: EXEC PROCEDURE …
- DBMS → Client: procedure result(s)
- The DBMS performs the procedure processing internally (shown as a self-loop arrow on the DBMS), so only a single request/response round-trip occurs between client and DBMS.

> By using stored procedures we can significantly reduce network communication overhead

## Slide 10: Database logic – pros and cons

- Database functions and stored procedures:
  - allow to create parameterised views and complex server-side processing
  - The most efficient processing – reduced client-server communication overhead
  - Execution plans created by the database server => faster than ad hoc statements
  - Unfortunately different standards exist (such as Transact-SQL or PL/SQL) => limited portability of procedure/function code

## Slide 11: Triggers (Wyzwalacze)

- Procedures executed after modification or instead of modification to the database
- There are INSERT triggers, UPDATE triggers and DELETE triggers
- Thus you can define for instance AFTER INSERT trigger for ORDERS table i.e. the procedure that will be called by the DBMS every time INSERT statement has been executed
- Notice: if multiple records are affected by a single CRUD statement, the trigger is activated only once – for the whole group of records

## Slide 12: Triggers - remarks

- Capabilities may depend on SQL implementation
- In some DBMS platforms triggers can be defined also for views. Thus a view behaves like a table and allows to define what actions will take place when a record is inserted into a view
- Trigger can change the content of another or even the same table and thus make DBMS fire other triggers

## Slide 13: Triggers - syntax

```sql
CREATE TRIGGER TriggerName ON TableName 
{AFTER|INSTEAD OF} 
{INSERT,UPDATE,DELETE}
AS
TriggerCode
```

AFTER triggers will be called after an action e.g. after a record is inserted into a table.

INSTEAD OF triggers in according to their name are called instead of original actions e.g. instead of inserting the records into a table/view they are defined for.

## Slide 14: Trigger - example

```sql
CREATE TRIGGER InsertOrder ON Orders AFTER INSERT 
AS
 DECLARE @customer varchar(100)
 SET @customer=(SELECT CustomerId FROM inserted)
 UPDATE Customers SET OrderCount=OrderCount+1 
 WHERE CustomerId=@customer
```

1. This code assumes that one order is inserted by an INSERT statement.
2. Recall that multiple records can be inserted at the same time by using INSERT ….. SELECT …..
3. Sample code comes from Ms SQL Server
4. The trigger will be executed AFTER processing each INSERT requested on Orders table

## Slide 15: Regular execution

- Modern DBMS run continuously
- They offer built-in capability of executing different actions on regular basis e.g. every hour
- Thus, stored procedures can be also executed automatically – for instance every night to transfer temporary data between the systems, remove out-of-date information etc.
- In Ms SQL Server, SQL Server Agent is the service responsible for managing jobs

## Slide 16: Sample job – Ms SQL Server

Screenshot of the Ms SQL Server "New Job" / "New Job Step" dialog windows.

The "New Job" window (annotated: **Defining the first step of the job**) has a "Select a page" panel listing: General, Steps, Schedules, Alerts, Notifications, Targets. Connection panel: Server MACIEKNTB\START; Connection MACIEKNTB\maciek; "View connection properties". Progress: Ready.

The "New Job Step" window (annotated: **Defining the task to be executed in this step (here: executing a procedure; note that different step types exist)**) shows:
- Select a page: General, Advanced
- Step name: `Archive jobs`
- Type: `Transact-SQL script (T-SQL)`
- Run as: (empty dropdown)
- Database: `Northwind`
- Command: `execute archiveorders 13`
- Buttons: Open…, Select All, Copy, Paste, Parse
- Connection panel: Server MACIEKNTB\START; Connection MACIEKNTB\maciek; "View connection properties". Progress: Ready.
- Buttons: OK, Cancel

> Jobs can be composed of multiple steps of different categories including the execution of operating system commands. Note: jobs can be created also programmatically with Transact-SQL. See: https://learn.microsoft.com/en-us/ssms/agent/create-a-job?view=sql-server-ver16#how-to-create-a-job-using-transact-sql-t-sql

## Slide 17: SP, triggers and functions

- Enable the most efficient form of data processing – thus are useful when time really matters
- Can be used by multiple applications and ensure consistent processing
- Triggers can help perform the same actions no matter if the CRUD statement was issued from one application or another

## Slide 18: Execution plans

- While the same or similar code as in SP could be used in an ad hoc statement, SP can take advantage of execution plan
- DBMS may maintain execution plans for SP that further decrease execution time by:
  - Caching the best predicted method of accessing data and performing requested operations for an entire SP compiled and analysed beforehand.

## Slide 19: Summary

- Stored procedures and functions executed in DBMS platform provide the most efficient data processing
- Furthermore, they make it possible to share the same functionality among a number of client applications
- The key limitation is limited portability of the code. Key DBMS platforms rely on their own languages

## Slide 20: Pytania ?

Zapraszam w trakcie wykładu i w trakcie konsultacji

Miejsce i termin konsultacji - na stronie:
https://pages.mini.pw.edu.pl/~grzendam/pl/dydaktyka.html

## Slide 21: Questions?

I am looking forward to your questions during the lectures (including now) and during my office hours

For details on my office hours, please check my website:
https://pages.mini.pw.edu.pl/~grzendam/eng/dydaktyka_eng.html

## Slide 22: Project funding

MSc program in Data Science has been developed as a part of task 10 of the project „NERW PW. Science - Education - Development - Cooperation" co-funded by European Union from European Social Fund.
