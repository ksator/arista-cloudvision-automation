'''
This script generates a Token using Python requests.
You first need to install the requests Python module using this command: pip install requests
'''

import json
import requests

requests.packages.urllib3.disable_warnings()

# Generate and get a token using Python via the CVP REST API

# Replace the CVP IP Address
URL = "https://192.168.0.5/cvpservice/login/authenticate.do"

# Replace the username and password
payload = json.dumps({
  "userId": "arista",
  "password": "aristad97w"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}
response = requests.request("POST", URL, headers=headers, data=payload, verify=False)

# Save the generated token into the variable named token
token = response.json()['sessionId']

# Print your token
print(token)
