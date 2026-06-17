# Relational databases (Relacyjne bazy danych)

**Author:** dr hab. inż. Maciej Grzenda
Maciej.Grzenda@pw.edu.pl
http://www.mini.pw.edu.pl/~grzendam
Politechnika Warszawska — Wydział Matematyki i Nauk Informacyjnych (Warsaw University of Technology, Faculty of Mathematics and Information Science)

## Slide 1: Title

Relacyjne bazy danych
Relational databases

dr hab. inż. Maciej Grzenda
Maciej.Grzenda@pw.edu.pl
http://www.mini.pw.edu.pl/~grzendam
Politechnika Warszawska
Wydział Matematyki i Nauk Informacyjnych

## Slide 2: Project acknowledgement

MSc program in Data Science has been developed as a part of task 10 of the project „NERW PW. Science - Education - Development - Cooperation" co-funded by European Union from European Social Fund.

## Slide 3: The first fundamental challenge

How can multiple employees efficiently share data among themselves and constantly update it?

Answer:

1. Use relational databases
2. This is the best option
3. In fact, the best option for most, but nowadays not all, data resources

## Slide 4: Relational databases

- Invented by Edgar F. Codd in 1970 and further developed during next 20 years
- Based on mathematical precise theory aiming to:
  - Increase the productivity of software development
  - Avoid ambiguity (niejednoznaczność) by preparing detailed specification
  - Provide for increased independency of programs and their data

## Slide 5: Data base

- Definition: set of data structures serving to organise and store data
- Core concept – relations (relacja), defined by the following features:
  - Each relation (table) has a unique name in a database
  - Each column has a unique name in a relation
  - All values in a column are of the same type
  - The order of columns in a table is not important

## Slide 6: Relation – continued

- Remaining features of a relation:
  - Every record in a relation must be different i.e. it is not allowed to have multiple identical records
  - The order of records is not important
  - The records are not referenced by a row index
  - Only atomic values of each column in each record can be used. Sets of values (e.g. lists) are not allowed.

**Rooms**

| Building | Floor | Room |
|---|---|---|
| Main Building | 2 | 213 |
| Main Building | 2 | 215 |
| . . . | . . . | |
| Chemistry | 4 | 452 |

## Slide 7: Primary keys (Klucze główne)

- Multiple records with the same content are not allowed => there must be a set of columns such that their values are unique for the whole table
- Such a minimal set is named a primary key (PK)

| Building | Floor | Room | … |
|---|---|---|---|
| Main Building | 2 | 213 | |
| Main Building | 2 | 215 | |
| . . . | . . . | | |
| Chemistry | 4 | 452 | |

*Primary key (here: composed of two columns) — i.e. the (Building, Floor) / (Building, Room) column set.*

## Slide 8: Candidate keys (Klucze potencjalne)

In case:

- there are multiple sets of columns such that their values are unique for the entire table
- and one set is not a part of another set – all the additional sets are candidate keys
- This is not very frequent

| Name | Surname | PESEL (Personal ID in Poland) | NIP (TAX ID in Poland) |
|---|---|---|---|
| Jan | Kowalski | 45012300561 | 521-125-33-12 |
| Anna | Nowak | 75011202561 | 521-125-33-14 |
| … | . . . | 88122300561 | 521-125-01-22 |

*PESEL = Primary key. NIP = Candidate key.*

## Slide 9: Composite key (Klucz złożony)

- Composite key – a key composed of more than one column
- Since a key must identify each record, the value of each column of a primary key must be specified
- Previous example: PESEL and NIP can not be left empty

**Composite primary key** (here: Building + Floor + Room set):

| Building | Floor | Room | … |
|---|---|---|---|
| Main Building | 2 | 213 | |
| Main Building | 2 | 215 | |
| . . . | . . . | | |
| Chemistry | 4 | 452 | |

## Slide 10: Null values

- Are used to annotate "unknown" or "not available" value in a column value
- Example: date of sale for products that have not been sold yet will be set to NULL. No proper date could be used in this context.
- But:
  - The use of NULL changes the logic of compare operations.
  - Every comparison with NULL returns false.

## Slide 11: NULL and comparisons

- Consider the following example:
  - Let there be 25 salesmen who generated an income of at least 100 USD
  - Let there be 15 salesmen who generated an income of less than 100 USD
  - What if there are salesmen who have income equal to NULL?
  - They are not included in the previous groups
  - It is not a binary true/false logic any more

## Slide 12: NULL - guidelines

- NULL is not an empty value e.g. 0 or ''
- NULL should NOT be used when empty value is required
- A decision whether NULL values are allowed is made separately for every column
- Columns should not accept NULL values unless there is a good explanation for it

**Employees**

| Name | Surname | PESEL (Personal ID in Poland) | NIP (TAX ID in Poland) |
|---|---|---|---|
| Jan | Kowalski | 45012300561 | … |
| Anna | Nowak | 75011202561 | … |
| … | . . . | 88122300561 | … |

*None of these columns should allow NULLs, but … whether this is true depends on some extra conditions.*

## Slide 13: Database design

- Core assumption - database systems like other systems should be treated as investments. The software systems can generate income or decrease the costs by:
  - Providing information for more effective decisions i.e. generating increased income or decreasing the costs,
  - Optimising business processes i.e. minimising the cost of performing these processes.
- Among project selection (and justification) methods:
  - ROI (Return on Investment, Zwrot z inwestycji)
  - NPV (Net Present Value)

  i.e. formal methods for calculating the income generated by a software project can be considered.

These methods play growing role in evaluating benefits arising from executing an IT project.

## Slide 14: Conceptual design of database – step I

- The objective: design the relations of a relational database for the problem analysed
- Step I:
  - Identify the scope of the system and system boundaries (zakres i granice systemu)
  - Example: the system for managing human resources would not include the list of fixed assets (środki trwałe) in an organisation

*There are many project managements methodologies, software engineering standards and project frameworks. However, the steps listed here should be considered in every case.*

## Slide 15: Conceptual design of database – step I

- Result – a written document defining:
  - what the system is aiming at
  - what is included in the system
  - what is NOT included
  - whether the system interacts with some other existing systems

**Diagram — "The information about a company":**

```
The information about a company
 ├── HR system (System kadrowy)         ──► [The database to be created]
 ├── Salaries (Wynagrodzenia)
 ├── Sales (Sprzedaż)
 ├── Fixed assets (Środki trwałe)
 └── …
```

The HR system / Salaries portion is what the database to be created covers; Sales, Fixed assets and others are outside its scope.

## Slide 16: Conceptual design of database – step II

- Identify crucial business processes (procesy biznesowe) to be supported by the system
- Remember: these processes must be optimised by using the software
- Example:
  - The process of generating monthly sales report
  - The process of delivering products to the clients
- Thanks to the database system:
  - No manual preparation is required (reduced cost of the process)
  - The risk of mistakes is reduced
  - The information is available on-line, thus better decisions can be made
- Avoid: fragmented support for a process of interest

## Slide 17: Conceptual design of database – step III

- Step III:
  - Determine business rules and regulations
  - Example:
    - What information must be printed on an invoice (faktura)?
    - Who is allowed to change the salary?
    - Can this document e.g. an invoice be removed or it can be cancelled by modifying its status?
    - ….

## Slide 18: Conceptual design of database – step IV

- Step IV:
  - Identify organisation's objects
  - Tips and tricks:
    - Use top-down and bottom-up approach to identify data entities like invoices, products, warehouse documents
    - Try to use organisation's terminology (identify "user objects" i.e. the objects the customer's staff is familiar with like: an invoice, an order, a purchase document, . . .)
  - Result: list of entities (possible future relations a.k.a. tables)

## Slide 19: Conceptual design of database – step V

- Step V – normalisation (normalizacja):
  - The process of designing relations (i.e. entities) so as to:
    - Eliminate redundancies in the entities (which will provide future tables)
    - Avoid possible modification anomalies
    - Redefine entities and their attributes
  - The normalisation procedure affects the attributes and the number of entities

*In this lecture, we discuss relational data modelling, which captures how the business (or an organisation in general) works. Note that dimensional data modelling capturing how business is monitored also exists. See [Hoberman, 2016] for a detailed discussion of both modelling types.*

## Slide 20: Normalisation – 1NF

First normal form 1NF (pierwsza postać normalna):

- The entity is in 1NF when it is a relation, thus the key conditions to meet are:
  - A primary key has to be present in the entity and has to be identified
  - No repeating attributes can be present i.e. non atomic values have to be eliminated.

This means that:

1. In case a non-atomic value is a list of features of a record, multiple columns have to be created out of one column
2. In case a non-atomic value is a list of other entities related to a record such as a list of rooms present in a building record, a new entity has to be developed

*Entities will become tables, assuming our data will be stored in a relational database management system such as MS SQL Server. However, at this stage, we aim to understand how an organisation works, i.e. develop a logical data model.*

## Slide 21: 1NF – an example

**Before (NOT in 1NF) — Rooms** (non-atomic "Assets" column):

| Building | Floor | Assets (type and asset identifier) | Room |
|---|---|---|---|
| Main | 2 | • Chair, 5 <br> • Table, 7 <br> • …. | 213 |
| Main | 2 | | 215 |
| . . . | . . . | | . . . |
| Chemistry | 4 | | 452 |

*Primary key = (Building, Room).*

The non-atomic Assets list is split into a separate entity (arrows show the decomposition):

**After — Rooms:**

| Building | Floor | Room |
|---|---|---|
| Main | 2 | 213 |
| … | .. | … |

*Primary key = (Building, Floor, Room).*

**After — Assets:**

| Building | Asset id | Room | Type |
|---|---|---|---|
| Main | 5 | 213 | Chair |
| Main | 7 | 213 | Table |

## Slide 22: Foreign key (klucz obcy)

**Rooms** (Primary key = Building, Floor, Room):

| Building | Floor | Room |
|---|---|---|
| Main | 2 | 213 |
| … | .. | … |

**Assets** (Primary key on top: Building, Asset id, Room; Foreign key at bottom: Building, Room):

| Building | Asset id | Room | Type |
|---|---|---|---|
| Main | 5 | 213 | Chair |
| Main | 7 | 213 | Table |

*The Foreign key (Building, Room) of Assets references the Primary key of Rooms.*

- By defining a foreign key, we declare that every combination of foreign key columns has to be present in one of the records of a referenced entity
- In this case every `(building, room)` combination present in the `Assets` table has to be present in the `Rooms` entity.

## Slide 23: Referential integrity (spójność referencyjna)

- By referential integrity we mean that every value of a foreign key is matched by a corresponding value of a primary key – present in the primary key table
- Example:
  - Every customer_id value in Orders is matched by a record in Customers table with the same value of customer_id
  - In other words, every order is linked to an existing customer
- Referential integrity can be enforced by a DBMS
- Once we define a foreign key, the DBMS will not allow:
  - Placing a record in a foreign key table (e.g. Orders) referring to a non-existing record in the primary key table (e.g. Customers)
  - Removing a record from a primary key table, which is referenced from any of possibly many foreign key tables
  - Modifying a primary key value and/or a foreign key value that would make foreign key refer to non-existing record in a primary key table

## Slide 24: Referential integrity (spójność referencyjna)

- Referential integrity is fundamental for a relational database
- A record referring to non-existing primary key value can be an orphan record.
- Orphan records should never be allowed in a database, as they mean a reference to non-existing data is made.
- Once a foreign key constraint in enforced in a DBMS, any updates to the data violating referential integrity will be rejected by the DBMS.

1. For all the reasons listed above, the identification of foreign keys is crucial to design a correct database.
2. In particular, to make a table match first normal form requirements, we frequently need to develop new tables linked with the original one via foreign keys.

## Slide 25: Normalisation – 2NF

- Second normal form (druga postać normalna) – 2NF:
  - The entity is in 2NF when:
    - It is in 1NF
    - Non-key attributes (i.e. columns not being a part of a primary key) are dependant on the entire primary key
  - Counter example:
    - Table of orders containing: `customer_id`, `order_id`, `customer_city`, `customer_country`. If `(customer_id, order_id)` is a PK, then `customer_city` depends on a part of PK i.e. `customer_id` only.

## Slide 26: 2NF – an example

**Before (NOT in 2NF) — Order:**

| customer id | order id | customer country | customer city | Other customer columns |
|---|---|---|---|---|
| ABC | 2 | Poland | Warsaw | … |
| COMP | 2 | Germany | Berlin | … |
| COMP | 56 | Germany | Berlin | … |
| COMP | 43 | Germany | Berlin | … |
| … | …. | … | … | … |

*Primary key = (customer id, order id).*

Decomposed into:

**After — Order:**

| Customer id | Order id |
|---|---|
| ABC | 2 |
| COMP | 2 |
| COMP | 56 |
| COMP | 43 |
| … | … |

*Primary key = (Customer id, Order id).*

**After — Customer:**

| customer id | customer country | customer city | … |
|---|---|---|---|
| ABC | Poland | Warsaw | |
| COMP | Germany | Berlin | |
| … | … | … | |

*Primary key = customer id.*

## Slide 27: Normalisation – 2NF (discussion)

- Counter example - discussion:
- If the 2NF rule is violated then a part of each record depends not on the entity itself. In this case it depends on the customer only, not the order.
- As a consequence, many records contain the same information i.e. the address of a certain customer (redundancy).
- Redundancy may cause inconsistency – what if we update the address of a customer in only one order record out of many records including the data of this customer?

## Slide 28: Normalisation – 3NF

- Third normal form – 3NF:
  - The entity is in 3NF when:
    - It is in 2NF
    - Non-key attributes are independent of each other. They do depend only on a primary key.
  - Counter example:
    - Entity of orders containing: `customer id`, `order id`, `employee id`, `employee name`, `employee surname`, `employee e_mail`.
    - While `employee id` is related only to an order, the `employee e_mail` attribute makes a problem.

## Slide 29: 3NF – an example

**Before (NOT in 3NF) — Order:**

| Customer id | Order id | Employee id | Employee name | … | Employee e_mail |
|---|---|---|---|---|---|
| ABC | 2 | 10 | John | | jp@cx.com |
| COMP | 2 | 10 | John | | jp@cx.com |
| COMP | 56 | 20 | Ann | | ay@other.com |
| COMP | 43 | 10 | John | | jp@cx.com |
| … | …. | … | … | | … |

*Primary key = (Customer id, Order id).*

Decomposed into:

**After — Order:**

| customer id | Order id | Employee id |
|---|---|---|
| ABC | 2 | 10 |
| COMP | 2 | 10 |
| COMP | 56 | 20 |
| COMP | 43 | 10 |
| … | … | |

**After — Employee:**

| Employee id | Employee name | … | Employee e_mail |
|---|---|---|---|
| 10 | John | | jp@cx.com |
| 20 | Ann | | ay@other.com |

*Primary key = Employee id.*

## Slide 30: Normalisation – 3NF (discussion)

- Counter example - discussion:
  - If the 3NF rule is violated then a part of each record depends not on the entity itself. In this case the `employee_e_mail` depends on employee rather than an order.
  - This is because `employee_e_mail` is not really a feature of an order
  - As a consequence, many records contain the same information i.e. the address of the employee (redundancy).
  - Redundancy may cause inconsistency – what if we update the email address of an employee in only one order record out many order records containing the data of this employee?

## Slide 31: Normalisation – 4NF

- MVD (multivalued dependency) – occurs when the value of attribute A is always associated with the same set of values of attribute B
- The entity is in 4NF when:
  - It is in 3NF
  - There are no overlapping candidate keys i.e. candidate keys sharing one or more attribute
  - There are no independent multivalued attributes in the entity (that is A determines possible values of B, A determines possible values of C, but C and B are independent)

1. 3NF is the industry standard for majority of database systems
2. 3NF is used to avoid data redundancy and is largely related to Online transaction processing (OLTP) systems. OLTP systems are expected to process a large number of changes i.e. maximise the performance of insert, update and delete operations. Typically this means systems used by end-users to constantly type in and modify new data.

## Slide 32: Sample outcome of database design, i.e. a sample logical data model

**Fig. 1 Sample subset of financial logical data model (based on [Hoberman, 2016])**

Entity–relationship diagram with two entities, **Account** and **Account Balance**, connected by a "contain" relationship:

```
Account                              ← Entity
┌─────────────────────────────┐
│ Account Id                  │      ← Primary key attributes
├─────────────────────────────┤
│ Account Open Date           │
│ Account Name                │      ← Attributes
│ Account Currency            │
└─────────────────────────────┘
            │ (one)  ── contain ──    "one account has at least one account balance"
            │ (one-and-only-one on Account side;
            │  one-or-many on Account Balance side)
Account Balance                      ← Entity
┌─────────────────────────────┐
│ Account Code (FK)           │      ← Foreign key
│ Close of Business Date      │      ← Primary key attributes
├─────────────────────────────┤
│ Account Balance Amount      │      ← Attributes
└─────────────────────────────┘
```

Relationship annotations:

- The crow's-foot notation on the Account side ("one and only one") means **one account balance is the balance of one account only**.
- The crow's-foot on the Account Balance side means **one account has at least one account balance**.
- `Account Code (FK)` is the Foreign key in Account Balance; together with `Close of Business Date` it forms the Primary key attributes of Account Balance.
- `Account Balance Amount` is an attribute of Account Balance.

## Slide 33: Databases – Computer Science and Information Systems perspective

- Selected competencies expected from Computer Science graduates:
  - Database Systems
  - Data Modelling

  Source: Curriculum Guidelines for Undergraduate Degree Programs in Computer Science, ACM

- Selected competencies expected from Information Systems graduates:
  1. Query the relational model
  2. Design relational databases
  3. Programming database systems using functions and triggers
  4. Secure a database
  5. Compare tradeoffs of different concurrency modes
  6. Develop non-relational models

  Source: Paul Leidig, Hannu Salmela, A Competency Model for Undergraduate Programs in Information Systems, The Joint ACM/AIS IS2020 Task Force

## Slide 34: Data Science perspective

**Data Science = intersection of three areas (Drew Conway-style Venn diagram):**

- Hacking skills
- Maths and statistics knowledge
- Substantive expertise

Discussion points:

- Why hacking skills in Data Science?
- Perhaps it is just enough to know ML techniques and describe possible options to IT team?
- Do enterprises prefer knowledge of the techniques only of or the ability to deliver new working solutions?
- IT teams frequently play the role of the leaders in adopting new technologies.
- What about Data Scientists? Should they be the leaders or followers?
- Data Science != Machine Learning

## Slide 35: Databases – Data Science perspective

- Selected statements describing the knowledge and skills of Data Science graduates:
  1. Methods for querying and parsing data sources
  2. Manipulate data from selected sources (e.g., databases, spreadsheets, text documents, XML) utilizing appropriate techniques (e.g., database queries, API calls, regular expressions).
  3. Techniques for creating and searching relational database systems
  4. Various relational, non-relational, and other database formats
  5. Create and use a relational database structure using SQL.
  6. The concepts and application scenarios of government database, data warehouse and mediator-based information integration -> data warehouses (hurtownie danych)
  7. An entire chapter on Big Data systems (even longer than the one for AI!)

  Source: A. Danyluk, P. Leidig, Computing Competencies for Undergraduate Data Science Curricula. ACM Data Science Task Force

Side notes:

- Data Scientist needs … data
- The best data can be found in databases
- Data stores offer data of different quality, which has a major impact on the use of ML (data complete vs. incomplete data etc.)

## Slide 36: Summary

- Relational databases are the key databases i.e.:
  - The most popular databases
  - The databases most frequently used to store the most important business data
- To correctly design a database means to match:
  - real-life opportunities (such as enabling improved support for business processes or developing a system enabling new services)
  - real-life data organisation
  - real-life requirements of end users
- Once preliminary data needs are identified, when a database is expected to enable high performance transaction processing, developing a database matching 3NF is mandatory

## Slide 37: Pytania? (Questions? — Polish)

Pytania?

Zapraszam w trakcie wykładu i w trakcie konsultacji

Miejsce i termin konsultacji - na stronie: https://pages.mini.pw.edu.pl/~grzendam/pl/dydaktyka.html

## Slide 38: Questions?

I am looking forward to your questions during the lectures (including now) and during my office hours

For details on my office hours, please check my website: https://pages.mini.pw.edu.pl/~grzendam/eng/dydaktyka_eng.html

## Slide 39: Project acknowledgement

MSc program in Data Science has been developed as a part of task 10 of the project „NERW PW. Science - Education - Development - Cooperation" co-funded by European Union from European Social Fund.
