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

# Apply configlets to a container
container_name = "ContainerA"
configletName = 'cvprac_example'
# help(clnt.api.get_container_by_name)
container = clnt.api.get_container_by_name(container_name)
# help(clnt.api.get_configlet_by_name)
configlet = clnt.api.get_configlet_by_name(configletName)
# help(clnt.api.apply_configlets_to_container)
clnt.api.apply_configlets_to_container("", container, [configlet])


