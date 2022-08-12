from cvprac.cvp_client import CvpClient
import requests.packages.urllib3
from pprint import pprint
import uuid
import time

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

# Create list of devices serial number
SN = []
for device in inventory: 
    SN.append(device['serialNumber'])

# print(SN)
# SN[3:5]

# Remove devices from CVP
# help(clnt.api.device_decommissioning)
device_id = SN[2]
request_id = str(uuid.uuid4())
clnt.api.device_decommissioning(device_id, request_id)
# help(clnt.api.device_decommissioning_status_get_one)
decomm_desired_status = "DECOMMISSIONING_STATUS_SUCCESS"
decomm_actual_status = ""
while decomm_actual_status != decomm_desired_status:
    decomm_actual_status = clnt.api.device_decommissioning_status_get_one(request_id)['value']['status']
    time.sleep(10)

print(decomm_actual_status)
