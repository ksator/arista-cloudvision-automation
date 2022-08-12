'''
This script creates and assigns topology tags to devices in order to create the topology in the CVP GUI
'''

import requests.packages.urllib3
import uuid
import time
from cvprac.cvp_client import CvpClient

requests.packages.urllib3.disable_warnings()

clnt = CvpClient()

with open('token.tok') as f:
    token = f.read().strip('\n')

CVP = '192.168.0.5'
clnt.connect(nodes=[CVP], username='',password='',api_token=token)

def get_dev_sn(clnt, device): 
    inventory = clnt.api.get_inventory()
    for item in inventory: 
        if item['hostname'] == device: 
            device_id = item['serialNumber']
    return(device_id)

print('Create workspace')
ws_name = 'global_tag_test'
ws_description = 'ws_description'
ws_id = str(uuid.uuid4())
clnt.api.workspace_config(workspace_id=ws_id, display_name=ws_name, description=ws_description)

print('Create topology hint tags')
element_type = 'ELEMENT_TYPE_DEVICE'
tags = {'topology_hint_datacenter':['NYC'],'topology_hint_pod':['pod_1','pod_2', 'pod_spine'], 'topology_hint_rack':['rack_1','rack_2', 'rack_3', 'rack_4', 'rack_5']}
for tag in tags:
    for value in tags[tag]:
        clnt.api.tag_config(element_type, ws_id, tag, value)

interface_id = ''

print('Assign topology hint datacenter tag to all devices')
devices = ['leaf1', 'leaf2', 'leaf3', 'leaf4', 'host1', 'host2','spine1', 'spine2', 'cvx01']
for dev in devices: 
    device_id = get_dev_sn(clnt, dev)
    clnt.api.tag_assignment_config(element_type, ws_id, 'topology_hint_datacenter', 'NYC', device_id, interface_id) 

print('Assign topology hint pod tags to some devices')
devices = ['leaf1', 'leaf2', 'host1']
for dev in devices: 
    device_id = get_dev_sn(clnt, dev)
    clnt.api.tag_assignment_config(element_type, ws_id, 'topology_hint_pod', 'pod_1', device_id, interface_id) 

devices = ['leaf3', 'leaf4', 'host2']
for dev in devices: 
    device_id = get_dev_sn(clnt, dev)
    clnt.api.tag_assignment_config(element_type, ws_id, 'topology_hint_pod', 'pod_2', device_id, interface_id) 

devices = ['spine1', 'spine2']
for dev in devices: 
    device_id = get_dev_sn(clnt, dev)
    clnt.api.tag_assignment_config(element_type, ws_id, 'topology_hint_pod', 'pod_spine', device_id, interface_id) 

print('Assign topology hint rack tag to each device')
devices = ['leaf1', 'host1']
for dev in devices: 
    device_id = get_dev_sn(clnt, dev)
    clnt.api.tag_assignment_config(element_type, ws_id, 'topology_hint_rack', 'rack_1', device_id, interface_id) 

devices = ['leaf2']
for dev in devices: 
    device_id = get_dev_sn(clnt, dev)
    clnt.api.tag_assignment_config(element_type, ws_id, 'topology_hint_rack', 'rack_2', device_id, interface_id) 

devices = ['leaf3', 'host2']
for dev in devices: 
    device_id = get_dev_sn(clnt, dev)
    clnt.api.tag_assignment_config(element_type, ws_id, 'topology_hint_rack', 'rack_3', device_id, interface_id) 

devices = ['leaf4']
for dev in devices: 
    device_id = get_dev_sn(clnt, dev)
    clnt.api.tag_assignment_config(element_type, ws_id, 'topology_hint_rack', 'rack_4', device_id, interface_id) 

devices = ['spine1', 'spine2']
for dev in devices: 
    device_id = get_dev_sn(clnt, dev)
    clnt.api.tag_assignment_config(element_type, ws_id, 'topology_hint_rack', 'rack_5', device_id, interface_id) 

print('Assign topology hint type tags to the hosts')
devices = ['host1', 'host2']
for dev in devices: 
    device_id = get_dev_sn(clnt, dev)
    clnt.api.tag_assignment_config(element_type, ws_id, 'topology_hint_type', 'endpoint', device_id, interface_id) 

print('Build WS')
request = 'REQUEST_START_BUILD'
request_id = 'b1'
clnt.api.workspace_config(workspace_id=ws_id,display_name=ws_name,description=ws_description,request=request,request_id=request_id)

print('Check WS build status')
time.sleep(1)
status = ''

while status not in ['BUILD_STATE_FAIL','BUILD_STATE_SUCCESS']: 
    request = clnt.api.workspace_build_status(ws_id,request_id)
    status = request['value']['state']
    print(f'WS status= {status}')
    time.sleep(5)

if status ==  'BUILD_STATE_FAIL': 
    print(f'WS status= {status}')
elif status == 'BUILD_STATE_SUCCESS':
    print(f'WS status= {status}')

print('Submit workspace')
if status == 'BUILD_STATE_SUCCESS':
    request = 'REQUEST_SUBMIT'
    request_id = 's1'
    clnt.api.workspace_config(workspace_id=ws_id, display_name=ws_name, description=ws_description,request=request,request_id=request_id)
    print('Workspace Sumitted')
