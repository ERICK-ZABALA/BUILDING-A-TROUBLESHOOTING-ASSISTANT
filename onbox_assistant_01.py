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

    # Run commands and store output
    # Create new folder for output
    # Create a file for each command output

