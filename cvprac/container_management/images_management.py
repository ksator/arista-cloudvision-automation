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

# Add image to a container
image_name = "EOS-4.25.4M"
image = clnt.api.get_image_bundle_by_name(image_name)
container_name = "Spine"
container = clnt.api.get_container_by_name(container_name)
# Add image to a container
# help(clnt.api.apply_image_to_container)
clnt.api.apply_image_to_container(image, container)

# Remove image to a container
image_name = "EOS-4.25.4M"
image = clnt.api.get_image_bundle_by_name(image_name)
container_name = "Spine"
container = clnt.api.get_container_by_name(container_name)
# help(clnt.api.remove_image_from_container)
clnt.api.remove_image_from_container(image, container)
