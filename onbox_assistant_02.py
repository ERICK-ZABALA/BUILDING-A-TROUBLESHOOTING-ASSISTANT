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
    # Create new folder for output
    # Create a file for each command output

