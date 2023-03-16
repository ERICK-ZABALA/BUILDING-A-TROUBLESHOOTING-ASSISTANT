#!/home/devnet/Documents/BUILDING-A-TROUBLESHOOTING-ASSISTANT/assistant/bin/python
import os
import paramiko
import scp
import json

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Conectarse al servidor remoto con nombre de usuario y contraseña
ssh.connect('10.10.20.177', username='admin', password='Cisco123')

# Ejecutar un comando en el servidor remoto para buscar los archivos
stdin, stdout, stderr = ssh.exec_command('dir bootflash: | json')

# Leer la salida del comando y dividirla en líneas
file = json.loads(stdout.read())
print()
print(file)
print()

fnames = []

for row in file["TABLE_dir"]["ROW_dir"]:
    fnames.append(dict(fname=row['fname']))

print(fnames)
"""
output: [{'fname': '.rpmstore/'}, {'fname': '.swtam/'}, {'fname': 'nxos.9.2.4.bin'}, {'fname': 'onbox_assistant.py'}, {'fname': 'platform-sdk.cmd'}, {'fname': 'scripts/'}, {'fname': 'set_boot.py'}, {'fname': 'ts_report_2023-03-15-03-17-39_interface1_11/'}, {'fname': 'virt_strg_pool_bf_vdc_1/'}, {'fname': 'virtual-instance/'}, {'fname': 'virtual-instance.conf'}, {'fname': '{folder_name}/'}]
"""

### Filter ts_report*

ts_report_file = list(filter(lambda x: 'ts_report' in x['fname'], fnames))

print()
print(ts_report_file)
print()

with scp.SCPClient(ssh.get_transport()) as scp_client:
    # Descargar cada archivo encontrado
    for item in ts_report_file:
        if "ts_report" in item["fname"]:
            print(item["fname"])
            fname = item["fname"]
            remote_path = fname
            local_path = os.path.join('/home/devnet/Documents/BUILDING-A-TROUBLESHOOTING-ASSISTANT/switch/', fname)
            scp_client.get(remote_path, local_path, recursive=True)

ssh.close()

# ARRAY OUT
#fnames = []
#for row in file["TABLE_dir"]["ROW_dir"]:
#    fnames.append(row["fname"])

#print(fnames)




