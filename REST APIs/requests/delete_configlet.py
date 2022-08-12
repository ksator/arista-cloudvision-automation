'''
Delete configlet using REST API
'''

import json
import requests

requests.packages.urllib3.disable_warnings()

with open("token.tok") as f:
    token = f.read().strip('\n')

configlet_name = "cvprac_example"

URL = "https://192.168.0.5/cvpservice/configlet/getConfigletByName.do?name=" + configlet_name

headers = {
  'Accept': 'application/json',
  'Cookie': "access_token=" + token
}

response = requests.request("GET", URL, headers=headers,  verify=False)
print(response.json())
configletKey = response.json()['key']

URL = "https://192.168.0.5/cvpservice/configlet/deleteConfiglet.do"

payload = json.dumps([{
  "key": configletKey,
  "name": configlet_name
}])

headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Cookie': "access_token=" + token
}

response = requests.request("POST", URL, headers=headers, data=payload, verify=False)
print (response.json())
