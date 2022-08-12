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

# dir(clnt)
clnt.nodes
clnt.node_cnt
clnt.api_token 
clnt.is_cvaas
clnt.last_used_node
clnt.headers

# print CVP version
clnt.version
result = clnt.api.get_cvp_info()
print(result)
clnt.version
