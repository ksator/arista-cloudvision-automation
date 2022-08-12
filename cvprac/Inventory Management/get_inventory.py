import requests.packages.urllib3
from pprint import pprint
from cvprac.cvp_client import CvpClient

# To avoid certificate warning messages
requests.packages.urllib3.disable_warnings()

# Read the CVP token saved in the file named token.tok and copy it to a variable named token so you can then use it in your code
with open("token.tok") as f:
    token = f.read().strip('\n')

# CvpClient is a class in the module cvprac.cvp_client
# clnt is an object, instance of the class CvpClient
clnt = CvpClient()

# help(clnt.connect)
cvp = '192.168.0.5'
clnt.connect(nodes=[cvp], username='',password='',api_token=token)

# Get a list of devices. Each device is a dictionnary. 
# help(clnt.api.get_inventory)
inventory = clnt.api.get_inventory()
# Examples of interesting commands
# type(inventory)
# len(inventory)
# inventory 
# pprint(inventory[0])
# inventory[0]['hostname']
# inventory[0]['systemMacAddress']
# inventory[0]['serialNumber']

# Print devices hostname
for dev in inventory:
    print(dev['hostname'])

