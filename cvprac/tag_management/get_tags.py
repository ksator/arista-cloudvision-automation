import requests.packages.urllib3
from cvprac.cvp_client import CvpClient

requests.packages.urllib3.disable_warnings()

clnt = CvpClient()

with open("token.tok") as f:
    token = f.read().strip('\n')

CVP = '192.168.0.5'
clnt.connect(nodes=[CVP], username='',password='',api_token=token)

element_type = "ELEMENT_TYPE_DEVICE"

# Get tags
tags = clnt.api.get_all_tags()
for item in clnt.api.get_all_tags(element_type=element_type)['data']:
    print(item['result']['value']['key']['label']+":"+item['result']['value']['key']['value'])
