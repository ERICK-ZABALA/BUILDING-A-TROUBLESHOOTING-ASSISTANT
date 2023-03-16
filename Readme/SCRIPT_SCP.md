# Download Files via SCP

Finally, you can create a script to extract all the file to your system. As example you can use this one.

+ Requirements: install scp, paramiko

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


