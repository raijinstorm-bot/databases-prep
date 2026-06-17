# Big Data: key solutions and data storage platforms
*(Big Data: kluczowe rozwiązania i platformy składowania danych)*

**Author:** dr hab. inż. Maciej Grzenda, prof. uczelni
M.Grzenda@mini.pw.edu.pl
http://www.mini.pw.edu.pl/~grzendam
Politechnika Warszawska — Wydział Matematyki i Nauk Informacyjnych

---

## Slide 2: MSc program acknowledgement

MSc program in Data Science has been developed as a part of task 10 of the project
„NERW PW. Science - Education - Development - Cooperation"
co-funded by European Union from European Social Fund.

---

## Slide 3: Objectives

- Major growth of data resources revealed limitations of traditional database platforms, relational databases and OLTP systems
- Big Data storage and analytics require largely different solutions and platforms
- Hence, new software systems focused on Big Data processing have been developed
- The objective of this lecture is to discuss:
  - what Big Data is
  - the key ideas behind first Big Data projects and lessons learned since then
  - the key systems used to store Big Data that can complement existing DBMSs

---

## Slide 4: Resources

- **[BIG_DATA_REVOL]** Mayer-Schonberger, V., Cukier, K, *Big Data – A Revolution That Will Transform How We Live, Work, and Think*, Houghton Mifflin Harcourt, USA, 2013
- **[GOOGLE_FLU]** Mohebbi M. H. et al., *Detecting influenza epidemics using search engine query data*, Nature, vol. 457, 2009
- **[KLEPPMANN2026]** Kleppmann, M. *Designing Data-Intensive Applications. The Big Ideas Behind Reliable, Scalable, and Maintanable Systems*, O'Reilly, 2026 (*Przetwarzanie danych w dużej skali : niezawodność, skalowalność i łatwość konserwacji systemów*, Helion, 2018)
- **[Lazer2014]** D. Lazer et al., *The Parable of Google Flu: Traps in Big Data Analysis*, Science, Vol. 343, Issue 6176, pp. 1203-1205, 2014
- **[Marr2018]** B. Marr, *How Much Data Do We Create Every Day? The Mind-Blowing Stats Everyone Should Read*, Forbes, 2018
- **[Matza2017]** S. C. Matza, M. Kosinski, G. Navec, and D. J. Stillwell, *Psychological targeting as an effective approach to digital mass persuasion*, available at https://www.pnas.org/content/pnas/114/48/12714.full.pdf, 2017

---

## Slide 5: To start from: case study and standard approach

- Case study: calculating the number of disease cases
- Standard approach:
  - The process:
    - In the USA, Centers for Disease Control and Prevention (CDC) requested doctors to inform them of new flu cases.
    - The data was submitted, and processed. Reports 1-2 weeks out of date were produced. Reasons:
      - people have to consult doctors first,
      - Data collection, possible cleaning and report publication takes time
  - The database perspective:
    - Most likely standard relational DBMS is used to collect and process high quality data, based on the features (tables and columns) designed by domain experts (here: medicine experts)

*Further details: Mohebbi M. H. et al., Detecting influenza epidemics using search engine query data, Nature, vol. 457, 2009*

---

## Slide 6: Case study: big data approach

- The process:
  - Google takes 50 million most common search terms typed into Google's search engine in the USA
  - They use the data for 9 regions that USA is composed of; the regions are defined proposed in CDC reports
  - They use CDC data for 2003-2008 period to build 450 million mathematical models to test search terms and search for the correlations between search terms and flu spread. In each logit model, one query is tested
  - No domain knowledge (here: medicine) involved in model construction
  - They find 45 search terms with strong correlations with CDC data
  - Next a linear model is developed based on these 45 variables. It yields a mean correlation of 0.90 (min=0.80, max=0.96, n=9 regions) with real flu data [GOOGLE_FLU]

---

## Slide 7: Case study - consequences

- Result: Google could predict flu spread-out in near-real time, even before people consult their doctors.
- This could be done at the level of individual states.
- In 2009 H1N1 flu crisis, Google's system turned out to be more useful and timely than official statistics
- The database perspective:
  - Large volumes of data of unknown quality and definitely noisy,
  - large processing power used to develop conclusions not available before,
  - No domain knowledge, human expertise etc. involved

---

## Slide 8: Google's prediction vs. government data

**Figure — "United States Flu Activity" line chart (Historical estimates):**
- Title bar: "Historical estimates" — "See data for: United States"
- Y-axis: Influenza estimate (Influenza-like illness (ILI) data provided publicly by the US Centres for Disease Control)
- X-axis: years 2004, 2005, 2006, 2007, 2008, 2009
- Two overlaid series:
  - **Google Flu Trends estimate** (blue line)
  - **United States data** (red/orange line)
- The two series track each other closely with recurring seasonal flu peaks across the years.

*Source: http://www.google.org/flutrends/intl/en_gb/about/how.html*

The Google Flu service is no longer active. The limitations of Google Flu project, which exemplify lessons learned from early Big Data project have been discussed inter alia in [Lazer2014].

---

## Slide 9: Lessons learned from early Big Data projects

- Initial assumption that no domain knowledge is needed in Big Data projects, was soon shown to be wrong
- Spurious correlations may occur, making the models vulnerable to such false dependencies
- As an example, the number of flu cases turned out to be correlated with queries referring to "high school basketball"
- Furthermore, dependencies in the data may start to evolve. The advent of health services disturbed the number of health–related queries increasing model errors
- Traditional models not relying on Big data my not suffer from this problem

*https://www.tylervigen.com/spurious-correlations is an example of a website collecting spurious correlations – a humorous warning for anyone just relying on correlations to predict future trends.*

---

## Slide 10: Big data – formal definition?

After discussion the following definition was adopted by the industry:

> **Big data is high-volume, high-velocity and/or high-variety information assets that demand cost-effective, innovative forms of information processing that enable enhanced insight, decision making, and process automation.**

*Source: http://www.gartner.com/it-glossary/big-data/*

Big Data is sometimes referred to 3Vs data.

---

## Slide 11: Key novel aspects: change from why to what?

Diagram — two parallel vertical flows comparing approaches, labeled by data quantity:

**TRADITIONAL APPROACH** (downward flow):
1. Design experiments/survey — Avoid too many variables not to confuse the model — Use expert's knowledge
2. Develop models
3. Develop theory explaining the data, theoretical formulas explaining the process and linking the knowledge to the theory of the field

**BIG DATA APPROACH** (downward flow):
1. Get as much of the data as possible
2. Develop possibly many models
3. Find the best model(s) explaining the data and use them as black boxes

*This is how Big Data projects were initiated at the beginning. Growing awareness of the benefits of involving domain knowledge (and the risks arising from not doing so) has been observed since then.*

---

## Slide 12: Key novel aspects: volume of digital data

- Dramatic increase of data volume and digital data availability
- As of 2018, Google was processing 3.5 billion searches per day [Marr2018]
- Even more importantly, the proportion of digital information has largely changed:
  - In the year 2000: 25% of stored information was digital, the rest was analogue (paper-based, magnetic tapes etc.)
  - In the year 2013: 98% of stored information was already digital

---

## Slide 13: Key novel aspects: volume of data and qualitative changes

- Analysis never possible before can now be easily done thanks to new data including data on users interests (books just browsed and bought), thoughts (twitter), opinions (Facebook likes)
- By processing entire data sets rather than samples, we can identify new subcategories, and submarkets
- Sampling was used to reduce the cost of data acquisition and processing. In many cases it is not needed any more
- Examples:
  - Amazon's data on user interests: books browsed, books purchased,
  - No need for sampling user's interest
  - New tools combined with hardware capabilities make the processing of large volumes of data possible
  - Consequence: long tail model (submarkets), cross-sale models and much more.

---

## Slide 14: Distribution of sales of products by internet retailers

**Figure — long-tail distribution curve:**
- Y-axis: **Quantity**
- X-axis: **Product**
- A curve starts very high on the left (a few products sold in high quantities), drops steeply, then flattens into a long tail extending far to the right along the X-axis (the "long tail").
- A green line/arrow highlights/points to the long-tail region under the curve.

*Many products are sold in small quantities i.e. contribute to long tail of the figure. Still, the overall income generated by these products can be substantial and even larger than the income generated by best selling products.*

---

## Slide 15: The long tail model

- The main idea is that the overall volume of sales of a large group of unpopular products may exceed the sales of the limited number of most successful products
- The long tail model was one of the cornerstones of the success of Amazon.com
- To successfully apply the model large quantities of data showing users' interests have to be successfully processed to suggest products of potential interest to a user

---

## Slide 16: (Section divider)

**THE CHALLENGES CREATED BY THE NEED FOR BIG DATA PROCESSING**

---

## Slide 17: Why not RDBMS: Cluster challenge for relational DBMS

- The advent of large scale web systems with millions of users (or even 1.2 billion monthly active users claimed by Facebook already in 2014 and 2.2 billion now) changed the data world
- Relational approach:
  - Scaling up i.e. providing a more and more powerful server (more memory, more CPUs,…) - not sufficient to deal with the problem,
  - Cluster of servers based on shared disk concept (see: Oracle Real Application Cluster) – still not sufficiently scalable, yet expensive
- The answer:
  - Scaling out: a cluster of commodity hardware hosts, each having its own part of data on its own storage and processing it locally, while not using relational database

1. The key driving factor behind Big Data platforms was the performance and costs limits – unacceptable for large scale processing of web data (posts, viewing history, …)
2. Once, new solutions were developed (largely inspired by Google BigTable and Amazon Dynamo solutions), new approach to more application-friendly data structures become possible, as well. This re-opened the discussion of DBMS paradigms.

---

## Slide 18: Sharding

- Based on the idea of distributing the data across multiple servers and putting different data on different servers
- Each server has its own data storage and can fully manage its subset of data. This includes creating, modifying and reading it.
- In practice, sharding is:
  - usually combined with replication to avoid having only one copy of the data
  - This combination of sharding and peer-to-peer replication is typical for many Big Data platforms.
- With a replication factor of 3, each shard is present on 3 nodes. At the same time, the cluster my include even hundreds of nodes, which largely improves performance.

---

## Slide 19: RDBMS vs. sharding approach

Diagram comparing two architectures side by side:

**RDBMS shared disk (e.g. Oracle RAC)** — Server#1, Server#2, Server#3 … Server#n all connect to a single shared **Database**:
1. Multiple database instances handle one database.
2. A few servers are typically used (2-4-…). 50 is a large installation.
3. Referential integrity is ensured
4. This results in significant communication overhead

**Sharding (e.g. Apache Hadoop)** — Server#1, Server#2 … Server#n each with its own **Data** store (Data, Data, Data):
1. Each server has its own disk storage and a part of overall data set on it
2. Typically, no referential integrity is offered.
3. Hence, the solution can be scaled from 5-10 to 100-1000s of servers
4. Communication overhead is reduced compared to RDBMS

---

## Slide 20: (Section divider)

**KEY BIG DATA PLATFORM: APACHE HADOOP**

---

## Slide 21: Apache Hadoop

- The Apache Hadoop software library is a framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. It is designed to scale up from single servers to thousands of machines, each offering local computation and storage.
- Hadoop is key platform for storing Big Data, available both as open source project and a part of commercial distributions of key Big Data vendors
- The project includes these key modules:
  - **Hadoop Distributed File System (HDFS™):** A distributed file system that provides high-throughput access to application data.
  - **Hadoop MapReduce:** A (…) system for parallel processing of large data sets.

1. Compiled partly based on http://hadoop.apache.org/
2. Note that Hadoop solutions are also developed, packaged and offered by third-party vendors such as Cloudera or Hortonworks. Such distributions are vital to meet the needs of commercial deployments.

---

## Slide 22: High level Hadoop architecture: HDFS

Diagram — Hadoop cluster topology:
- A **Master node** (containing layers: **MapReduce** / **Storage**) sits at the top right and connects via a tree of links to multiple worker servers.
- Worker nodes: **Server#1**, **Server#2** … **Server#n**, each containing layers: **MapReduce** and **Storage**.
- Below each server is its own data store (cylinder): **Data#1**, **Data#2** … **Data#n**.

*The overall disk space made available for HDFS can be seen as a single directory tree providing space for PBs of data. Every time a new file is created, its content is transferred to one of the servers (i.e. nodes). Data are saved and read from many largely independent servers in parallel.*

---

## Slide 23: High level Hadoop architecture

Diagram — same Hadoop cluster topology as the previous slide:
- A **Master node** (**MapReduce** / **Storage**) at top right connects via a tree of links to worker servers.
- Worker nodes: **Server#1**, **Server#2** … **Server#n**, each with **MapReduce** and **Storage** layers.
- Each server has its own data store cylinder: **Data#1**, **Data#2** … **Data#n** (a green arrow highlights the link between a server's processing and its local Data store).

*Not only large scale data storage is provided, but also individual data chunks can be (and are) processed locally by individual servers e.g. with MapReduce tasks. This provides unprecedented performance of the clusters.*

---

## Slide 24: The difference between a local file system and HDFS

Screenshots from an HDFS shell session, with three callout labels:

**The content of a local file system** — output of `ls`:
```
[root@sandbox ~]# ls
anaconda-ks.cfg   install.log.syslog   start_hbase.sh
build.out         sandbox.info         start_solr.sh
install.log       start_ambari.sh      stop_solr.sh
[root@sandbox ~]#
```

**The help on `ls` statement:**
```
[root@sandbox ~]# hadoop fs -usage ls
Usage: hadoop fs [generic options] -ls [-d] [-h] [-R] [<path> ...]
```

**The content of HDFS system** — output of `hadoop fs -ls /`:
```
[root@sandbox ~]# hadoop fs -ls /
Found 9 items
drwxrwxrwx   - yarn    hadoop    0 2015-10-27 12:39 /app-logs
drwxr-xr-x   - hdfs    hdfs      0 2015-10-27 13:19 /apps
drwxr-xr-x   - hdfs    hdfs      0 2015-10-27 13:06 /demo
drwxr-xr-x   - hdfs    hdfs      0 2015-10-27 12:39 /hdp
drwxr-xr-x   - mapred  hdfs      0 2015-10-27 12:39 /mapred
drwxrwxrwx   - mapred  hadoop    0 2015-10-27 12:40 /mr-history
drwxr-xr-x   - hdfs    hdfs      0 2015-10-27 13:12 /ranger
drwxrwxrwx   - hdfs    hdfs      0 2015-10-27 12:54 /tmp
drwxr-xr-x   - hdfs    hdfs      0 2015-10-27 13:22 /user
[root@sandbox ~]#
```

1. A local file system is a file system managed by an OS (Unix-like) of a node HDFS shell runs on
2. HDFS is the file system managed by Hadoop software and typically spanning many nodes of a Hadoop cluster, but seen as a single, the same file system from each node
3. Hence, the distinction between both file systems is vital for the use of HDFS shell. Moreover, HDFS shell statements by default refer to HDFS.

---

## Slide 25: HDFS: Sample shell statements

| Command | Comments |
|---|---|
| appendToFile | Appends one or many local system files to destination file system |
| cat | Copies one or many source files to stdout |
| chgrp | Change group owner of an HDFS file. This statement is reserved for a super-user or the owner of a file |
| chmod | Change permission mask of an HDFS file/files |
| chown | Change owner of a file. This is reserved for a super-user |
| copyFromLocal | Copy a local system file to HDFS location |
| copyToLocal | Copy an HDFS file to local file system |
| count | Count and display stats on the number of files and directories in HDFS path |
| cp | Copy files within HDFS |
| df | Display free space |
| du | Display disk usage |
| find | Search for HDFS files |
| get | Copy HDFS file to local file system |

---

## Slide 26: Hadoop – 5 types of data

| Data category | Objective |
|---|---|
| Social media data | Model consumer sentiment |
| IT logs incl. server logs | Predict events, detect intrusions, monitor system performance |
| Clickstream data | Understand how people move on your portal, select and possibly buy products, identify typical visit paths, improve user experience, perform granular customer segmentation |
| Sensor data | Perform predictive analytics using large scale sensor data |
| Geolocation data | Collect geolocation data such as GPS traces to optimise service delivery and reduce the cost of logistics |

1. Developed based on Hortonworks Data Sheet 5 Types of Hadoop Data
2. All these cases are about large volumes of data not really matching relational model i.e. text data, time series data, spatial data

---

## Slide 27: Hadoop: fundamental change

- At its core Hadoop offers the ability to store large volumes of raw data in files of an HDFS directory tree, with emphasis on:
  - unstructured content e.g. web documents (HTML,…)
  - and semi-structured content (e.g. log files following some syntax/templates, but not processed before placing them in Hadoop)
- In traditional data management systems, **Schema-on-Write** is the approach i.e. before placing the data in a data store, the data structures are carefully designed (tables, relations, data types).
- Hadoop relies on **Schema-on-Read** i.e.:
  - put any data you want in data store, as this is done by placing files with arbitrary content in HDFS
  - Interpret these files later to extract the data you need. Later means at the time of reading file content.

---

## Slide 28: Big data expectations and solutions

**Figure — Gartner Hype Cycle for Emerging Technologies (as of July 2014):**
- Axes: **expectations** (Y-axis) vs **time** (X-axis).
- The five hype-cycle phases along the X-axis: **Innovation Trigger** → **Peak of Inflated Expectations** → **Trough of Disillusionment** → **Slope of Enlightenment** → **Plateau of Productivity**.
- Selected technologies plotted along the curve include (approximate positions): Speech-to-Speech Translation, Autonomous Vehicles, Smart Advisors, Data Science, Prescriptive Analytics, Neurobusiness, Biochips, Internet of Things, Natural-Language Question Answering, Wearable User Interfaces, Consumer 3D Printing, Cryptocurrencies, Complex-Event Processing, Big Data, In-Memory Database Management Systems, Content Analytics, Hybrid Cloud Computing, Gamification, Augmented Reality, Machine-to-Machine Communication Services, Mobile Health Monitoring, Enterprise 3D Printing, Activity Streams, In-Memory Analytics, Gesture Control, Virtual Reality, Cloud Computing, NFC, 3D Scanners, Speech Recognition, Consumer Telematics, Virtual Personal Assistants, Digital Security, Bioacoustic Sensing, Smart Workspace, Quantified Self, Connected Home, Brain-Computer Interface, Human Augmentation, Quantum Computing, Software-Defined Anything, Volumetric and Holographic Displays, 3D Bioprinting Systems, Affective Computing, Smart Robots, etc.
- **Plateau will be reached in:** ○ less than 2 years; ◯ 2 to 5 years; ● 5 to 10 years; ▲ more than 10 years; ⊗ obsolete before plateau.

*Source: Gartner, August 2014. Cited after: http://www.gartner.com/newsroom/id/2819918*

The main idea is that expectations about big data were already in 2014 over-inflated. However, big data solutions will maintain significant position in modern IT market.

---

## Slide 29: Summary

- Big Data has largely changed data storage patterns
- Big Data processing is not only about technology. It enables novel services such as these based on large scale recommendation engines
- RDBMS platforms turned out to be not sufficiently scalable to handle Big Data
- Hence, new platforms such as Apache Hadoop enabling clusters of 100s of servers have been developed
- Still, Apache Hadoop offers a file system rather than a database platform
- Hence, other scalable platforms enabling more structured Big data storage have been developed next

---

## Slide 30: Pytania? (Questions? — Polish)

**Pytania ?**

Zapraszam w trakcie wykładu i w trakcie konsultacji

Miejsce i termin konsultacji - na stronie:
https://pages.mini.pw.edu.pl/~grzendam/pl/dydaktyka.html

*Information Sensitivity: General\External*

---

## Slide 31: Questions? (English)

**Questions?**

I am looking forward to your questions during the lectures (including now) and during my office hours

For details on my office hours, please check my website:
https://pages.mini.pw.edu.pl/~grzendam/eng/dydaktyka_eng.html

---

## Slide 32: MSc program acknowledgement

MSc program in Data Science has been developed as a part of task 10 of the project
„NERW PW. Science - Education - Development - Cooperation"
co-funded by European Union from European Social Fund.
