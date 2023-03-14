from cli import cli, clip
import json
bootimage = json.loads(cli("show version | json"))["kick_file_name"]
set_boot = cli("conf t ; boot nxos {}".format(bootimage))
save_config = cli("copy running-config startup-config")
