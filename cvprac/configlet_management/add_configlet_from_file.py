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

# create configlet from file
# create a file named configlet_ns.cfg with some EOS configuration 
configletName = "cvprac_example2"
with open("configlet_ns.cfg") as file:
     configletString = file.read()

clnt.api.add_configlet(configletName, configletString)
