
from cvprac.cvp_client import CvpClient
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()

# Generate a token from CVP and copy it locally so you can then use it from your code
with open("token.tok") as f:
    token = f.read().strip('\n')

# CvpClient is a class in the module cvprac.cvp_client
# clnt is an object, instance of the class CvpClient
clnt = CvpClient()

# help(clnt.connect)
cvp = '192.168.0.5'
clnt.connect(nodes=[cvp], username='',password='',api_token=token)

# Get a list of devices. Each device is a dict. 
# help(clnt.api.get_inventory)
inventory = clnt.api.get_inventory()

# Get device running configuration
# help(clnt.api.get_device_configuration)
# inventory[1]['hostname']
# conf = clnt.api.get_device_configuration(inventory[1]['systemMacAddress'])
# print(conf)

# Write the running configuration of each device using the fqdn as the filename

# Create a list of MAC addresses
device_macs = []
for dev in inventory:
    device_macs.append(dev['systemMacAddress'])

# Create a dictionary with MAC to running-config mapping
# help(clnt.api.get_device_configuration)
running_configs = {}
for mac in device_macs:
    running_configs[mac] = clnt.api.get_device_configuration(mac)

# Write the running configuration of each device using the fqdn as the filename
for dev in inventory:
    with open(dev['fqdn']+'.cfg', 'w') as f:
        f.write(running_configs[dev['systemMacAddress']])

