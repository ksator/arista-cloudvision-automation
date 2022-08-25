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

# Configlets management

# Add a configlet 
configletName = "cvprac_example"
configletString = """
!
ip name-server vrf management 1.1.1.1
ip name-server vrf management 8.8.8.8
!
"""
# help(clnt.api.add_configlet)
clnt.api.add_configlet(configletName,configletString)

