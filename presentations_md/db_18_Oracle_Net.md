# Introduction to the network architecture of Oracle DBMS

dr hab. inż. Maciej Grzenda, prof. uczelni
M.Grzenda@mini.pw.edu.pl
http://www.mini.pw.edu.pl/~grzendam
Politechnika Warszawska
Wydział Matematyki i Nauk Informacyjnych

## Slide 1: Title

Introduction to the network architecture of Oracle DBMS

dr hab. inż. Maciej Grzenda, prof. uczelni
M.Grzenda@mini.pw.edu.pl
http://www.mini.pw.edu.pl/~grzendam
Politechnika Warszawska
Wydział Matematyki i Nauk Informacyjnych

## Slide 2: Project funding acknowledgement

MSc program in Data Science has been developed as a part of task 10 of the project „NERW PW. Science - Education - Development - Cooperation" co-funded by European Union from European Social Fund.

## Slide 3: Introduction

- Oracle DBMS is an example of a complex RDBMS platform
- At the same time, it is one of the most frequently used RDBMS platforms. Hence, it is:
  - used by software developers to develop database applications
  - used by data scientists to query the data
  - managed by system administrators
- The primary objective of this lecture is to describe key components of Oracle Database platform and the way network connections with DBMS instance are established

## Slide 4: References and further reading

1. Oracle Net Services Administrator's Guide
   https://docs.oracle.com/en/database/oracle/oracle-database/26/netag/database-net-services-administrators-guide.pdf
2. Other resources e.g. at
   https://docs.oracle.com/en/database/oracle/oracle-database/

## Slide 5: Oracle instance

**Diagram:**

Outer box labeled "Oracle instance" contains:
- A row of ovals: Background Process#1, Background Process, Background Process, Background Process, ... , Background Process#n
- Below them a wide box: System Global Area (SGA)

A double-headed (up/down) arrow connects the Oracle instance box to a box below labeled "Database", which contains File, File, File, ... , File (drawn as disk/cylinder shapes).

**Caption:**
One Oracle DBMS instance handles one database only (unlike in Ms SQL Server). The core of the instance are background processes and shared memory of SGA.

## Slide 6: Oracle and client-server paradigm

**Diagram:**

Outer box labeled "Oracle database" contains:
- An inner box labeled "Oracle instance", which contains:
  - On the left: ovals "Server proces#1" and "Server proces#n" (overlapping), with a vertical double-headed arrow down to a box "Program Global Areas (PGAs)".
  - On the right: ovals "Background Process#1", "Background Process#2", ... , "Background Process#k", with a vertical double-headed arrow down to a wide box "System Global Area (SGA)".
  - A horizontal double-headed arrow connects the Server processes/PGAs area to the Background processes/SGA area.
- Below the Oracle instance, a box labeled "Database" containing File ... File (disk/cylinder shapes).
- A vertical double-headed arrow between the Oracle instance and the Database, annotated on the left "Write to data files and online redo logs" and on the right "Read data from data files".

Outside the Oracle database box, on the lower left, a box "Client application".
- An arrow connects "Server proces#1" to the "Client application", annotated: "Send: SQL statements / Fetch: results".

## Slide 7: SGA

- SGA (System Global Area): a large memory buffer where Oracle:
  - Maintains internal structures used by all processes,
  - Caches data from a disk,
  - Holds parsed SQL statements
  - Hold transaction log buffer
  - Keeps in-memory area intended for speeding up scans and joins
- SGA is shared by all background and server processes

**Caption:**
The actual implementation of Oracle instance depends on the system. On UNIX platforms multiple processes are started. On Ms Windows systems processes with multiple processing threads playing the role of UNIX processes are started.

## Slide 8: Background processes

- There are a number of background processes responsible for multiple tasks such as:
  - Writing transaction logs (LGWR process)
  - Saving changes to database (DBWn processes)
  - Archiving transaction logs to prevent tchem from being overwritten by newer changes (ARCn processes)
  - Registering an instance with a listener (LREG process)
- Background processes are automatically started when an instance is started
- Whether some processes are started, depends on DBMS configurations

## Slide 9: Oracle Net Services

Oracle Net Services

## Slide 10: Oracle Net Services

- Enable network connections from client processes to the Oracle server processes
- Oracle Net or a module simulating it (e.g. JDBC) is located on each client workstation or client server
- Oracle Net includes:
  - a background component on a client computer. It enables network connections with the instance, whereas hiding internal network protocols used for the communication between client application and server process
  - a listener process. It enables the communication between a client application and DBMS instance.
- The foundation of Oracle Net Services is TNS, which stands for Transparent Network Substrate
- Oracle Net Services with TNS allow connections to be independent of the operating system and communication protocols

## Slide 11: Network-based connections

- In Oracle 26ai, the following network protocols are supported by Oracle Net:
  - TCP/IP
  - TCP/IP with SSL
  - Named Pipes
  - SDP (Sockets Direct Protocol)
  - Exadirect (new protocol for low overhead database access)
  - Websocket protocol
- Connecting over the network requires TNS listener process to be running
- Oracle Net runs on top of supported network protocols, thus the client and server processes remain unaware of the actual transport layer
- TNS stands for Transparent Network Substrate
- In case of TCP/IP-based connections the Oracle client software connects to TNS listener typically using port 1521

## Slide 12: Oracle Net Listener

- The process residing on the server used to establish the network communication between clients and Oracle DBMS
- One listener can service multiple database instances identified by service names
- Listener is not a part of DBMS instance

## Slide 13: Oracle Net Listener (diagram)

**Diagram:**

Top: a wide box labeled "Oracle instance".

Below, left to right:
- Oval "Client process"
- A vertical bar labeled "LAN/WAN"
- Oval "Oracle Net Listener"
- Oval "Oracle Server process"

Arrows:
- From "Client process" across LAN/WAN to "Oracle Net Listener", labeled "1."
- A dash-dot arrow from "Oracle Net Listener" to "Oracle Server process", labeled "2."
- A double-headed vertical arrow between "Oracle instance" and "Oracle Server process", labeled "3."
- An arrow from "Oracle Server process" back to "Client process", labeled "3."

**Caption (numbered):**
1. Network request for a new connection is received from a client process by a listener, typically on TCP port 1521. CONNECT packet is sent.
2. The Listener starts a new server process to handle the connection
3. The server process is used to handle the connection and all submitted requests.
4. When the listener process is terminated, new remote connections can not be established. Still, any already established connections will be handled.

## Slide 14: Establishing a connection

| Method | Description |
|--------|-------------|
| Easy connect naming | Server name, TCP port and instance name need to provided. No need to configure client workstation. TCP/IP is the only supported protocol. Advanced options not available. Example: `sqlplus marketing/pass@127.0.0.1:1521/orcl` The complete syntax is: `username/password@host[:port][/service_name][:server_type][/instance_name]` |
| The use of Net service name | Easy connect is not always convenient and/or sufficient. In such cases, net service name can be used. Example: `sqlplus marketing/pass@mySalesServer` The complete syntax is: `user/password@ServiceName` |

**Note:** Sqlplus is Oracle utility used to execute SQL statements and manage Oracle instances including starting and stopping them

## Slide 15: Name resolution

- Name resolution is the process required to establish a connection with Oracle server process when using Net service names
- In general:
  - client application refers to net service name,
  - the name is resolved with the help of Oracle Net in order to identify:
    - DBMS server name/network address,
    - DBMS instance name,
    - Protocol-specific settings e.g. TCP/IP port,
    - Connection-related settings e.g. whether dedicated or shared server process is requested
- Thanks to the name resolution process, the client process knows how to connect to the listener process

## Slide 16: Name resolution in practice

**Diagram:**

Left side — "Client machine" box containing:
- Box "Client application"
- Box "Client Oracle Net Services components"

Middle — "LAN/WAN" band.

Right side — "DBMS Server" box containing (top to bottom):
- "Oracle listener process"
- "Oracle instance"
- "Database" (disk/cylinder shape)

Annotations (right margin callouts):
- "Client application can refer to a net service name (such as mySalesServer) rather than hard-coded listener address and connection-related settings to establish a connection with Oracle instance"
- "Client components of Oracle Net Services based on e.g. tnsnames.ora file determine the settings to be applied to connect to the listener process (such as IP address and port)"
- "The listener accepts new connection and starts a child process (if configured to do so) to make interaction with an instance possible"

## Slide 17: Naming methods

| Method | Description | Advanced options |
|--------|-------------|------------------|
| Local naming | tnsnames.ora specifies the mapping of service aliases to connect descriptors. The most frequently used naming method. | YES |
| Directory naming | LDAP-compliant directory services are used to resolve service aliases and obtain: server, protocol, port and instance name. No need to maintain local tnsnames.ora files on many workstations. | YES |
| External naming | Non-Oracle naming services are involved. These may include NIS (Network Information Service), DCE (Distributed Computing Environment) and CDS (Cell Directory Services) | YES |

**Note:** Naming methods are used in name resolution process to find what net service name such as mySalesServer means i.e. to find the network address of the server and other settings needed to establish the connection. For details on how naming methods are configured see the next slides.

## Slide 18: Oracle Net Configuration files

| File | Sample content | Description |
|------|----------------|-------------|
| sqlnet.ora | `NAME.DIRECTORY_PATH= (TNSNAMES, EZCONNECT)` | Overall NET configuration incl. the use of different naming methods to resolve network names. |
| tnsnames.ora | See below | Defines local names and their mapping to server name, protocol, port and service id i.e. to connect descriptor. The descriptor contains protocol-related attributes. These may differ depending on the protocol used to communicate with the server. |
| listener.ora | See below | Defines a list of all listener processes on the server and a list of instances handled by each listener. |

**Note:** All files reside in `<oracle_home>/network/admin/`

## Slide 19: Defining server-side settings: sample listener.ora file

```
SID_LIST_LISTENER =
(SID_LIST =
(SID_DESC =
(SID_NAME = PLSExtProc)
(ORACLE_HOME = d:\oracle10g4\product\10.2.0\db_1)
(PROGRAM = extproc)
)
)
LISTENER =
(DESCRIPTION_LIST =
(DESCRIPTION =
(ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1))
(ADDRESS = (PROTOCOL = TCP)(HOST = main.pw.edu.pl)(PORT = 1521))
)
)
```

1. The SID_LIST_LISTENER defines the database instance, the listener will be providing access to.
2. The second part defines the listener process, the name of the listener and the protocols that will be used by a listener to listen for connections made to it.

## Slide 20: listener.ora – two listeners defined

```
…
LISTENER =
(DESCRIPTION_LIST =
(DESCRIPTION =
(ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1))
)
(DESCRIPTION =
(ADDRESS = (PROTOCOL = TCP)(HOST = localhost)(PORT = 1521))
)
)
LISTENER_BETA =
(DESCRIPTION_LIST =
(DESCRIPTION =
(ADDRESS = (PROTOCOL = TCP)(HOST = myserver)(PORT = 1571))
)
(DESCRIPTION =
(ADDRESS = (PROTOCOL = TCP)(HOST = myserver)(PORT = 1583))
)
)
```

1. Two listeners named LISTENER and LISTENER_BETA have been defined
2. The second listener uses two different ports to accept new connections

## Slide 21: Listener – serviced databases

```
SID_LIST_LISTENER_BETA =
(SID_LIST =
(SID_DESC =
(ORACLE_HOME = D:\oracleMarketing\product\version\db_1)
(SID_NAME = ORCL)
)
(SID_DESC =
(ORACLE_HOME = D:\oracleSales\product\version\db_1)
(SID_NAME = ORCL2)
)
)
```

1. LISTENER_BETA is servicing two different instances, named ORCL and ORCL2.
2. Should any other SID be used in the connection request, an error will be returned by a listener. The listener will not know anything about the requested instance.
3. The instance must be up and running for the connection to succeed.
4. Modern Oracle instances automatically register (by using dynamic registration) with the default listener on database startup.

The example above uses static registration because non-default TCP port is used by a listener LISTENER_BETA.

## Slide 22: Client-side settings: tnsnames.ora

```
ALPHASRV =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = 172.16.173.21)(PORT = 1521))
    )
    (CONNECT_DATA =
      (SERVICE_NAME = orcl)
    )
  )
mySalesServer =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = main.pw.edu.pl)(PORT = 1561))
    )
    (CONNECT_DATA =
      (SERVICE_NAME = orcl2)
    )
  )
```

1. The file lists service names a.k.a. aliases. Each service name is mapped to connect descriptor. Service name does not need to match instance name.
2. Service names can be used in Oracle tools to avoid specifying all network and instance-related settings. Example: `sqlplus user/password@mySalesServer`

## Slide 23: Advanced connection options

| Option | Description |
|--------|-------------|
| Connect-time failover | The alias has more than one associated listener configured. If one listener fails, another one is attempted. |
| Load balancing | The alias has more than one associated listener configured. Each time new connection is established, the listener is selected in a random manner. |
| Timeout settings | Timeout options make it possible to configure how long to wait for a connection to be established and how many times to try to set up a connection |
| Transparent Application Failover | A client can be reconnected to another instance if the current DBMS instance fails. One option is to replay in-progress queries. Note that an active transaction is rolled back at the time of failure. |

**Note:** Further details can be found in https://docs.oracle.com/en/database/oracle/oracle-database/26/netag/enabling-advanced-features-oracle-net-services.html

## Slide 24: Client side settings — tnsnames.ora – connect-time failover

```
LOADTEST =
  (DESCRIPTION =
    (ADDRESS_LIST =
(load_balance=on)
(failover=on)
      (ADDRESS = (PROTOCOL = TCP)(HOST = servername_IP1)
(PORT = 1521))
      (ADDRESS = (PROTOCOL = TCP)(HOST = servername_IP2)
(PORT = 1571))
    )
    (CONNECT_DATA =
      (SERVICE_NAME = ORCL)
    )
  )
```

1. Two addresses have been identified on a list of a service alias. These correspond to two different network interfaces that are used by the listeners servicing this instance.
2. load_balance=on instructs the client process to randomly connect to one of the two supported addresses
3. failover=on adds fault tolerance – if the address randomly selected does not respond, the other one is attempted.
4. Sample usage: `sqlplus user/password@LOADTEST`

## Slide 25: A more complex setting

**Diagram:**

Left side — "Client machine" box containing:
- Box "Client application"
- Box "Client Oracle Net Services components"

Middle — "LAN/WAN" band.

Right side — "DBMS Server" box containing:
- Two listeners side by side: "Listener1" and "Listener2"
- Below them: "Oracle instance"
- Below that: "Database" (disk/cylinder shape)

Both listeners connect down to the single Oracle instance.

Annotations (right margin callouts):
- "Client components of Oracle Net Services based on e.g. tnsnames.ora determine the settings to be applied, which include load balancing and connection failover."
- "A connection to one of two listeners serving the database is attempted. This is transparent for the client application"
- "The listener that accepted the connection request enables the actual communication with the instance."
- "Note that each of the listeners could also handle more than one instance residing on the server"

## Slide 26: Summary

- Modern DBMS platform is a complex set of interrelated services
- Oracle Net Services show the complexity of DBMS architecture and network connectivity:
  - Different network protocols can be used to connect a client application to a DBMS instance
  - Multiple listener processes may be set up
  - Multiple DBMS instances can be served by one listener process
  - High-availability settings such as attempting connection through different network interfaces (cards), ports and listener processes are possible. This reduces the risk of communication failures

## Slide 27: Appendix I

Oracle tools related to the configuration of network settings

## Slide 28: lsnrctl utility

- Command line utility used to manage listener procesess. Frequently used commands:
  - `start [ListenerName]`
  - `stop [ListenerName]`
  - `status [ListenerName]`
  - `set CURRENT_LISTENER [ListenerName]`
  - `help`

1. The first way of using lsnrctl:
   ```
   lsnrctl
   lsnrctl> start ….
   ```
2. The second way:
   ```
   lsnrctl start ….
   ```
3. The first one is more suited for interactive mode, the second mode can be used for developing batches.

## Slide 29: tnsping utility

- Used to test the connectivity with the listener process
- Can accept both Easy Connect parameters and service name
- Examples:
  - `tnsping localhost:1571`
  - `tnsping mySalesServer`
  - `tnsping localhost:1571/orcl`
- Does not verify the availability of the requested service
- Does not verify whether the listener handles a requested service name

## Slide 30: Summary of tools used to perform Oracle network configuration

| Application | Role | Remarks |
|-------------|------|---------|
| Oracle Net Manager — netmgr | Allows to configure naming methods to be used, local naming methods and listeners, incl. advanced settings (the instances handled by a listener) unlike Oracle Net Configuration Assistant | Changes are saved to TNSNAMES.ORA, LISTENER.ORA and SQLNET.ORA |
| Oracle Net Configuration Assistant | Used by Oracle Universal Installer when installing Oracle software | Automatically creates default, basic configuration files. Its functionality partially overlaps with the functionality of Oracle Net Manager. |
| Enterprise Manager (web application) | Allows to start/stop/edit listener settings, local naming, directory naming. | The changes are saved to the configuration files listed above. |
| Oracle Internet Directory | Network services that can be used to store the data previously stored in tnsnames.ora | Allows to move the data to central directory, in a similar whay /etc/hosts data can be moved to DNS |
| Command line tools — tnsctrl and tnsping | Used to start/stop listener processes and test client-server connectivity. | |

## Slide 31: Project funding acknowledgement

MSc program in Data Science has been developed as a part of task 10 of the project „NERW PW. Science - Education - Development - Cooperation" co-funded by European Union from European Social Fund.
