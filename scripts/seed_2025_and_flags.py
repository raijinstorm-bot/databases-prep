#!/usr/bin/env python3
"""
(1) Seed the 2025 exam questions (authored answers + explanations + topic tags).
    These are real 2025 exam questions -> generated: false.
(2) Stamp a `generated:` flag onto every EXISTING question file that lacks one:
      - 2023-1 questions: generated: true  (real questions, but the answer
        OPTIONS were AI-generated)
      - 2024-A / 2024-B questions: generated: false
Idempotent: re-running won't duplicate the flag.
"""
import os, glob, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "questions")
os.makedirs(OUT, exist_ok=True)

Q = []
def add(num, typ, stem, options, correct, pdfs, explanation):
    Q.append(dict(num=num, typ=typ, stem=stem.strip(), options=options,
                  correct=correct, pdfs=pdfs, explanation=explanation.strip()))

E = "2025"

add(1, "multi", "Data cube:",
    [("a","is used in GIS"),
     ("b","is created in order to make it easier to browse raw data"),
     ("c","contains date dimension"),
     ("d","contains date measure"),
     ("e","typically built on top of the data present in a data warehouse")],
    ["c","e"], ["data-warehouses"],
    "An OLAP cube is a multidimensional structure built over the (aggregated) data of a data warehouse (e), and commonly includes a time/date dimension (c). Measures are numeric values (sums, counts), not dates (d); a cube serves analytical browsing of aggregated data, not raw data (b), and is unrelated to GIS (a).")

add(2, "multi", "A transaction is executed in READ UNCOMMITTED mode. When executing this transaction the programmer reads the balance contained in a certain bank account record. This means:",
    [("a","The balance of this account is guaranteed not to change during the transaction"),
     ("b","The record with the balance can be not committed yet, dirty reads can be observed"),
     ("c","Another isolation level should be used, due to the possible use of wrong data in the transaction"),
     ("d","Another isolation level should be used to speed up data processing")],
    ["b","c"], ["concurrency"],
    "READ UNCOMMITTED permits dirty reads, so the balance read may come from an uncommitted (possibly rolled-back) change (b); for financial data this is unsafe, so a stronger isolation level is advisable (c). It gives no stability guarantee (a), and higher isolation does not speed up processing (d).")

add(3, "multi", "A connection from a remote client application to Oracle database is attempted. This always requires:",
    [("a","the use of Oracle listener"),
     ("b","the use of user and password"),
     ("c","satisfying conditions defined by the user profile")],
    ["a","b"], ["oracle-net","oracle-security"],
    "A new remote connection must reach a running listener (a) and authenticate with valid credentials (b). A profile is assigned to every user, but satisfying its limits is not the universal gating requirement that establishing the connection itself is, so (c) is not the intended 'always required' condition.")

add(4, "single", "A table has been defined. Next, the need to change its structure was observed. Such a change:",
    [("a","can be always done with ALTER TABLE"),
     ("b","may require the table to be dropped and recreated"),
     ("c","is not possible without disconnecting all users")],
    ["b"], ["physical-data-models"],
    "Many structural changes work with ALTER TABLE, but not all — some require dropping and recreating the table (b). 'Always' (a) is false, and disconnecting all users (c) is not generally required.")

add(5, "multi", "Oracle database has been successfully running in NOARCHIVE mode and suggested backups were created. After the failure of disk containing data files:",
    [("a","The database can be recovered to the moment of the last whole backup of a database"),
     ("b","The database can be recovered till the moment immediately preceding disk failure"),
     ("c","Backup is not needed to recover the database"),
     ("d","Online logs will not be used to recover a database")],
    ["a","d"], ["oracle-storage-backup"],
    "In NOARCHIVELOG mode there are no archived redo logs to roll forward, so after media failure you can only restore the last whole (consistent) backup (a) and cannot apply redo to reach the point of failure (b is false); online redo logs cannot be used for this media recovery (d). A backup is essential (c is false).")

add(6, "multi", "Data warehouse:",
    [("a","contains all columns present in OLTP database"),
     ("b","is nowadays replaced by Business Intelligence platforms"),
     ("c","has higher quality data than Big Data resources"),
     ("d","typically contains data from multiple relational databases"),
     ("e","typically contains data for recent weeks only to speed up analytical processing")],
    ["c","d"], ["data-warehouses"],
    "A warehouse integrates curated data from several relational source systems (d) and, being validated/cleansed, is of higher quality than raw Big Data (c). It does not copy every OLTP column (a), is not replaced by BI tools that sit on top of it (b), and keeps long history rather than only recent weeks (e).")

add(7, "single", "A table contains 500 000 records and columns: A taking 500 000 unique values and B taking 3 unique values. Both columns are frequently used for filtering, but not together:",
    [("a","An index should be created with an index key composed of column A"),
     ("b","An index should be created with an index key composed of column B"),
     ("c","An index should be created with an index key composed of both columns A and B")],
    ["a"], ["indexes"],
    "Column A is highly selective (every value unique), so a B-tree index on A is very effective (a). Column B has only 3 distinct values (very low selectivity) — indexing it gives little benefit (b). Since the columns are not used together, a composite index (c) is inappropriate.")

add(8, "single", "A foreign key pointing from table A to table B (teachers) and relying on a single column has been defined. The column of the foreign key was set as a NOT NULL column. This means:",
    [("a","For every teacher there is at least one lecture, but possibly more"),
     ("b","For every teacher there is exactly one lecture"),
     ("c","For every lecture there is possibly more than one teacher assigned"),
     ("d","For every lecture there is exactly one teacher assigned"),
     ("e","For some lectures there may be no teacher assigned"),
     ("f","Some lectures may refer to teachers that have been already removed from the table of teachers")],
    ["d"], ["er-modelling","relational-databases"],
    "A single-column, NOT NULL foreign key from A (lectures) to B (teachers) forces each lecture row to reference exactly one existing teacher (d). NOT NULL rules out lectures without a teacher (e); a single FK column cannot reference several teachers (c); the FK constraint prevents dangling references (f); and nothing guarantees every teacher is used (a, b).")

add(9, "open", "Some of the tables of an Oracle database contain confidential data that should be browsed only by some of the system users. Occasionally, a database administrator may also have to browse it. Describe how to reduce the risk that unauthorised users will read the data and how to detect reading of the confidential data by users allowed to do so but overusing their permissions. (For extra points: describe how an SQL injection attack can be performed and how it relates to unauthorised use of data.)",
    [], [], ["oracle-security","jdbc"],
    "**Reducing the risk.** Apply least privilege: grant SELECT on the confidential tables only to the users who genuinely need it, ideally through roles rather than direct grants, and revoke everything else. Finer control can be added with views that expose only permitted columns/rows, or with Virtual Private Database / fine-grained access control and column/row-level security; sensitive columns can also be encrypted. The DBA cannot be denied access by privileges alone, which is exactly why detection is needed.\n\n**Detecting overuse.** Enable auditing on the confidential tables so that read (SELECT) access is logged, including access by privileged users and the DBA; **fine-grained auditing (FGA)** can log reads that match specific conditions (e.g. particular rows/columns) and is well suited to catching authorised-but-excessive access. The audit trail is then reviewed to spot users reading data beyond their legitimate need.\n\n**SQL injection.** If a client builds SQL by concatenating unvalidated user input (e.g. `... WHERE name = '<userInput>'`), an attacker can supply input such as `' OR '1'='1` to change the query's meaning and read data they should not see. It relates directly to unauthorised data use because it bypasses application-level access checks at the query level. The defence is **parametrised/prepared statements** (bind variables) plus input validation and least-privilege database accounts.")

add(10, "multi", "A table in the first normal form:",
    [("a","contains primary key"),
     ("b","can include values such as “London, Downing Street, 10”"),
     ("c","can contain a composite primary key"),
     ("d","can include columns that depend on a part of a primary key only")],
    ["a","c","d"], ["er-modelling"],
    "1NF requires a key (a), allows a composite primary key (c), and does NOT forbid partial dependencies — those are only removed at 2NF — so a 1NF table may still have columns depending on part of the key (d). A single column holding a whole composite address like “London, Downing Street, 10” is non-atomic and violates 1NF (b).")

add(11, "multi", "Big Data is defined as:",
    [("a","high value data"),
     ("b","high quality data"),
     ("c","high volume data"),
     ("d","high velocity data")],
    ["c","d"], ["big-data"],
    "The classic defining 'Vs' present here are Volume (c) and Velocity (d). Big Data is not defined by high quality (b), and value (a) is a later add-on rather than a defining characteristic.")

add(12, "open", "Describe the logical organisation of an Oracle database. (For extra points: describe how to use tablespaces and backups to quickly restore, after a failure, the data of e.g. 20 tables first — so users can work with the core functionality without waiting for the remaining data to be restored.)",
    [], [], ["oracle-storage-backup"],
    "**Logical organisation.** An Oracle database is organised logically into **tablespaces**, each a logical storage container mapped to one or more physical datafiles. A tablespace holds **segments** (e.g. a table or index), each segment consists of **extents**, and each extent is a set of contiguous **data blocks** — the smallest logical I/O unit. Schema objects (tables, indexes, views, etc.) belong to user schemas and are stored in segments within tablespaces. This logical layer is deliberately separated from the physical files so storage can be managed independently.\n\n**Fast partial recovery.** Place the ~20 business-critical tables in their own dedicated tablespace(s), run the database in ARCHIVELOG mode, and back up at tablespace/datafile granularity (e.g. with RMAN). After a failure you can then perform **tablespace- or datafile-level restore and recovery**, bringing the critical tablespace(s) back online first by restoring their datafiles and applying redo, while the other tablespaces remain offline and are recovered afterwards. Users regain the core functionality quickly instead of waiting for the whole database to be restored.")

add(13, "single", "A one-to-many relation has been identified between tables A and B. This means:",
    [("a","Foreign keys have to be added to both of the tables"),
     ("b","A new table with one foreign key is needed"),
     ("c","A new table with two foreign keys is needed"),
     ("d","A new table without foreign keys is needed"),
     ("e","A foreign key should be added to table B"),
     ("f","A foreign key should be added to table A")],
    ["e"], ["er-modelling"],
    "A one-to-many relationship (one A relating to many B) is implemented by placing a foreign key on the 'many' side, table B, referencing A (e). No junction table is needed — that is for many-to-many — and a single FK on B suffices, so the other options are wrong.")

add(14, "multi", "To recover an Oracle database, the following files will be useful:",
    [("a","whole backup"),
     ("b","online transaction logs"),
     ("c","vector layers"),
     ("d","archived transaction logs"),
     ("e","raster layers")],
    ["a","b","d"], ["oracle-storage-backup"],
    "Recovery uses a restored backup (a), the online redo logs (b) and, for media/point-in-time recovery, the archived redo logs (d). Vector and raster layers (c, e) are GIS concepts, unrelated to database recovery.")

add(15, "single", "A NoSQL cluster platform has been proposed to store the data. This means:",
    [("a","SQL queries will not be possible"),
     ("b","SQL queries may not be possible"),
     ("c","improved support for transactions compared to RDBMS can be expected")],
    ["b"], ["nosql"],
    "NoSQL platforms vary: many offer SQL-like query interfaces while others do not, so SQL queries 'may not be possible' (b) rather than definitely impossible (a). Distributed NoSQL stores typically provide weaker, not stronger, transactional guarantees than an RDBMS (c).")

add(16, "open", "Describe in points the differences between a table in an RDBMS such as MS SQL Server and a table in Apache HBase. (For extra points: describe whether dedicated mechanisms exist for storing multiple versions of the data in a row, whether this means versioning entire rows, and how the number of versions is set.)",
    [], [], ["hbase","nosql"],
    "**RDBMS table (e.g. MS SQL Server):** fixed schema defined in advance; every row has the same columns with declared data types; supports SQL, joins, referential integrity and ACID transactions; data is typically normalised; rows are identified by a primary key.\n\n**Apache HBase table:** a sparse, distributed, wide-column store. The schema fixes only **column families**; the actual columns (qualifiers) can differ from row to row and are added dynamically. Data is accessed by **row key** (and column family/qualifier), there are no SQL joins, and it scales horizontally across a cluster with no full relational ACID semantics. Empty cells take no space (sparse).\n\n**Versioning.** HBase has a dedicated mechanism: each **cell** (a given row key + column family + qualifier) can store **multiple versions distinguished by a timestamp**. This is per-cell, not whole-row versioning — different columns can have different numbers of versions. The maximum number of versions kept is configured per **column family** (the VERSIONS setting), and reads can return the latest or a specific historical version. A standard RDBMS table does not keep such automatic value history.")

add(17, "single", "The company needs a system that should easily answer queries such as finding all water supply pipes located at least partly in the city area defined by a polygon. This means that the company needs:",
    [("a","GIS system"),
     ("b","NoSQL system"),
     ("c","RDBMS system"),
     ("d","Apache HBase")],
    ["a"], ["gis"],
    "Finding features that lie within / intersect a polygon is a spatial query over geographic data, which is exactly what a GIS provides (a). Plain NoSQL, RDBMS or HBase do not natively offer spatial layers and operators.")

add(18, "single", "A utility company has decided to use a GIS system. It can expect a return on investment:",
    [("a","because of just buying and installing the GIS system"),
     ("b","because of running spatial queries on raster labelling of its network"),
     ("c","because of just using GIS and mathematical modelling of its network"),
     ("d","because of making better decisions thanks to the GIS system and mathematical modelling")],
    ["d"], ["gis"],
    "ROI comes from the better decisions enabled by combining the GIS with analysis/mathematical modelling of the network (d), not from merely buying/installing the software (a) or from the tools alone without acting on their output (b, c).")

add(19, "multi", "Sample NoSQL platforms include:",
    [("a","Apache HBase"),
     ("b","ESRI ArcGIS"),
     ("c","MS SQL Server"),
     ("d","MongoDB")],
    ["a","d"], ["nosql","hbase"],
    "Apache HBase (wide-column) and MongoDB (document) are NoSQL platforms (a, d). ESRI ArcGIS is a GIS (b) and MS SQL Server is a relational DBMS (c).")

add(20, "single", "A table of products has been designed which includes a primary key and a column with a list of countries in which a product is sold. Individual country names in this column are comma separated. Such a table:",
    [("a","is in the first normal form"),
     ("b","is in the second normal form"),
     ("c","is in the third normal form"),
     ("d","is not normalised")],
    ["d"], ["er-modelling"],
    "A comma-separated list in one column is a repeating, non-atomic value, which violates the very first requirement (1NF). The table therefore is not normalised (d) and cannot be in 1NF/2NF/3NF.")

add(21, "multi", "A table in the third normal form:",
    [("a","contains primary key"),
     ("b","can include non-atomic values"),
     ("c","can include one column for all address data i.e. (city, street, house number)"),
     ("d","can contain a composite primary key"),
     ("e","is also a table in the second normal form"),
     ("f","can include columns that depend on a part of a primary key only")],
    ["a","d","e"], ["er-modelling"],
    "A 3NF table has a primary key (a), may have a composite key (d), and by definition already satisfies 1NF and 2NF (e). It must use atomic values (so b and the single combined-address column c are not allowed) and must have removed partial dependencies (f violates 2NF and hence 3NF).")

add(22, "multi", "Before the list of columns for the tables planned in the relational database is developed:",
    [("a","System scope should be defined"),
     ("b","Normalization should be performed"),
     ("c","Possible high-level integration with other databases should be identified"),
     ("d","The objectives for creating the database should be specified")],
    ["a","c","d"], ["er-modelling"],
    "Defining columns is a design step that must be preceded by requirements/analysis: establishing the objectives (d), the system scope (a), and how it integrates with other systems (c). Normalisation operates on already-identified attributes/columns, so it comes afterwards, not before (b).")

add(23, "single", "Big Data is:",
    [("a","typically used with schema-on-write approach"),
     ("b","typically data of higher quality than data present in data warehouses"),
     ("c","typically carefully modelled before being placed in a system, typically being a relational database management system"),
     ("d","frequently stored in Apache Hadoop")],
    ["d"], ["big-data"],
    "Big Data is frequently stored on Apache Hadoop (d). It uses schema-on-read rather than schema-on-write (a), is generally of lower quality than a curated warehouse (b), and is ingested raw rather than carefully modelled into an RDBMS first (c).")

add(24, "multi", "The benefits of using a stored procedure compared to executing a batch of SQL statements include:",
    [("a","improved performance"),
     ("b","portability of the code among different DBMSs"),
     ("c","the ability to reduce the overhead of client-server network communication")],
    ["a","c"], ["stored-procedures"],
    "A stored procedure runs server-side, is precompiled/cached and bundles many statements into one call, improving performance (a) and cutting client-server round-trips (c). Procedural code is vendor-specific, so it is not portable across DBMSs (b).")

add(25, "single", "There is a need to put new orders into a local database and into a central database of a company. The orders can be placed in the central database with some latency in case of network connectivity issues which occasionally happen. The suggested solution is to:",
    [("a","use distributed transactions"),
     ("b","use replication from the local database to the central database"),
     ("c","put new records directly from the local application into the central database")],
    ["b"], ["architecture-patterns"],
    "Tolerating latency and occasional network outages points to asynchronous replication from the local to the central database (b). Distributed transactions require all nodes to be available synchronously (a), and writing directly to the central database fails during connectivity issues (c).")

# ---- writer ----
def yaml_list(items):
    return "[]" if not items else "[" + ", ".join(f'"{i}"' for i in items) + "]"

count = 0
for q in Q:
    qid = f"q-{E}-{q['num']:02d}".lower()
    fname = os.path.join(OUT, qid + ".md")
    L = ["---",
         f'id: "{qid}"',
         f'exam: "{E}"',
         f'number: {q["num"]}',
         f'type: "{q["typ"]}"',
         "generated: false",
         f'tags: {yaml_list([E])}',
         f'correct: {yaml_list(q["correct"])}',
         f'pdfs: {yaml_list(q["pdfs"])}',
         "---", "", q["stem"], ""]
    if q["typ"] == "open":
        L += ["### Answer", "", q["explanation"], ""]
    else:
        L += [f"- {l}) {t}" for l, t in q["options"]]
        L += ["", "### Explanation", "", q["explanation"], ""]
    open(fname, "w", encoding="utf-8").write("\n".join(L))
    count += 1
print(f"Wrote {count} x 2025 question files")

# ---- stamp generated flag onto existing files lacking it ----
stamped = 0
for path in glob.glob(os.path.join(OUT, "*.md")):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        continue
    fm = m.group(1)
    if re.search(r"^generated:", fm, re.M):
        continue  # already has it (e.g. the 2025 files just written)
    exam_m = re.search(r'^exam:\s*"?([^"\n]*)"?', fm, re.M)
    exam = exam_m.group(1).strip() if exam_m else ""
    val = "true" if exam == "2023-1" else "false"
    # insert generated line right after the type: line
    new_fm = re.sub(r"(^type:.*$)", r"\1\ngenerated: " + val, fm, count=1, flags=re.M)
    if new_fm == fm:  # no type line; append
        new_fm = fm + f"\ngenerated: {val}"
    text = text.replace("---\n" + fm + "\n---", "---\n" + new_fm + "\n---", 1)
    open(path, "w", encoding="utf-8").write(text)
    stamped += 1
print(f"Stamped generated flag onto {stamped} existing files")
