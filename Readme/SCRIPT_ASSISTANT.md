# TEST

# ASSITANT ONBOX WITH PYTHON

The first step is running conectivity with your Nexus 9000 and environment development on linux developing this file in python.

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

Second step is create the vector arguments using `argparse` in your script an test, you can check the code `onbox_assistant_02.py`

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

Third steps is collect the data retrive via function `def run_command(command, interface)`

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

![image](https://user-images.githubusercontent.com/38144008/225753103-f9474e7b-b78f-4149-a3a2-d7fad14c8ef5.png)

