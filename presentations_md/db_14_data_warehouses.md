# Hurtownie danych i systemy Business Intelligence / Data warehouses and Business Intelligence systems

## Slide 1: Title

dr hab. inż. Maciej Grzenda, prof. uczelni
M.Grzenda@mini.pw.edu.pl
http://www.mini.pw.edu.pl/~grzendam

Politechnika Warszawska
Wydział Matematyki i Nauk Informacyjnych

Hurtownie danych i systemy Business Intelligence
Data warehouses and Business Intelligence systems

## Slide 2: Project funding

MSc program in Data Science has been developed as a part of task 10 of the project
„NERW PW. Science - Education - Development - Cooperation”
co-funded by European Union from European Social Fund.

## Slide 3: Challenges related to long-term analysis of data

- What if we want to analyse long-term trends for an entire organization—for example, an entire company—but:
  - the organization's data is spread across many databases,
  - these databases are managed by different database management systems,
  - and some of the historical data in those databases is routinely deleted over time?
- For example, we may want to determine whether the financial benefits introduced two years ago—recorded in the human resources database running on Oracle—had any effect on reducing product quality issues, which are tracked in the production database managed by MS SQL Server.
- Ideally, we should also let business users analyse enterprise-wide data coming from different databases

The answer to these questions is: use data warehouses (pl. hurtownie danych) and Business Intelligence software

## Slide 4: OLTP vs. OLAP

- OLTP – On-Line Transaction Processing
- OLTP system – a system used to process transactions in an on-line manner i.e. a system serving to collect and manage everyday business data. These are the systems we have focused so far
- OLAP – On-Line Analytical Processing
- OLAP system – a system used to support decisions by analysing the data rather than focusing on handling multiple concurrent transaction. It turns out it should rely on other data models than those used by OLTP systems.

## Slide 5: Data warehouse (DWH) - idea

Selected data from a number of databases used by an organisation is extracted, transformed and loaded into a data warehouse. ETL (Extract Transform Load) or ELT systems can be applied to handle this process. There is no need to transfer the data in an on-line manner as data warehouse is used to observe trends in the data and aggregate values. For this sort of queries having the data from the last hour is not needed.

**Diagram:** Four source database cylinders at the top — Database#1, Database#2, Database#3, … Database#n — all feed downward into a central "ETL/ELT process" box. The ETL/ELT process box feeds down into a "Data warehouse" cylinder at the bottom.

Annotation (callout box): "Data from source systems can be extracted, transformed and loaded (ETL) into a data warehouse or extracted, loaded and transformed (ELT process)"

## Slide 6: Data warehouse – typical queries

- Some of the queries:
  - Total sales of groups of products per a month
  - Total income per a company division over different periods
  - Volume of sales per a country and region over different periods
  - Total number of customer complaints for individual months, product groups and regions
  - Ranking of products sorted by total income grouped by quarters and years
  - …

## Slide 7: Data warehouse – key features

- A data warehouse:
  - Contains corporate historical data including the data in many cases not available any more in OLTP databases, as these data are not needed there already
  - Includes high-quality data carefully integrated from many data sources to make it possible to monitor the performance of an organisation
- Hence, the data present in a data warehouse are particularly useful for:
  - analysis and visualisation with Business Intelligence software,
  - statistical processing and data mining techniques

## Slide 8: Data warehouse – performance issues

- Data warehouse:
  - is optimised for reporting, unlike OLTP systems which are optimised for data modification
  - can contain additional redundant structures to speed up typical queries e.g. total sales per a month
- The data structures in a data warehouse (DWH) are the outcome of dimensional modelling (pol. modelowanie wymiarowe). They are frequently denormalised to improve performance
- Furthermore, they are simplified, which makes queries and reporting easier
- Therefore, data warehouse typically does not use the same data structures as the OLTP system providing data for it

## Slide 9: Data warehouse and source databases - an example

**Diagram:** Four source database cylinders across the top:

- Sales — Data from last year
- HR
- Inventory — Data from last 2 years
- Production

All four point with arrows downward into a single large cylinder:

- Data warehouse — Data from last 10 years

## Slide 10: Systems – key terms

**Diagram:** A vertical stack of layers, with each layer connected upward to the next:

- Production database#1, Production database#1, Production database#1, … Production database#n (bottom row of source databases)
- ETL/ELT system
- Data warehouse
- OLAP system
- Business Intelligence (BI) system (top)

Annotations (callouts pointing to layers):

- **Business Intelligence (BI) system:** Software tools used primarily by business administrative staff to navigate through the data warehouse. Include reporting, querying, data analysis and data visualization. Can use data from OLAP platforms e.g. from data cubes or directly from data warehouses
- **OLAP system:** Database systems that primarily involve aggregating large amounts of data in a data warehouse
- **ETL/ELT system:** Systems used to Extract data from operational sources, Transform data for import into the data warehouse, and Load the transformed data into the data warehouse

## Slide 11: References and further reading

1. Adamson, Christopher, The complete reference : star schema, McGraw-Hill Companies, 2010 (dimensional modelling, ETL)
2. Hoberman, Steve, Data Modeling Made Simple, Technics Publications 2016 (dimensional and relational modelling)
3. Kimball, Ralph and Ross, Margy, The Kimball Group Reader: Relentlessly Practical Tools for Data Warehousing and Business Intelligence, Second Edition, Wiley, 2016 (available as an e-book via Main Library portal available at https://bg.pw.edu.pl/, dimensional modelling)
4. Simon, Alan, Enterprise Business Intelligence and Data Warehousing: Program Management Essentials, Morgan Kaufmann, 2014 (available as an e-book via Main Library portal available at https://bg.pw.edu.pl/)
5. Howson, C., Successful Business Intelligence. Unlock the value of BI and Big Data, McGraw Hill, 2nd Ed., 2014
6. Ward, A., Oracle Business Intelligence Enterprise Edition 12c - Second Edition: Build your organization's Business Intelligence system 2nd Edition, Packt, 2017

1. What should be emphasised is that some people tend to use the name Business Analytics instead of BI.
2. Moreover, BI is used in some cases to refer to the whole technical architecture, while other people tend to use is for front-end part of the entire architecture only. C. Howson makes a discussion of these terminology issues.

## Slide 12: Business intelligence

- To have a data warehouse does not mean to have a BI system.
- A key part of BI deployment are the tools that let users transform data into useful information [Howson2014, Root2012]. This relies on efficient:
  - Data warehouse (DW),
  - Reporting mechanisms

1. Terminology issues affect also data warehouse.
2. A database designed for reporting with one or many centralised fact tables, measures and optional supporting dimension tables is considered a DW [Root2012]. However, data mart, data silo or data factory are other names used in this context [Root2012].
3. Unlike DW, data mart usually serves the needs of a part of, rather than entire organisation.

## Slide 13: BI: sample view types

**Diagram:** Screenshot of an Oracle Business Intelligence dashboard in a browser, with KPI tiles (e.g. 3.3%, 2,500, 3.21), a "Revenue by Year" bar chart, and a "Monthly Revenue Trend" line chart, plus a left-hand navigation panel.

Annotations (callouts):

- Dashboard with a number of tabs
- Interactive figures with drill-down capabilities
- Interactive tables with drill-down capabilities

## Slide 14: Data warehouse – key terms

- **Fact** – data element used to measure business performance.

  Examples:
  - records of sales, purchase, product delivery, production,…
- **Dimension** – an attribute or a set of hierarchical attributes, used to group facts.

  Examples:
  - time (decomposed to year/quarter/month/week/day)
  - location (based on country, region, city an district attributes)
  - organisation (company, branch, division, department)
- **Measure** – typically a numerical attribute of fact, used as a measure of business performance.

  Examples:
  - Sales in USD
  - Income in USD
  - Number of customer complaints
  - Number of labour hours

Relational data modelling (which we discussed so far) is about capturing how the business works. Dimensional data modelling is the process of capturing how the business is monitored [Hoberman, 2016] and is used to develop data models for data warehouses.

## Slide 15: Data warehouse – key structures

- **Fact table** – a table containing business facts. Typically the following attributes comprise on the fact table:
  - date of record e.g. date of sales fact, provides for date dimension
  - a number of measure attributes,
  - a number of dimension attributes of foreign keys to dimension tables
- Fact table usually contains large number of records possibly describing many years of organisations history. Thus, text based descriptive columns, large binary fields and other irrelevant attributes may be not present in a fact table
- **Dimension table** – any related table used to describe the data in facts table by providing dimension attributes.

  Example:
  - Table containing proper city names in case only numerical city identifiers exist in fact table

## Slide 16: Sample simplified dimensional model

**Diagram:** A star schema with a central fact table and two dimension tables.

- **Order_facts** (Fact table) — columns: OrderID (PK), CustomerID, OrderDate, RequiredDate, ShippedDate, Freight, ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry, ProductID (PK), UnitPrice, Quantity, Discount
- **Customers** (Dimension table) — columns: CustomerID (PK), CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax
- **Products** (Dimension table) — columns: ProductID (PK), ProductName, CategoryName, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued

Relationships: Order_facts.CustomerID relates to Customers.CustomerID (many-to-one); Order_facts.ProductID relates to Products.ProductID (many-to-one).

This model is an example of a star schema i.e. a fact table surrounded with dimension tables. Dimension tables in star schema do not refer to other tables.

## Slide 17: Data cube - example

**Diagram:** A 3-dimensional OLAP data cube.

- **Location dimension** (left axis): France, Germany (with West / East sub-levels)
- **Product dimension** (bottom/front axis): Monitors, Notebooks
- **Time dimension** (depth axis, going back into the cube): 01/2015, 02/2015, 03/2015

Sample cell values shown on the front face:

- 100 USD
- 9900 USD (label reads "9900 USD")
- 1232 USD (front-left cell, Monitors)
- 2345 USD (front cell, Notebooks)

A cube is a primary data structure used by OLAP systems to ensure efficient data processing.

## Slide 18: Data cube - definition

- A multi-dimensional representation of business data:
  - each cell represents measure value
  - each edge denotes dimension attribute
  - Cube is built on the table of facts and some dimension tables
- In reality, includes frequently:
  - more than 3 dimensions
  - more than one measure
  - a number of hierarchical dimensions allows to drill down any part of a cube to find the data of interest e.g. total sales of LCD monitors made in February 2014 in Berlin

## Slide 19: Measures

For measure and dimension combination an aggregation method can be defined. The most frequently used aggregation method is a sum. Remaining methods include:

- Average,
- Weighted average,
- Weighted sum,
- Minimum,
- Maximum,
- First,
- Last,
- Count

Notice: every time the aggregate function will be calculated for all the facts in a cell, for instance: the number of sales records for Germany in January 2017. A fact could be invoice detail record that refers to one product or order detail record in case orders are considered.

## Slide 20: Sample visualisation with cube data in a BI interface

**Diagram:** Screenshot of a BI cube-design / pivot interface. A left-hand tree lists the cube objects (Order_data, Customers, Order facts, Products). The main area shows a cross-tab report with "Country ▸ City" columns (Argentina, Belgium, Brazil, Canada, …) and rows grouped by "Category Name ▸ Product Name" (e.g. expandable "Beverages" group with products such as Chai, Chang, Chartreuse verte, Côte de Blaye, Guaraná Fantástica, Ipoh Coffee, Lakkalikööri, Laughing Lumberjack Lager, Outback Lager, Rhönbräu Klosterbier, Sasquatch Ale, Steeleye Stout, plus other category groups Condiments, Confections, Dairy Products, Grains/Cereals, Meat/Poultry, Produce, Seafood), with numeric measure cells (Order Facts Count) at the intersections.

To get such a report, we simply drag and drop measures and dimensions from a data cube and drill down by clicking on hierarchical dimensions e.g. to see the details on the sales of Beverage products.

## Slide 21: BI solution life cycle

**Diagram:** A circular life-cycle flow (clockwise):

1. Interview and Identify Data →
2. Plan BI solution →
3. Create data warehouse →
4. Create ETL Process →
5. Create Cubes →
6. Create reports →
7. Test and Tune the Solution →
8. Approve, Release and Prepare for next version →
(back to "Interview and Identify Data")

Source: [Root2012]

Even before data investigation is made, requirements should be analysed. Equally importantly, creating a data warehouse combined with ETL process is not a final step, since front-end part i.e. interactive data presentation is needed.

## Slide 22: Summary

- Unlike source databases frequently focused on different aspects of running an organisation such as production, sales or accounting, a DWH provides a "big picture"
- Importantly, the data in a data warehouse are high quality data
- Data analytics based on DWH is significantly simplified, as time-consuming data integration and cleansing can be largely eliminated
- Therefore, DWH is a perfect data source for:
  - Business Intelligence systems enabling business users to develop their own reports
  - Analytical departments and data scientists doing even more sophisticated reporting and analytical tasks

## Slide 23: Pytania ?

Information Sensitivity: General\External

Pytania ?

Zapraszam w trakcie wykładu i w trakcie konsultacji

Miejsce i termin konsultacji - na stronie:
https://pages.mini.pw.edu.pl/~grzendam/pl/dydaktyka.html

## Slide 24: Questions?

I am looking forward to your questions during the lectures (including now) and during my office hours

For details on my office hours, please check my website:
https://pages.mini.pw.edu.pl/~grzendam/eng/dydaktyka_eng.html

## Slide 25: Questions?

I am looking forward to your questions during the lectures (including now) and during my office hours

For details on my office hours, please check my website:
https://pages.mini.pw.edu.pl/~grzendam/eng/dydaktyka_eng.html

## Slide 26: Project funding

MSc program in Data Science has been developed as a part of task 10 of the project
„NERW PW. Science - Education - Development - Cooperation”
co-funded by European Union from European Social Fund.
