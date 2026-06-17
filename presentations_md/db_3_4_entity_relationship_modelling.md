# Data integrity / Integralność danych — Data models / Modele danych — E-R diagrams / Diagramy E-R

**dr hab. inż. Maciej Grzenda**
M.Grzenda@mini.pw.edu.pl
http://www.mini.pw.edu.pl/~grzendam
Politechnika Warszawska
Wydział Matematyki i Nauk Informacyjnych

---

## Slide 1: Title slide

Data integrity / Integralność danych
Data models / Modele danych
E-R diagrams / Diagramy E-R

dr hab. inż. Maciej Grzenda
M.Grzenda@mini.pw.edu.pl
http://www.mini.pw.edu.pl/~grzendam
Politechnika Warszawska
Wydział Matematyki i Nauk Informacyjnych

---

## Slide 2: Project acknowledgement

MSc program in Data Science has been developed as a part of task 10 of the project „NERW PW. Science - Education - Development - Cooperation” co-funded by European Union from European Social Fund.

*(Slide contains the project / EU funding logo image.)*

---

## Slide 3: Some challenges related to data quality

- How to ensure that the data stored in our database is high quality?
  - How to avoid problems such as multiple records with the same primary key value present in a database? This could happen due to human mistakes or errors in client applications placing data in databases.
  - How to avoid removing, e.g. a customer record to which orders refer? Could we identify who placed the order and where to ship the products then?
  - Is it better to prevent data quality issues or fix them later?

The answer: DBMS capabilities, which (if properly used) will prevent many data quality problems

---

## Slide 4: Data integrity (section divider)

Data integrity

---

## Slide 5: Data integrity

- Several aspects of integrity:
  - Entity integrity (integralność encji),
  - Referential integrity (spójność referencyjna),
  - Additional constraints (dodatkowe ograniczenia)
- Modern DBMSs, when configured properly, reject data modification statements that violate data integrity e.g. by:
  - Violating the uniqueness of a primary key
  - Violating referential integrity

---

## Slide 6: Entity integrity

- Objective: guarantee the uniqueness of a primary key throughout table records
- Solution:
  - primary key is defined for a table by the person defining the table
  - typically, a unique index, i.e. a tree-like structure used to quickly check which PK values already exist in a table, is automatically created by a DBMS as well
  - next, the DBMS monitors all the create and update operations to maintain the uniqueness of a PK. It rejects requests to modify table data that would result in having records with duplicate PK values

---

## Slide 7: Referential integrity

- Objective: guarantee that foreign keys refer to existing records identified by matching PK values
- Solution:
  - a primary key is defined for a primary key table and a foreign key is defined for a foreign key table to establish the relation
  - The DBMS monitors all the CRUD (create/update/delete) operations to maintain the relation

---

## Slide 8: Referential integrity revisited

Diagram of two related tables. The **Rooms** table holds the **Primary key**, the **Assets** table holds the **Foreign key**, and the foreign key in Assets refers to the primary key in Rooms (matching on building, room).

**Rooms** (Primary key)

| Building | Floor | Room |
|----------|-------|------|
| Main     | 2     | 213  |
| …        | ..    | …    |

**Assets** (Foreign key)

| Building | Asset_id | Room | Type  |
|----------|----------|------|-------|
| Main     | 5        | 213  | Chair |
| Main     | 7        | 213  | Table |

In the analysed case, DBMS will not allow:
- Removing a Rooms record for which an Assets record with same (building, room) exists
- Changing PK of a Rooms record for which an Asset record with same (building, room) exists
- making an Asset record refer to non-existing (building, room) in Rooms table

---

## Slide 9: Surrogate primary keys (Zastępcze klucze główne)

- A frequent practice is to replace natural primary keys with surrogate primary keys
- A surrogate primary key
  - is a PK with integer values generated from a sequence, typically 1, 2, ....
  - relies on values not used in the real world, frequently not even shown to end users
  - is a solution when no natural PK exists e.g. when enterprise asset management is implemented for the first time
  - is also frequently used in modern databases, especially when a natural PK is a composite PK

---

## Slide 10: Referential integrity – surrogate PKs in use

Diagram of two tables linked by a surrogate key. The **Rooms** table's **Room_id** is the **Primary key**; the **Assets** table's **Room_id** is the **Foreign key** referring to Rooms.

**Rooms** (Room_id = Primary key)

| Room_id | Building | Floor | Room |
|---------|----------|-------|------|
| 23215   | Main     | 2     | 213  |
| 23216   | …        | ..    | …    |
| ...      | ...       | ...    | ...   |

**Assets** (Room_id = Foreign key)

| Asset_id | Room_id | Asset | …  |
|----------|---------|-------|----|
| 423      | 23215   | Chair | …  |
| 756      | 104576  | Table | …  |

Referential integrity is absolutely necessary, when a primary key (hence, a foreign key as well) is a surrogate PK. Should room record with room_id=23215 be removed, nothing will be known about the location of asset 423.

---

## Slide 11: Additional constraints

- It is possible to define logical conditions that must be fulfilled by all the records like:
  - salary>tax to ensure that the value in salary column is greater than the value of tax for each person in a table
- These conditions are checked whenever CRUD operations are attempted on a table
- However, such conditions may depend on local configuration settings, needed by individual enterprises. Hence, a tendency to place such constraints in client applications rather than DBMSs is observed.

---

## Slide 12: Some challenges related to understanding real-life needs of the users of database systems

- Can we somehow document our understanding of business needs? Will our understanding always be correct?
- Can we somehow confirm with business experts that indeed we understand the way business works?
  - Will they be able to understand primary keys and foreign keys?
  - If so, is there a way to use less technical language and share our understanding of data needs with non-IT professionals?

The answer is: data models and entity-relationship diagrams

---

## Slide 13: Data models (section divider)

Data models

This part of the lecture is mostly based on S. Hoberman, Data Modeling Made Simple, 2nd Ed., 2016, Technics Publications

---

## Slide 14: Data model

"A data model is a set of symbols and text used for communicating a precise representation of an information landscape"
— Steve Hoberman, Data Modeling Made Simple, Technics Publications 2016

A data model:
- contains only types, not actual values such as real names, prices or VAT IDs
- contains interactions, i.e. it captures how concepts interact with each other, e.g. whether a company has one or many phone numbers
- provides a concise communication medium. A piece of paper with a data model communicates more than multiple spreadsheet files with hundreds of real records of e.g. persons, products, companies etc.

Do we need data models?

" (…) a good data model serves as a lingua franca between business and information-technology professionals. (…) Conceptual and logical data models capture the ways in which technical professionals think a business process works. Business professionals can examine these assumptions and offer corrections and refinements before code is created"
— Foreword to Steve Hoberman, Data Modeling Made Simple, Technics Publications 2016

---

## Slide 15: The categories of data models

| Model format | Idea | Comments |
|--------------|------|----------|
| **Conceptual** (model pojęciowy, ewent. konceptualny) | Conceptual data model (CDM) represents the business at a very high level | Contains only basic (frequently used by organisation) and critical (fundamental for the organisation) concepts with their definitions and relationships. Limited to one page and ca. 20 concepts of top importance e.g. for project scope. |
| **Logical** | Logical data model (LDM) represents a detailed business solution | Contains entities including all attributes, according to strict business rules and independent of technology |
| **Physical** | Physical data model (PDM) represents a detailed technology solution, optimised for a specific software or even hardware | Is a LDM modified with performance-enhancing techniques for a specific environment e.g. Ms SQL Server |

We focus on logical data models in this lecture, as these document the way organisation works in detail, while they refrain from including aspects unique for the database software (such as Oracle Database or MongoDB) to be used. Based on logical models, physical models will be developed, which will be discussed during next lectures.

---

## Slide 16: The use of data models

- Data models are used:
  - during the analysis and design phases of a project before the actual database is created,
  - to understand an existing application,
  - to understand the impact of planned changes to both business and data models,
  - to learn about the business, as a data model helps understand the way the organisation works.
- Which data model should be used depends on the needs, e.g.
  - To explain how a legacy sales application works to a team of data scientists, the model selected should be the physical data model with the following features:
    - Scope: department
    - Time: today (we focus on existing solutions not the ones planned in the future)
    - Function: application

---

## Slide 17: Entity-relationship modelling (section divider)

Entity-relationship modelling

---

## Slide 18: Terminology

- Entity – a real world object – e.g. patient, employee, order, contract, …
- Entity class a.k.a. entity type or entity set – a set of entities with the same characteristics e.g. patients of a hospital
- As organisations make decisions based on entities, they should be:
  - identified,
  - their attributes should be described,
  - their relationships have to be identified e.g. one order may refer to many products.

---

## Slide 19: Entity-relationship diagram (Diagram encji-relacji)

- Entity-relationship diagram (ER diagram) is a graphical diagram that depicts entities, their relationships and attributes
- De facto standard in data modelling as:
  - It allows for a detailed description of a data model and database structure
  - There are software tools that allow to generate CREATE TABLE statements reflecting E-R diagram (and create a database out of a diagram) and perform reverse engineering i.e. generate E-R diagram based on a database structure (e.g. Ms SQL Server database)
- Used at all stages of a database system life cycle starting from project initiation, through planning, execution, up to maintenance
- Entity-relationship diagrams can be developed both for logical and physical data models

---

## Slide 20: E-R diagram - example

ER diagram with three entities — **PRODUCT**, **PART**, and **VENDOR** — connected by labelled relationship lines:

```
   PRODUCT ───|<──── is delivered by ────o<─── VENDOR
      │                  delivers
      │
 Is composed of  o
      │
 is a part of  ─|<
      │
    PART
```

- **PRODUCT — VENDOR**: line labelled "is delivered by" (reading toward VENDOR) and "delivers" (reading toward PRODUCT). PRODUCT end shows "one and many" (bar + crow's foot); VENDOR end shows "zero and many" (circle + crow's foot).
- **PRODUCT — PART**: vertical line labelled "Is composed of" (toward PART, with a circle near PRODUCT end) and "is a part of" (toward PART end, with bar + crow's foot).

Notes:
1. Every relationship is described by a line
2. The line endings define the category of a relationship

---

## Slide 21: ER diagram – how to create it?

- Identify entities i.e. determine objects, people and relationships that need to be described in the system
- As there are many different notations for E-R diagrams, select one of them
- This lecture shows one of the standards
- A logical data model can be developed by developing an ER diagram

---

## Slide 22: Design approaches

Diagram contrasting two approaches along an axis from "General statements on the system" to "Detailed system specification":

- **Top-down**: In this case, we start from brief high-level objectives for the database system to be created.
- **Bottom-up**: In this case, we start from investigating many detailed needs of future users.

```
General statements          Detailed
on the system   ◄── Top-down ──►   system specification
                ◄── Bottom-up ──►
```

---

## Slide 23: Top-down and bottom-up

| Approach | Description |
|----------|-------------|
| **Top-down** | • Start from planned benefits, scope and objectives of your project first. Identify organisation's entities first, then capture required attributes and determine relationships.<br>• Typically used at least at the beginning of a project, since typically a project starts with e.g. a project charter defining high level project objectives. |
| **Bottom-up** | • Start from the requirements of different end users to determine different possible entities and merge them next.<br>• Try to end up with a consistent vision of a system to be created. Less frequently used than top-down. |
| **Used in reality** | Mixture of both, first top-down allows to better capture overall requirements for the system and select its architecture, while bottom-up used next helps you answer the needs of different end users and cross-check the requirements captured with top-down. |

---

## Slide 24: Top-down and bottom-up - guidelines

| Approach | Description |
|----------|-------------|
| **Top-down** | Organisation's management staff should provide business objectives for the system. Frequently economic justification for the system expressed through ROI and NPV is expected as well. It is good to start from identifying departments of an organisation to be supported by a system and entities they need. |
| **Bottom-up** | Interviews with key stakeholders of the project should provide you with their perspective on the system and its functionality. Remember to investigate the processes to be supported by the system not to be left with the users' imagination of the system. It may require a lot of experience to combine the opinions of different users into a consistent system design. |
| **Used in reality** | Usually the management defines the scope of the project, thus you start from top-down in fact. Then you verify your initial view of the system by using bottom-up and top-down. |

---

## Slide 25: Design guidelines

- Reality:
  - Frequently not a very clear role of the system to be created in an organisation
  - The system is frequently expected to optimise business processes, thus a system designer has to both:
    - design a new system
    - and participate in redefining existing business processes and procedures.
- Thus:
  - Try to determine real reasons for creating a database system and problems to be solved.

---

## Slide 26: Relations

Diagram showing a relationship line between **PRODUCT** and **VENDOR**, labelled "is delivered by". Arrows annotate the two ends of the relationship symbol:

```
PRODUCT ─────────────o<──── VENDOR
            is delivered by
           ╱              ╲
   At least part:        At most part:
   Minimal cardinality   Maximal cardinality
   of a relationship     of a relationship
```

- **At least part**: Minimal cardinality of a relationship (the symbol nearer the entity / inner symbol)
- **At most part**: Maximal cardinality of a relationship (the symbol at the line ending / outer symbol)

---

## Slide 27: Relationship cardinality

Three relationship-line ending symbols and their meanings:

- **○ (circle)**
  1. Stands for zero
  2. Used with minimal cardinality only
- **| (bar / single tick)**
  1. Stands for one
  2. Used with both minimal and maximal cardinality
- **< (crow's foot)**
  1. Stands for many
  2. Used with maximal cardinality only

---

## Slide 28: Sample relationship cardinalities

Three composite end symbols and their meanings:

- **○| (circle + bar)** — "at least 0, at most one":
  1. At least 0 at most one
  2. Simply at most one e.g. every mountain is in at most one national park
- **|| (double bar)** — "exactly one":
  1. Exactly one
  2. Every capital is a capital of exactly one country
- **|< (bar + crow's foot)** — "one to many":
  1. Stands for one to many
  2. Example: every student studies on at least one faculty (but possibly many)

---

## Slide 29: Sample diagram revisited: the need for precision

Same ER diagram as Slide 20 (PRODUCT — VENDOR "is delivered by" / "delivers"; PRODUCT — PART "Is composed of" / "is a part of"):

```
   PRODUCT ───|<──── is delivered by ────o<─── VENDOR
      │                  delivers
 Is composed of  o
      │
 is a part of  ─|<
      │
    PART
```

A good data model yields precision. Symbols and terms have a clear, unambiguous interpretation. This may require a lot of discussion, but saves much more time in the future.

Is the meaning of "product" obvious without defining it?

" (…) a good data model serves as a lingua franca between business and information-technology professionals. (…) Conceptual and logical data models capture the ways in which technical professionals think a business process works. Business professionals can examine these assumptions and offer corrections and refinements before code is created"
— Foreword to Steve Hoberman, Data Modeling Made Simple, Technics Publications 2016

---

## Slide 30: Sample diagram revisited: the risk of lost precision

A degraded version of the diagram with vague / missing labels. PRODUCT connects to VENDOR (with **no relationship label** — "Missing label") and PRODUCT connects to PART with the vague label "**have**" (shown in red):

```
   PRODUCT ───|<──────────(missing label)──────o<─── VENDOR
      │
      o
      │
    have   (vague — shown in red)
      │
   ─|<
      │
    PART
```

If the terms (such as product here) are poorly defined or have no definitions, the model remains imprecise.

Comments on the "have" label (PRODUCT – PART):
- A vague label such as "have" makes the meaning unclear
- What is the meaning of "Have parts"? Have spare parts? Are composed of parts?
- Labels such as "have", "are associated with" etc. should be avoided

Comments on the missing label (PRODUCT – VENDOR):
- Missing label
- If so, is the vendor someone who delivers this product or someone to be potentially contacted in the future to find it out?

---

## Slide 31: Recurrent relationships

A single entity **Employee** linked to itself by a recurrent (self) relationship, with the two ends labelled "is managed by" and "is a manager of":

```
        ┌────────────┐
        │  Employee  │
        └─┬────────┬─┘
          ○        ○
          │        │  is managed by
          └────────┘
        is a manager of
```

1. It is possible that an entity enters a recurrent relationship with itself
2. Frequently, this corresponds to hierarchical structures of an organisation, product etc.
3. Note that by defining a foreign key referring to the table it is located in, we can document tree-like structure in a database

---

## Slide 32: Entity description

- Entity attributes are usually written in the entity box. Frequently they correspond to column names.
- Every attribute should be assigned its domain e.g. phone numbers with (or without) country code, past dates only etc.

Example entity box:

```
┌───────────┐
│ Name      │
│ Price     │
│ VAT rate  │
│ ….        │
└───────────┘
```

Notes:
1. Notice that you may frequently determine large number of entities and attributes in an organisation.
2. When your task is to develop a database application and you work on application data model, use the system scope to determine the attributes and entities you need!
3. When you develop an application, for every entity there must be a method for providing entity instances (input screens, data import etc.)
4. What would be the domain for salary attribute?
5. Will the domain of an attribute be important for a software developer implementing input screens or a data scientist?

---

## Slide 33: Data models revisited

Hierarchy: **Data models** split into Conceptual data models (CDMs), Logical data models (LDMs), and Physical data models (PDMs).

**Conceptual data models (CDMs)**
- Contain only basic and critical to the business concepts, e.g. Customer, Product and Employee
- Note that some attributes can be so critical for business that can show up on CDMs, e.g. phone number in telco industry
- Conceptual relationships connect key concepts

**Logical data models (LDMs)**
- Entities in LDMs are more detailed than concepts in CDMs
- One concept of CDM can be represented by multiple entities in LDM
- Logical relationships are detailed business rules
- All attributes of entities and their domains are identified

**Physical data models (PDMs)** — Entities in PDMs (physical entities) are even more detailed:
- In RDBMs entities present in PDMs become tables (or views) and attributes become columns
- Physical entities contain detailed features of attributes e.g. state that CompanyName is char(50) not null
- Physical relationships become database constraints e.g. foreign keys

---

## Slide 34: The objective of data modeling: sample logical data model

Fig. 1 Sample subset of financial LDM (based on [Hoberman, 2016]).

Two entities, **Account** and **Account Balance**, connected by a "contain" relationship (Account contains Account Balance).

**Account** (Entity)
```
┌──────────────────────────┐
│ Account                  │
├──────────────────────────┤
│ Account Id               │  ← Primary key attribute
├──────────────────────────┤
│ Account Open Date        │
│ Account Name             │  ← Attributes
│ Account Bank Department   │
└──────────────────────────┘
```

**Account Balance** (Entity)
```
┌──────────────────────────┐
│ Account Balance          │
├──────────────────────────┤
│ Account Code (FK)        │  ← Foreign key
│ Close of Business Date   │  ← Primary key attributes
├──────────────────────────┤
│ Account Balance Amount   │  ← Attributes
└──────────────────────────┘
```

Relationship: Account ──┤├── contain ──< Account Balance.

Labelled callouts identify the diagram parts: **Entity**, **Primary key attributes**, **Attributes**, **Foreign key**.

A logical data model includes entities and relationships. This example relies on the notation used in [Hoberman, 2016].

---

## Slide 35: Entities - subtypes

**First example — VEHICLE entity with subtypes:**
```
┌──────────────────┐
│     VEHICLE      │
│ ┌──────────────┐ │
│ │     VAN      │ │
│ ├──────────────┤ │
│ │    LORRY     │ │
│ ├──────────────┤ │
│ │     CAR      │ │
│ └──────────────┘ │
└──────────────────┘
```
1. In case an entity contains several different subtypes these subtypes can be depicted on the diagram as well
2. Remember to describe all existing subtypes in that case

**Second example — ORDERS entity with subtypes, and a subtype in a relationship:**
```
┌────────────────────┐
│      ORDERS        │
│ ┌────────────────┐ │
│ │ SUBMITTED ORDER│ │
│ ├────────────────┤ │
│ │ ACCEPTED ORDER │ │
│ ├────────────────┤ │
│ │ FINISHED ORDER │─┼──┤├─────┤├── INVOICE
│ └────────────────┘ │
└────────────────────┘
```
The FINISHED ORDER subtype enters a relationship with the **INVOICE** entity (each end marked "exactly one" / double bar).

1. Entity subtypes may also enter relationships with other entities
2. The more details of this kind we capture, the higher the chances for a valid model i.e. matching real life

---

## Slide 36: Many to many relationships (Relacje wiele-do-wielu)

- A many-to-many relationship
  - is a relationship with "at most many" on both ends
  - is allowed in conceptual data models
  - when developing a physical model for RDBMS, should be extended with an extra entity on a diagram. Such an entity corresponds to an additional table needed in a RDBMS for the many-to-many relation.

**Before (conceptual, many-to-many):**
```
PRODUCT ───|<──── is delivered by ────o<─── VENDOR
                     delivers
```
PRODUCT — VENDOR linked directly by "is delivered by" / "delivers" with many on both ends.

**After (physical, resolved with an associative entity):**
```
PRODUCT ──┤├──┐                    ┌──┤├── VENDOR
              │                    │
              o<                  >o
               ┌──────────────────┐
               │ VENDOR_PRODUCTS  │
               └──────────────────┘
```
PRODUCT and VENDOR are each connected to the new **VENDOR_PRODUCTS** entity (one-to-many on each side).

This table (VENDOR_PRODUCTS) includes at least:
- a product identifier i.e. a FK linking it with Product table
- a vendor identifier i.e. a FK linking it with Vendor table

---

## Slide 37: Mutually exclusive relationships (Relacje wzajemnie wykluczające się)

- In some cases, when an entity enters a relationship with another entity, it can not participate in another relation
- Examples:
  - For every finished order, there can be either a receipt or an invoice
  - A customer is either a person or a legal entity

---

## Slide 38: Mutually exclusive relationships

Diagram of the **ORDERS** entity (with subtypes SUBMITTED ORDER, ACCEPTED ORDER, FINISHED ORDER) whose FINISHED ORDER subtype enters two mutually exclusive (XOR) relationships — one with **INVOICE** and one with **RECEIPT**. The two relationship lines are joined by an arc with dots placed on it, denoting the exclusive-or constraint.

```
┌────────────────────┐
│      ORDERS        │
│ ┌────────────────┐ │
│ │ SUBMITTED ORDER│ │
│ ├────────────────┤ │
│ │ ACCEPTED ORDER │ │
│ ├────────────────┤ │
│ │ FINISHED ORDER │─┼──┤├──●──┤├── INVOICE
│ └────────────────┘ │        │  (XOR arc with dots
└─────────┬──────────┘        │   joining the two
          │                   │   relationships)
        ──┤├──●───────────────┘
          │
       ┌─────────┐
       │ RECEIPT │
       └─────────┘
```

1. The line matching relationships with dots placed on them denotes: there is a XOR relationship between the two relationships
2. In this case, there is either an invoice or a receipt issued for every finished order

---

## Slide 39: Remaining relationship properties

- In some CASE tools it is possible to set additional relationship properties e.g.:
  - Cardinality of relationship greater than 1 but limited e.g. each house may have at most 2 owners,
  - In case the diagram is expected to be transformed into relational database, „cascade on delete" settings can be provided for relationships e.g. for relationship between an order and order line to delete all order lines whenever an order is removed
  - relationships regarding candidate keys (i.e. unique attribute combinations) can be further described
  - Attribute i.e. column features such as declaring which columns are NOT NULL

---

## Slide 40: Data modelling

- Data modelling is a vital step towards a fully functional database system
  - Logical data models help understand and document the way organisation works
  - ER diagrams help (and force team members to) capture and clearly document all relevant data needs and detailed relationships
  - The diagrams also help involve project stakeholders in the analysis process
  - When designing a database, data models are created (and modified) before the tables come into being. This reduces the risk of starting work on implementing a database and applications too early, i.e. without a proper understanding of the organisation.

---

## Slide 41: What is wrong here?

ER diagram with three entities: **STUDENT**, **COURSE**, **EXAM RESULT**.

```
┌─────────┐   attends                 ┌────────┐
│ STUDENT │──┤├───────────────────>o──│ COURSE │
└────┬────┘   is attended by          └────────┘
     │
   ─|<
     │
┌──────────────┐
│ EXAM RESULT  │
└──────────────┘
```

- **STUDENT — COURSE**: labelled "attends" / "is attended by"; STUDENT end is "exactly one" (double bar), COURSE end is "many" (crow's foot).
- **STUDENT — EXAM RESULT**: STUDENT connects (one) to EXAM RESULT (one-to-many, bar + crow's foot at EXAM RESULT end).

Note: Course is a component of study program. Sample courses: Programming in Python, Databases.

1. One of the things to learn is to evaluate potential solutions
2. Is there anything to fix here?

---

## Slide 42: Pytania? (Questions? — Polish)

Pytania?

Zapraszam w trakcie wykładu i w trakcie konsultacji

Miejsce i termin konsultacji - na stronie:
https://pages.mini.pw.edu.pl/~grzendam/pl/dydaktyka.html

Information Sensitivity: General\External

---

## Slide 43: Questions? (English)

Questions?

I am looking forward to your questions during the lectures (including now) and during my office hours

For details on my office hours, please check my website:
https://pages.mini.pw.edu.pl/~grzendam/eng/dydaktyka_eng.html

---

## Slide 44: Project acknowledgement (closing)

MSc program in Data Science has been developed as a part of task 10 of the project „NERW PW. Science - Education - Development - Cooperation” co-funded by European Union from European Social Fund.

*(Slide contains the project / EU funding logo image.)*
