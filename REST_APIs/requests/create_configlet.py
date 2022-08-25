import requests
import json

requests.packages.urllib3.disable_warnings()

with open("token.tok") as f:
    token = f.read().strip('\n')

url = "https://192.168.0.5/cvpservice/configlet/addConfiglet.do"

configletName = "cvprac_example"

configletString = """
!
ip name-server vrf management 1.1.1.1
ip name-server vrf management 8.8.8.8
!
"""

payload=json.dumps({
  "config": configletString,
  "name": configletName
})

headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Cookie': "access_token=" + token
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

response.ok
response.status_code
response.json()
