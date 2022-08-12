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

# Apply configlets
configletName = 'cvprac_example'
device_name = "leaf1.atd.lab"
# help(clnt.api.get_device_by_name)
device = clnt.api.get_device_by_name(device_name)
device
pprint(device)
# help(clnt.api.get_configlet_by_name)
configlet = clnt.api.get_configlet_by_name(configletName)
pprint(configlet)
configlet['name']
configlet['config']
# help(api.apply_configlets_to_device)
clnt.api.apply_configlets_to_device("", device, [configlet])
