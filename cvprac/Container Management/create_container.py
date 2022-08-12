from cvprac.cvp_client import CvpClient
import requests.packages.urllib3

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

# Create a container 
# Get container information
# help(clnt.api.get_container_by_name)
parent = clnt.api.get_container_by_name("Leaf")
parent["name"]
parent["key"]
# Create container ContainerA under container Leaf
help(clnt.api.add_container)
clnt.api.add_container("ContainerA",parent["name"],parent["key"])
