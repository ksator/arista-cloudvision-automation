import json
import requests

requests.packages.urllib3.disable_warnings()

# Generate a token
URL = "https://192.168.0.5/cvpservice/login/authenticate.do"

payload = json.dumps({
  "userId": "arista",
  "password": "aristad97w"
})

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request("POST", URL, headers=headers, data=payload, verify=False)

token = response.json()['sessionId']

# Get the inventory using the generated token
URL = "https://192.168.0.5/cvpservice/inventory/devices?provisioned=true"

payload={}

headers = {
  'Accept': 'application/json',
  'Cookie': "access_token=" + token
}

response = requests.request("GET", URL, headers=headers, data=payload, verify=False)

# Print the CVP inventory
print(response.text)
