# ASSITANT ONBOX WITH PYTHON

+ The first step is running conectivity with your Nexus 9000 and environment development on linux developing this file in python.

```python
"""
This is a script that will run "onbox" on a Nexus Switch with the goal
of running a series of show commands and collecting
the output into files stored into date/time folders. One file per command.
Command to run:
    show interface ethernet N/N
    show logging last 50
    show ip arp vrf all
    show mac address-table
    ahow ip route vrf all
    show system internal interface ethernet N/N ethernet
N/N event-history
Command Line Argument: Interface ID
"""

if __name__ == "__main__":
    print("Collecting show commands storing in bootflash.")

    # Run commands and store output
    # Create new folder for output
    # Create a file for each command output
```

+ Second step is create the vector arguments using `argparse` in your script an test, you can check the code `onbox_assistant_02.py`

Output: 

```python

(assistant)  devnet@Devnet  ~/Documents/BUILDING-A-TROUBLESHOOTING-ASSISTANT   main  python onbox_assistant_02.py --h      
Collecting show commands storing in bootflash.
usage: onbox_assistant_02.py [-h] --interface INTERFACE

Run show command to assist with troubleshooting

optional arguments:
  -h, --help            show this help message and exit
  --interface INTERFACE
                        Interface of interest. (example 1/1)
(assistant)  devnet@Devnet  ~/Documents/BUILDING-A-TROUBLESHOOTING-ASSISTANT   main  python onbox_assistant_02.py --interface 1/11

Collecting show commands storing in bootflash.
Interface Ethernet 1/11 will be checked.

```

+ Third steps is collect the data retrive via function `def run_command(command, interface)`

```python
def run_command(command, interface):
    """
    Run a given command, gather both raw and Json output.
    Return as a tuple. (output_raw, output_json)
    """

    output_raw = command.format(interface_id = interface)
    output_json = command.format(interface_id=interface)

    return (output_raw, output_json)

 # Dict of command to run. 
    
    commands = {
        "show_interface":"show interface ethernet {interface_id}"
    }
    # Output Dict
    output = {}
    # Loop over commands to run function and save output
    for label, command in commands.items():
        output[label] = run_command(command, args.interface)
    
    print(output)

```

Output:

```bash
(assistant)  devnet@Devnet  ~/Documents/BUILDING-A-TROUBLESHOOTING-ASSISTANT   main  python onbox_assistant_03.py --interface 1/11
Collecting show commands storing in bootflash.
Interface Ethernet 1/11 will be checked.
{'show_interface': ('show interface ethernet 1/11', 'show interface ethernet 1/11')}

```
# Debuging in Python with Args

![image](https://user-images.githubusercontent.com/38144008/225752592-a51b518f-f0d6-4b44-8aee-515acbc97383.png)

![image](https://user-images.githubusercontent.com/38144008/225752634-8164353a-0a40-4a48-a741-4d602e959aa3.png)

![image](https://user-images.githubusercontent.com/38144008/225752796-ac2623bd-451b-4aaf-b302-c5711f57c04d.png)

![image](https://user-images.githubusercontent.com/38144008/225753009-da9f7aea-500e-404d-8725-6407cd5daa4b.png)

![image](https://user-images.githubusercontent.com/38144008/225753454-44599782-fb60-4936-896c-fada6a495c8b.png)

+Fourth step insert the library cli that only work in the Switches Nexus. 

```python

def run_command(command, interface):
    """
    Run a given command, gather both raw and Json output.
    Return as a tuple. (output_raw, output_json)
    """

    output_raw = `cli`(command.format(interface_id = interface))
    output_json = `clid`(command.format(interface_id=interface))

    return (output_raw, output_json)

```
![image](https://user-images.githubusercontent.com/38144008/225761002-3fcfae29-aed9-4a23-87a1-6e547e8c35b0.png)

![image](https://user-images.githubusercontent.com/38144008/225761097-c9b29640-07aa-43b2-8689-d865123edfcc.png)

![image](https://user-images.githubusercontent.com/38144008/225761127-fe29d3e8-fa24-4844-bf4e-8a8ee81d62a6.png)

![image](https://user-images.githubusercontent.com/38144008/225761214-ee7ef8c4-0c70-4468-a9b4-86545e066b6a.png)

then you can inser all the commands that you are going to use to evaluate your system and finally export in the bootflash all the data creating a folder.

```python
 # Create new folder for output
   print("Output will be stored in folder bootflash:{folder_name}/".format(folder_name=folder_names))
    folder = '/bootflash/{folder_name}'.format(folder_name=folder_names)
    #print(folder)
    mkdir(folder)


    # Create a file for each command output
    for command, results in output.items():
        # unpack the results
        raw_output, json_output = results

        # write raw data file
        if raw_output:
            print("Writing file {folder_name}/{command}.txt".format(folder_name=folder, command = command))
            with open ("{folder_name}/{command}.txt".format(folder_name=folder, command=command), "w") as f_raw:
                f_raw.write(raw_output)

        # if json_output available, write json file
        if json_output:
            print("Writing file {folder_name}/{command}.json".format(folder_name = folder, command = command))
            with open ("{folder_name}/{command}.json".format(folder_name=folder, command=command), "w") as f_json:
                f_json.write(json_output)
                
```
# Activate Syslog with EEM

Configure this Events and actions in your Nexus 9000

```bash

Monitor for DOWN
dist-sw01(config)#
dist-sw01(config)# event manager applet TS_Assitant_Eth1_11_DOWN
dist-sw01(config-applet)# event syslog pattern "Interface Ethernet1/11 is down"
Configuration accepted successfully
dist-sw01(config-applet)# action 1 syslog priority notifications msg SAW INTERFACE E1/11 GO DOWN
dist-sw01(config-applet)# action 2 cli python bootflash:onbox_assistant.py --interface 1/11
dist-sw01(config-applet)# exit

Monitor for UP
dist-sw01(config)# event manager applet TS_Assistant_Eth1_11_UP
dist-sw01(config-applet)# event syslog pattern "Interface Ethernet1/11 is up"
Configuration accepted successfully
dist-sw01(config-applet)# action 1 syslog priority notifications msg SAW INTERFACE E1/11 GO UP
dist-sw01(config-applet)# action 2 cli python bootflash:onbox_assistant.py --interface 1/11
dist-sw01(config-applet)# exit
```
# Manual Download of Files via SCP

running this command you are going to download all the report.

`devnet@Devnet  ~/Documents/BUILDING-A-TROUBLESHOOTING$ scp -r "admin@10.10.20.177:ts_report*" ./`

![image](https://user-images.githubusercontent.com/38144008/225761865-a901caba-9e99-4294-83a0-018427fbfee4.png)


# Download Files via SCP

Finally, you can create a script to extract all the file to your system. As example you can you this one.


```python
"""
This script permit dowload the files from your Nexus9000 via scp use the library paramiko and scp
Really useful when you whant to integrate to your Jenkis in the future.

"Switch Nexus 9000: 10.10.20.177
 username='admin'
 password='Cisco123'"

"""
import os
import paramiko
import scp
import json

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Conect to the switch using credentials and ip
ssh.connect('10.10.20.177', username='admin', password='Cisco123')

# Apply this command and display format json
stdin, stdout, stderr = ssh.exec_command('dir bootflash: | json')

# Read the variable stdout and load to format json.
file = json.loads(stdout.read())
print()
print(file)
print()

fnames = []

for row in file["TABLE_dir"]["ROW_dir"]:
    fnames.append(dict(fname=row['fname']))

print(fnames)

"""
output fnames: [{'fname': '.rpmstore/'}, {'fname': '.swtam/'}, {'fname': 'nxos.9.2.4.bin'}, {'fname': 'onbox_assistant.py'}, {'fname': 'platform-sdk.cmd'}, {'fname': 'scripts/'}, {'fname': 'set_boot.py'}, {'fname': 'ts_report_2023-03-15-03-17-39_interface1_11/'}, {'fname': 'virt_strg_pool_bf_vdc_1/'}, {'fname': 'virtual-instance/'}, {'fname': 'virtual-instance.conf'}, {'fname': '{folder_name}/'}]
"""

### Filter files that begin with: ts_report*

ts_report_file = list(filter(lambda x: 'ts_report' in x['fname'], fnames))

print()
print(ts_report_file)
print()

with scp.SCPClient(ssh.get_transport()) as scp_client:
    # Dowload each file founded
    for item in ts_report_file:
        if "ts_report" in item["fname"]:
            print(item["fname"])
            fname = item["fname"]
            remote_path = fname
            local_path = os.path.join('/home/devnet/Documents/BUILDING-A-TROUBLESHOOTING-ASSISTANT/', fname)
            scp_client.get(remote_path, local_path, recursive=True)

ssh.close()

```

# Result:

You can see the status of this interface Eth1/11 that change to status Down and also the time 03:17:31 and you logs was stored at time 03-17-39:    `delay ~8seg`

![image](https://user-images.githubusercontent.com/38144008/225758317-6ffd20aa-339b-4be7-8a87-b09692e31438.png)

![image](https://user-images.githubusercontent.com/38144008/225758975-97bd7117-bbea-47ea-b771-d210fd9a377f.png)

# REFERENCES
+ [Switches Nexus Supported](https://developer.cisco.com/site/python/) python onbox.
+ [Devnet Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/43964e62-a13c-4929-bde7-a2f68ad6b27c?diagramType=Topology) to test your Nexus9000.
+ [JSON](https://jsonlint.com/) to test format.

