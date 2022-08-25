import requests.packages.urllib3
import uuid
import time
from cvprac.cvp_client import CvpClient

requests.packages.urllib3.disable_warnings()

clnt = CvpClient()

with open("token.tok") as f:
    token = f.read().strip('\n')

CVP = '192.168.0.5'
clnt.connect(nodes=[CVP], username='',password='',api_token=token)

def get_dev_sn(clnt, device): 
    inventory = clnt.api.get_inventory()
    for item in inventory: 
        if item['hostname'] == device: 
            device_id = item['serialNumber']
    return(device_id)

# Create workspace
ws_name = 'ws_name'
ws_description = "ws_description"
ws_id = str(uuid.uuid4())
clnt.api.workspace_config(workspace_id=ws_id, display_name=ws_name, description=ws_description)

# Delete Tag (works as well even if tag is assigned to a device)
interface_id = ''
element_type = 'ELEMENT_TYPE_DEVICE'
tag_label = 'status'
tag_value = 'unused'
clnt.api.tag_config(element_type, ws_id, tag_label, tag_value, remove=True) 

# Build WS
request = 'REQUEST_START_BUILD'
request_id = 'b1'
clnt.api.workspace_config(workspace_id=ws_id,display_name=ws_name,description=ws_description,request=request,request_id=request_id)

# Check WS build status 
time.sleep(1)
status = ""

while status not in ["BUILD_STATE_FAIL",'BUILD_STATE_SUCCESS']: 
    request = clnt.api.workspace_build_status(ws_id,request_id)
    status = request['value']['state']
    print(f"WS status= {status}")
    time.sleep(5)


if status ==  "BUILD_STATE_FAIL": 
    print(f"WS status= {status}")
elif status == 'BUILD_STATE_SUCCESS':
    print(f"WS status= {status}")

# Submit workspace
if status == 'BUILD_STATE_SUCCESS':
    request = 'REQUEST_SUBMIT'
    request_id = 's1'
    clnt.api.workspace_config(workspace_id=ws_id, display_name=ws_name, description=ws_description,request=request,request_id=request_id)
