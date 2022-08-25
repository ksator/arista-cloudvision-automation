from cvprac.cvp_client import CvpClient
import requests.packages.urllib3
from pprint import pprint

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

# help(clnt.api.get_device_by_name)
device = clnt.api.get_device_by_name(device_name)

# Get configlets for a device
# help(clnt.api.get_configlets_by_device_id)
device['systemMacAddress']
clnt.api.get_configlets_by_device_id(device['systemMacAddress'])
for configlet in clnt.api.get_configlets_by_device_id(device['systemMacAddress']): 
    print(configlet['name'])

