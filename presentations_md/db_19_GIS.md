# Geodatabases and geographical information systems

**dr hab. inż. Maciej Grzenda, prof. uczelni**
M.Grzenda@mini.pw.edu.pl
http://www.mini.pw.edu.pl/~grzendam
Politechnika Warszawska
Wydział Matematyki i Nauk Informacyjnych

## Slide 1: Title

Geodatabases and geographical information systems

dr hab. inż. Maciej Grzenda, prof. uczelni
M.Grzenda@mini.pw.edu.pl
http://www.mini.pw.edu.pl/~grzendam
Politechnika Warszawska
Wydział Matematyki i Nauk Informacyjnych

## Slide 2: Funding acknowledgement

MSc program in Data Science has been developed as a part of task 10 of the project „NERW PW. Science - Education - Development - Cooperation" co-funded by European Union from European Social Fund.

## Slide 3: Introduction

- Many real-life entities are described also with their location. This includes:
  - Employees working in the field
  - Transportation networks and vehicles
  - Buildings
  - Assets comprising on utility networks such as water supply networks
  - Police units
  - Public services such as schools, swimming pools, city hall offices,….
- In many cases, location of these entities should be described with geo-coordinates rather than addresses only. Examples include: fire hydrants located in parks, power grid lines located in forest areas,….
- In such cases, geodatabases a.k.a. spatial databases (geobazy, przestrzenne bazy danych) i.e. databases with extensive support for geographic data storage and processing are needed

## Slide 4: Geodatabases

- Geodatabases are used to store records, while including their geographical coordinates and providing tools to process spatial data
- Typically, data are stored as numerical maps (mapy numeryczne), such as a map of the power grid network in the country or in one city only
- Maps are typically stored in the form of layers
- A layer (warstwa) is a collection of objects of the same category
- Examples include: a layer of rivers, a layer of buildings, a layer of address points, a layer of satellite images

Source: https://www.openstreetmap.org/

*(Figure: a screenshot of OpenStreetMap showing a street/road map of a city centre with a river running through it. A "Map Layers" panel on the right offers selectable base-map styles such as Standard, Cycle Map, Transport Map, Humanitarian, etc., each shown as a small thumbnail.)*

## Slide 5: Raster layers and vector layers

- Raster layers (warstwy rastrowe) include:
  - Scanned paper-based maps,
  - Ortophotos (aerial photos), satellite images
- Raster layers are stored as bitmaps linked to the geocoordinates of the region which a tile of a map represents. In addition, the geodatabase may include preprocessed raster images to be shown at non-default scales
- Vector layers (warstwy wektorowe). A vector layer is a collection of objects, each having its shape, geographical coordinates and descriptive attributes such as street name, city name or valve diameter and number.
- Unlike raster layers, vector layers:
  - make sophisticated queries possible
  - can be displayed at an arbitrary scale with equally high quality

## Slide 6: GIS

- Geographical Information System (GIS) (System Informacji przestrzennej) is a collection of computer hardware, software and geographic data for capturing, managing, analyzing and displaying every form of geographically referenced information, often called spatial data (source: https://www.gartner.com/en/information-technology/glossary/geographic-information-systems-gis)
- GIS is used to manage geodatabases and generate maps out of raster and vector layers
- Top providers include:
  - ESRI
  - Autodesk Inc.
  - Bentley Systems Inc.
- Business applications include:
  - Utilities (gas, water supply (sieć wodociągowa), sewer systems (systemy kanalizacyjne), hydrology, power grid (sieć energetyczna), telecoms, district heating systems (systemy ciepłownicze)
  - Marketing analysis in large organisations
  - Service optimisation in large/medium-scale organisations
  - Government incl. military solutions

## Slide 7: The architecture of a GIS system

*(Diagram: three blue boxes stacked vertically and connected top-to-bottom by large double-headed blue arrows. From top to bottom: **Client applications** → **GIS system** → **Geodatabase**. Each box has a green callout box pointing to it with explanatory text, as transcribed below.)*

- **Client applications** — A user may interact with an (optional) application such as power grid network application or directly with a generic GIS system
- **GIS system** — GIS system is responsible for saving geodata, indexing it, rendering maps in user interface, querying geodata, managing permissions
- **Geodatabase** — In the simplest case, GIS system interacts directly with geodata stored in data files i.e in raster files and vector files.

Note that geodatabase may include descriptive data such as tables stored in a relational database. Hence, for instance the colour of a parking area rendered in a client application on a map can show whether the parking is full or not. Similarly, the label on a parking area may show the number of free places dynamically retrieved from the tabular data linked to the parking object present in vector layer.

## Slide 8: GIS in practice

Note challenges faced by GIS developers such as online generation of map images based on geodata, avoiding overlapping labels, mixing raster and vector data, scalable symbols and much more. This is why one of leading commercial or open sources GIS software packages rather than in-house applications is used when a GIS is needed.

While geodata is rendered as a map, the content of the geodatabase can be also exported (here: as XML)

Source: https://www.openstreetmap.org/

*(Figure: an OpenStreetMap web page titled "Welcome to OpenStreetMap!" displaying a rendered street map of an urban area, with a highlighted/exported feature (a green line across the map) illustrating that geodata underlying the rendered map can be exported, e.g. as XML.)*

## Slide 9: Vector layers (warstwy wektorowe)

- Each vector layer, depending on the GIS system contains objects of the same or different shapes.
- Typical categories of vector layers are:
  - Polyline (linia łamana)
  - Point (punkt)
  - Polygon (wielobok)
- Problems:
  - Different coordinate systems (układy współrzędnych) were developed in the past and are still in use
  - In Poland 5+ standard coordinate systems exist
  - ESRI ArcGIS platform supports 4000+ coordinate systems

## Slide 10: Business applications

- GIS platforms used by business entities go beyond simple solutions of popular GIS platforms
- As an example a GIS system for waterworks company would have:
  - Possibly hundreds of very detailed layers in the system such as: valves, fire hydrants, water supply pipes, water purification plants, pressure reducing valves, drainage, chambers,…
  - Additional tools e.g. for simulating the impact of broken connections, outage, selecting closest valves to cut off leaking pipes, buildings not supplied with water in the case of cutting of a network section,….

## Slide 11: Maps – data storage

- Simple solution:
  - collection of files e.g. ESRI SHAPE files, RDL/DGN (CAD format), DXF (CAD format),…
  - drawback:
    - limited editing capabilities: one file can be edited by one user only
    - complicated management: thousands of files used in some installations
- Enterprise solution:
  - Geodata is stored in a standard RDBMS (Oracle, Ms SQL Server,…)
  - or managed by a Spatial extension of RDBMS
  - Many users can potentially edit the same map layer at the same time

## Slide 12: GIS – free and commercial data sets

Source: http://www.openstreetmap.org/

Some geodata are publicly available. This includes OpenStreetMap and open data made available by government and cities. Many data sources are expensive to get. This includes satellite images, maps created out of historical data of the enterprises, data purchased from other organisations.

*(Figure: an OpenStreetMap web page showing a colourful rendered map of a riverside city area, with a left-hand panel listing legend entries (Szukaj / search, Pomoce, etc.) and toolbar tabs in Polish (Edycja, Historia, Zmiany, Eksport).)*

## Slide 13: Non-commercial GIS platforms

- One of the most successful free GIS platforms is QGIS (https://qgis.org), which is an open source platform
- Similarly to other complex offerings, QGIS includes:
  - QGIS Desktop – used to edit, analyse and publish geodata
  - QGIS Server – used to publish layers through network services such as WMS and WFS services
  - QGIS Web client – used to publish GIS projects on the web i.e. make them available via web browsers

Having layers is not the same as having a GIS project. A GIS project includes references to individual layers to comprise on a map, but also complex settings defining symbols to be used (possibly different at different scales), labels to be placed on a map for vector layers (e.g. street names or house numbers), which layers should be shown at which scales, layers shown at request only; the width, style and colour of line, polygon, and point symbols, which can be also data dependent e.g. to make line width reflect pipe diameter.

## Slide 14: Sample QGIS visualisation

Source: https://qgis.org/en/site/about/features.html

Note that similarly to other GIS tools, a map image is dynamically rendered on the fly based on possibly gigabytes of data of raster and vector layers included in the GIS project.

*(This slide contains a sample QGIS map visualisation illustrating a rendered map composed of multiple raster and vector layers.)*

## Slide 15: Beyond map rendering: distinctive features of GIS

- Every map object of a vector layer is composed of spatial and descriptive data:
  - Shape (e.g. collection of points),
  - Location,
  - Attributes e.g. pipe material or the name of the river
- Hence, queries can be done both in view of spatial information (all the buildings within the distance of 100 meters from the river) and descriptive data (that are made of concrete)

## Slide 16: Queries – examples

Source: ArcEditor application

*(Screenshot: the ArcEditor desktop application with a "Layers" tree on the left (entries such as "Forecast_GridDis…") and a "Select By Location" dialog open in the centre. The dialog lets the user select features from one or more layers based on where they are located in relation to features in another layer. A dropdown labelled "that:" is expanded, showing the available spatial relationship predicates used to build a query:*
- *intersect*
- *are within a distance of*
- *contain*
- *completely contain*
- *contain (Clementini)*
- *are within*
- *are completely within*
- *are identical to*
- *touch the boundary of*
- *share a line segment with*
- *are crossed by the outline of*
- *have their centroid in*

*This illustrates that GIS queries can combine spatial relationships (e.g. intersect, within a distance, contain) with attribute/descriptive criteria.)*

## Slide 17: Sample system architecture

*(Diagram: a tiered client–server architecture.)*

- **Top tier — clients:** **Desktop client**, **Desktop client**, ….. (more), **Web client**. Arrows connect every client to the GIS Application Server.
- **Middle tier:** **GIS Application Server**, connected by several double-headed arrows (and "…..") down to the **DBMS Server**.
- **Bottom tier:** **DBMS Server**, connected by a double-headed arrow down to a database cylinder labelled **geodatabase**.

Green callout annotations:

- **Desktop clients** — Used to:
  - edit maps
  - perform sophisticated analysis and geoprocessing
- **GIS Application Server / DBMS Server** — Used to:
  - manage spatial data
  - maintain spatial indexes
  - manage versioning and long-lasting transactions
- **Web client** — Used to:
  - browse maps
  - perform typical spatial and descriptive queries
  - print maps
  - provide limited editing capabilities

## Slide 18: Sample system architecture – case study

*(Diagram: the same tiered architecture as Slide 17, instantiated with concrete ESRI/Oracle products.)*

- **Top tier — clients:** **ArcGIS**, **ArcGIS**, ….. (more), **Web client**, all connecting to the ArcGIS Server.
- **Middle tier:** **ArcGIS Server**, connected by double-headed arrows (and "…..") down to Oracle DBMS.
- **Bottom tier:** **Oracle DBMS**, connected by a double-headed arrow down to a cylinder labelled **geodatabase**.

Green callout annotations:

- (pointing to the ArcGIS desktop clients) **20 workstations**
- (pointing to the ArcGIS Server) **A single central server**
- (pointing to the Web client) **Used by 1000+ users**
- **ESRI software products have been used**

## Slide 19: Communication standards

*(Diagram: the same case-study architecture as Slide 18, with a "Network communication" bar inserted between the clients and the ArcGIS Server.)*

- **Top tier — clients:** **ArcGIS**, **ArcGIS**, ….. (more), **Web client**.
- A **Network communication** bar sits between the clients and the server; arrows connect the clients through this bar to the ArcGIS Server.
- **ArcGIS Server**, connected by a double-headed arrow (and "…..") down to **Oracle DBMS**.
- **Oracle DBMS**, connected by a double-headed arrow down to a cylinder labelled **geodatabase**.

Green callout listing the network communication options:

1. Vendor-based protocol
2. Standard feature-based service (WFS)
3. Standard image-based service (WMS)
4. …

Additional annotations:

- (pointing to the Web client) **Used by 1000+ users**
- **ESRI software products have been used**

## Slide 20: GIS – data layers

*(Diagram: a stack of overlapping map-layer rectangles (grey on top, then yellow, then black, then a large green rectangle in front). The front green rectangle is labelled **"Raster and vector map layers"**. Curly braces on the right group the stacked layers into two categories, each linked to an orange callout box.)*

- Upper group → **Base map layers (rivers, streets, buildings,…** — orange callout: **These layers may come from city server**
- Lower group → **Network map layers (e.g. water supply)** — orange callout: **These layers may come from company server**

Bottom green banner:

WMS (Web Map Service) can be used to integrate on-the-fly map layers coming from different servers of different organisations to render map images based on most recent data from different organisations.

## Slide 21: GIS Program development

*(Diagram: a 10-step vertical flowchart grouped into four phases, connected by arrows top to bottom.)*

- **Planning and Investigation**
  1. Prepare for ROI Project
  2. Identify Business Opportunities
  3. Prioritize Business Opportunities
- **Program Definition**
  4. Construct GIS Program
  5. Define Project Control
- **Business Analysis**
  6. Specify and Cost GIS Projects
  7. Estimate Benefits
  8. Create Benefits Roadmap
  9. Calculate Financial Metrics
- **Reporting**
  10. Build and Deliver Report

Cited from: Maguire D., Kouyoumjian V., Smith R., *The Business Benefits of GIS. An ROI Approach*, ESRI Press, 2008

Right-hand bullets:

- Map acquisition is frequently an expensive process as it may include:
  - Making aerial photos,
  - Scanning paper-based maps,
  - Calibration,
  - Digitisation,
  - Geocoding
- ROI calculation for a GIS project is not an easy task
- Thus, complete methodology aimed at GIS program planning has been developed

## Slide 22: ROI in GIS – utility enterprises

| Improved decision making | |
|---|---|
| RESULT1 | Better new investment and maintenance work planning thanks to detailed knowledge on existing network (e.g. water supply network) |
| RESULT2 | Heat/water production /sewage disposal optimisation thanks to mathematical modelling |
| RESULT3 | Decisions on connecting new clients made in view of the capacity of existing network systems |

| Improved business processes | |
|---|---|
| RESULT1 | Time-consuming data gathering eliminated |
| RESULT2 | Immediate reports taking into account all the spatial and descriptive features possible (e.g. all the water supply pipes with diameter 100mm, located in this area, built in the 1960s) |

## Slide 23: GIS and network modelling

*(Diagram: a vertical stack connected by blue arrows. From bottom to top: a cylinder **Geodatabase** ↕ (double-headed arrow) → **GIS** ↑ → **Mathematical modelling software** ↑ → **Analysis of network behaviour**. Orange callout boxes annotate the stack, and a final large orange box on the right gives the concluding note.)*

- (pointing to **Analysis of network behaviour**) This may result in the changes in water supply (pressures, pressure zones), heat production (temperature) etc.
- (pointing to **Geodatabase**) Maps of the network, location of individual clients
- (concluding note, right) Note that similarly to other IT systems, the benefits of GIS are not because of having the data, but because of using it for changes in real world, such as changes in the utility network

## Slide 24: Summary

- GIS systems are largely needed by organisations which work with assets and persons, which are spatially distributed
- Map interface is much more intuitive in such cases than browsing tabular data of a relational database only
- Furthermore, sophisticated queries referring to spatial data can be answered
- Importantly, location data can be the only data, which makes it possible to identify real-life objects such as valves located underground in park or forest areas
- Furthermore, due to the cost of the construction and maintenance works in the field, GIS systems should be recognised for their potential of reducing excessive costs of these works

## Slide 25: Funding acknowledgement

MSc program in Data Science has been developed as a part of task 10 of the project „NERW PW. Science - Education - Development - Cooperation" co-funded by European Union from European Social Fund.
