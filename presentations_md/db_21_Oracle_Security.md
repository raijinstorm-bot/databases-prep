# Databases and Security Issues

**dr hab. inż. Maciej Grzenda, prof. uczelni**
M.Grzenda@mini.pw.edu.pl
http://www.mini.pw.edu.pl/~grzendam
Politechnika Warszawska
Wydział Matematyki i Nauk Informacyjnych

---

## Slide 1: Databases and security issues

dr hab. inż. Maciej Grzenda, prof. uczelni
M.Grzenda@mini.pw.edu.pl
http://www.mini.pw.edu.pl/~grzendam
Politechnika Warszawska
Wydział Matematyki i Nauk Informacyjnych

## Slide 2: Project acknowledgement

MSc program in Data Science has been developed as a part of task 10 of the project „NERW PW. Science - Education - Development - Cooperation" co-funded by European Union from European Social Fund.

## Slide 3: Introduction

- Databases contain data of key value for organisations managing DBMS platforms. These include:
  - confidential business and government data
  - data protected by legal regulations; examples include:
    - personal data protected by GDPR (General Data Protection Regulation) (in Polish: RODO, Rozporządzenie o Ochronie Danych Osobowych),
    - medical records
    - data on the use of telecom services including the location of mobile network subscribers
- Hence, data stored in databases have to be protected against not only data loss, but also unauthorised access
- Modern commercial DBMS platforms offer extensive security-focused capabilities which complement security-oriented settings applied in other IT systems such as system managing network connectivity

## Slide 4: Security principles

- Data protection starts with DBMS instance protection
- Least needed privileges should be applied
  - Not used user accounts should be locked
  - Not needed privileges should be revoked
- Security policy should be followed:
  - When necessary security policy should be developed,
  - Password policy has to be configured.
- Critical operations should be audited i.e. monitored
- Patches should be applied as many intrusion are made by exploiting known, yet not fixed by IT staff vulnerabilities

> It is the responsibility of a DBA to secure an instance, the database served by it and the operating system. Importantly, DBMS solutions should be used to the largest extent possible. Attempts to re-implement them in client applications should not be a replacement for DBMS solutions.

## Slide 5: Key techniques: Oracle database

- Security in Oracle DBMS relies on:
  - User accounts with each account having its own, appropriate privileges
  - Roles, which are lists of privileges of two categories:
    - System-defined roles such as: DBA, CONNECT
    - User-defined roles
  - Privileges, which are of two types:
    - System privileges such as CREATE TABLE or GRANT ANY PRIVILEGE
    - Object privileges i.e. permissions to perform some operations on some objects e.g. execute SQL SELECT on a certain table
  - Profiles, which are linked to user accounts and can be used to set password-related policies

> It is the responsibility of a DBA to manage accounts and roles. In particular, this means granting appropriate roles to individual user accounts, linking privileges to roles, and setting profile attributes.

## Slide 6: Managing user accounts

- To unlock/lock user account:

```sql
alter user UserName account unlock
alter user UserName account lock
```

- To list accounts – both open and locked

```sql
select username,account_status from dba_users
```

- In case of open user accounts, any permissions granted to PUBLIC pseudo-user are granted to all the users

```sql
revoke execute on utl_file from public
```

> Not used user accounts should be locked. Not needed privileges should be revoked. Frequently, such not used accounts and/or permissions can be used by an intruder to get access to the data of a database and possibly modify it.
>
> As an example, with the UTL_FILE package, users can read and write operating system text files. Thus, such permissions should not be granted to everyone not to enable the use of DBMS as a backdoor for breaking into the operating system.

## Slide 7: User profiles

- A profile in Oracle DBMS can be created and assigned to a user or a number of users. This can be done to:
  - Set limits on the use of database resources
  - Define log-on and password-related constraints
- This answers the following problems:
  - A single user could consume majority of CPU resources (or other resources) e.g. by submitting a particularly demanding query(ies). As a consequence, the DBMS system (and applications using it) could stop responding, which could mean a form of Denial of Service attack.
  - An intruder could try to guess user's password by performing multiple logon requests with different possible requests.
  - Passwords should not be too simple. The notion of what "simple" means is likely to vary across different systems. Hence, a policy can be used to define expectations in this matter.

## Slide 8: User profile: sample settings

The slide shows a screenshot of a SQL query and its result grid:

```sql
select * from dba_profiles where profile='DEFAULT'
```

Result set (columns: PROFILE, RESOURCE_NAME, RESOURCE_TYPE, LIMIT):

| PROFILE | RESOURCE_NAME | RESOURCE_TYPE | LIMIT |
| --- | --- | --- | --- |
| DEFAULT | COMPOSITE_LIMIT | KERNEL | UNLIMITED |
| DEFAULT | SESSIONS_PER_USER | KERNEL | UNLIMITED |
| DEFAULT | CPU_PER_SESSION | KERNEL | UNLIMITED |
| DEFAULT | CPU_PER_CALL | KERNEL | UNLIMITED |
| DEFAULT | LOGICAL_READS_PER_SESSION | KERNEL | UNLIMITED |
| DEFAULT | LOGICAL_READS_PER_CALL | KERNEL | UNLIMITED |
| DEFAULT | IDLE_TIME | KERNEL | UNLIMITED |
| DEFAULT | CONNECT_TIME | KERNEL | UNLIMITED |
| DEFAULT | PRIVATE_SGA | KERNEL | UNLIMITED |
| DEFAULT | FAILED_LOGIN_ATTEMPTS | PASSWORD | 10 |
| DEFAULT | PASSWORD_LIFE_TIME | PASSWORD | UNLIMITED |
| DEFAULT | PASSWORD_REUSE_TIME | PASSWORD | UNLIMITED |
| DEFAULT | PASSWORD_REUSE_MAX | PASSWORD | UNLIMITED |
| DEFAULT | PASSWORD_VERIFY_FUNCTION | PASSWORD | NULL |
| DEFAULT | PASSWORD_LOCK_TIME | PASSWORD | UNLIMITED |
| DEFAULT | PASSWORD_GRACE_TIME | PASSWORD | UNLIMITED |

> `select username,profile from dba_users` can be used to find the profile of a user.
> `alter user UserName PROFILE ProfileName` is used to assign the user a profile.

## Slide 9: Password profile settings

- Include:
  - **FAILED_LOGIN_ATTEMPTS** - the number of failed logon attempts causing the user account to be locked
  - **PASSWORD_LIFE_TIME** – the number of days that will pass before a user is prompted to change the password
  - **PASSWORD_REUSE_TIME** - the number of days that have to pass before a password can be reused
  - **PASSWORD_REUSE_MAX** – the number of times that a password can be reused
  - **PASSWORD_VERIFY_FUNCTION** – PL/SQL function implementing custom password policy verification
  - **PASSWORD_LOCK_TIME** – the number of days, an account will be locked after FAILED_LOGIN_ATTEMPTS
  - **PASSWORD_GRACE_TIME** – the number of days following successful login after PASSWORD_LIFE_TIME

> By defining a number of profiles and assigning users to these profiles, detailed policies regarding password settings can be implemented.

## Slide 10: Other profile settings

The slide shows a "Create Profile" GUI dialog (breadcrumb: Database Instance: orcl > Profiles > Create Profile), with tabs **General** and **Password**.

- Name: ACCOUNTING

**Details:**
- CPU/Session (Sec./100): DEFAULT
- CPU/Call (Sec./100): DEFAULT
- Connect Time (Minutes): DEFAULT
- Idle Time (Minutes): DEFAULT

**Database Services:**
- Concurrent Sessions (Per User): DEFAULT
- Reads/Session (Blocks): DEFAULT
- Reads/Call (Blocks): DEFAULT
- Private SGA (KBytes): DEFAULT
- Composite Limit (Service Units): DEFAULT

Callout annotations pointing at the dialog fields:
- Profiles let the DBA define the limitations imposed on users' sessions. Thus, excessive consumption of [resources can be prevented]
- One of the settings is how long a connection can be idle
- Another setting is how many connections to DBMS one user can open
- Sessions reading too much data can be also prevented

## Slide 11: Auditing

- Not every action is reasonable to prevent. Some permissions have to be granted to the users to let them do their work e.g. of Data Scientists.
- In particular, DBA will be allowed to do almost anything.
- Whether permissions are not overused by a user should be monitored.
- Can be used to track:
  - selected actions of selected users and/or performed on selected objects
  - logon actions
  - both successful actions and unsuccessful attempts
  - DBA's activity
- Among other options, the access to confidential data can be monitored, including data modifications and reading

> Extensive auditing may negatively affect performance. Thus, precise settings aimed at monitoring only needed actions are needed.

## Slide 12: Auditing – database configuration

- AUDIT_TRAIL instance parameter must be set
- The parameter accepts the following settings:
  - **NONE or FALSE** – no auditing, irrespective of other settings
  - **OS** – operating system's trail file will be used to save audit trail
  - **DB or TRUE** – database table SYS.AUD$ will be used to save audit trail
  - **DB_EXTENDED** – as DB setting. In addition SQL statements with bind variables that generated audit trail are saved.

Example:

```sql
alter system set audit_trail=DB_EXTENDED scope=spfile
```

> For security reasons, AUDIT_TRAIL setting can not be changed without restarting an instance.

## Slide 13: Auditing – monitored events

- Sample commands:

```sql
AUDIT CREATE ANY TRIGGER
AUDIT SESSION
AUDIT INSERT ON HR.DEPARTMENTS
AUDIT SESSION WHENEVER NOT SUCCESSFUL
…
```

- If AUDIT_TRAIL=DB or DB_EXTENDED, audit records can be found in DBA_AUDIT_TRAIL or more specialised views

## Slide 14: Audit views

| View name | Description |
| --- | --- |
| DBA_AUDIT_OBJECT | Actions performed on database objects |
| DBA_AUDIT_STATEMENT | SQL statements |
| DBA_AUDIT_SESSION | Logon attempts – successful and/or not successful depending on the settings |

> View columns include client host machine name, date and time, name and owner of affected database object, privileges granted and revoked, text of SQL query, user name. In addition, custom triggers can be defined to monitor more precisely changes made to database records e.g. basing on column values.

## Slide 15: Value-based auditing

- In some cases, it might be important to capture the actual values inserted into a table or used to update existing records
- This can be achieved by using triggers
- Trigger-based auditing offers the greatest flexibility when tracking the values existing in a table and used to insert and update the data
- This will not help when SQL SELECT statements have to be monitored

> Trigger-based auditing may negatively affect database performance. Thus, it should be used only when necessary.

## Slide 16: Fine-grained auditing (FGA)

- Provides standard manner for monitoring SQL SELECT or DML statements affecting
  - selected tables,
  - selected rows of these tables i.e. rows matching a criterion,
  - selected columns,
  - Selected SQL statement types out of a list: SELECT, INSERT, UPDATE, DELETE
- Is obtained by creating, enabling, disabling and dropping FGA policies
- DBMS_FGA package is used to manage FGA policies

> DBA_FGA_AUDIT_TRAIL view contains the audit trail i.e. actions captured by FGA policies.

## Slide 17: Unified auditing

- Unified auditing makes it possible to capture and analyse audit records inter alia from:
  - Audit records (including SYS audit records) from unified audit policies and AUDIT settings
  - FGA audit records collected from the DBMS_FGA PL/SQL package
  - Oracle Recovery Manager audit records
  - Oracle Data Mining records
  - Oracle Data Pump
  - Oracle SQL*Loader Direct Load
- In this way, a read-only table in the AUDSYS schema in the SYSAUX tablespace makes audit records from variety of sources available in one format
- The use of unified auditing largely simplifies viewing audit records

> Note that suspicious operations can mean not only reading data from a table with SQL SELECT, but also exporting the data from the system or loading new data into the system

## Slide 18: Unsafe practices to avoid

- Software developers and data scientists are also responsible for making data secure
- Examples of unsafe practices:
  - Creating copies of data extracted from a database at user workstations
  - Storing data on portable devices
  - Developing software applications relying on a single user with excessive permissions
  - Implementing unprotected, not sufficiently protected software services, e.g. services that can execute any SQL query if asked to do so
  - Preparing code not protected against SQL code injection
  - …

## Slide 19: Summary

- To make data possibly secure multiple solutions have to be implemented. This includes, but is not limited to:
  - hardware solutions reducing the risk of data loss
  - backup policies making recovery after physical media failure, human and software errors possible
  - security policies reducing the risk of intrusion into DBMS e.g. by exploiting unused, yet not locked accounts
  - audit settings making it possible to monitor the way the right permissions granted to the right users are actually used
- Making data secure is a major objective of DBAs
- Importantly, also software developers and data scientists should contribute to data security. Creating copies of the data, not separating different roles in a client application or using accounts with excessive permissions may cause major violation of data security

## Slide 20: Project acknowledgement

MSc program in Data Science has been developed as a part of task 10 of the project „NERW PW. Science - Education - Development - Cooperation" co-funded by European Union from European Social Fund.
