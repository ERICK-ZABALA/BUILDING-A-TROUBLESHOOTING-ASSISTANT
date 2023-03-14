#!/home/devnet/Documents/BUILDING-A-TROUBLESHOOTING-ASSISTANT/assistant/bin/python
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
def run_command(command, interface):
    """
    Run a given command, gather both raw and Json output.
    Return as a tuple. (output_raw, output_json)
    """

    output_raw = command.format(interface_id = interface)
    output_json = command.format(interface_id=interface)

    return (output_raw, output_json)
#############################################################################



if __name__ == "__main__":
    print("Collecting show commands storing in bootflash.")

    # Collect interface ID as command line argument
    import argparse
    # Use argparse to determine the interface id
    parser = argparse.ArgumentParser(description="Run show command to assist with troubleshooting")
    parser.add_argument('--interface', required=True, type=str, help="Interface of interest. (example 1/1)")

    args = parser.parse_args()
    print("Interface Ethernet {interface_id} will be checked.".format(interface_id = args.interface))
    # Run commands and store output
    
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

    # Create new folder for output
    # Create a file for each command output


