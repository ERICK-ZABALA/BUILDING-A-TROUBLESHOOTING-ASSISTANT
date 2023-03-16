
![image](https://user-images.githubusercontent.com/38144008/225514767-010fa633-9c2e-410a-9734-4fce1372d125.png)

# BUILDING-A-TROUBLESHOOTING-ASSISTANT

Network Automation is becoming increasingly important for managing and maintaining large-scale networks efficiently. If you're working with Cisco Switch Nexus 9000 NX-OS, you might be familiar with the Embedded Event Manager (EEM) and the importance of capturing logs when specific events occur on your interfaces.

In this project, we'll be exploring the powerful CLI library in Cisco Switch Nexus 9000 NX-OS and leveraging it to build a troubleshooting assistant that can automate the process of capturing logs and storing them in the bootflash. By the end of this project, you'll have a better understanding of how to use EEM, CLI libraries, and automation to streamline your network operations and troubleshoot issues faster. 

+ Click to Machine Logo to check the video!!! 

+ How can we know the status changed?
  Syslog
+ Where run the command?
  Onbox Nexus 9000
+ How to send the command to nexus 9000?
  Using Cli library of Python
+ Where we are going to save the information?
  Bootflash
+ How to xtract the information allocated in the Nexus
  Using SCP


* Library to interact: Cli, scp

|Topics|Description|Title|Notes|
|---|---|---|---|
| INSTALL PYTHON AND DEPENDENCIES | Install Python 3.10.2.  | [INSTALL PYTHON AND DEPENDENCIES](https://github.com/ERICK-ZABALA/AUTOMATING-A-NETWORK-INVENTORY-WITH-PYTHON/blob/main/INSTALL%20PYTHON%20AND%20DEPENDENCIES.md) | In this first step you install your Python. |
| INSTALL ANYCONNECT VPN CLIENT | Install VPN Client via CLI  | [INSTALL ANYCONNECT VPN CLIENT](https://github.com/ERICK-ZABALA/AUTOMATING-A-NETWORK-INVENTORY-WITH-PYTHON/blob/main/INSTALL%20ANYCONNECT%20VPN%20CLIENT.md) | In this second step you install your vpn anyconnect client. |
| INSTALL GIT | Install GIT via CLI | [INSTALL GIT](https://github.com/ERICK-ZABALA/AUTOMATING-A-NETWORK-INVENTORY-WITH-PYTHON/blob/main/INSTALL%20GIT.md) | In this step you install git in your environment. |
| CREATE SPREADSHEET | Create Spreadsheet  | [CREATE SPREADSHEET](https://github.com/ERICK-ZABALA/AUTOMATING-A-NETWORK-INVENTORY-WITH-PYTHON/blob/main/CREATE%20SPREADSHEET.md) | In this step you create an Spreadsheet. |
| CREATING A CSV FILE | Provide a CSV File as a report in Python  | [CREATING A CSV FILE](https://github.com/ERICK-ZABALA/AUTOMATING-A-NETWORK-INVENTORY-WITH-PYTHON/blob/main/CREATING%20A%20CSV%20FILE.md) | In this step you are going to provide a report via Python. |

# REFERENCES

* Download in your machine [Summer 2021 Devasc-Prep-Network-Inventory-01](https://github.com/hpreston/summer2021-devasc-prep-network-inventory-01.git) maked by Hank Preston, that is a guide if you need help to develop all the code related how to make an inventory.
+ Creation from [Excel File](https://pubhub.devnetcloud.com/media/pyats-getting-started/docs/quickstart/manageconnections.html#creation-from-excel-file)
+ [Devnet Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/43964e62-a13c-4929-bde7-a2f68ad6b27c?diagramType=Topology) to test owner Inventory
+ [JSON](https://jsonlint.com/) to test format
