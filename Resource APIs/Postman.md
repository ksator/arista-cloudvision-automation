**Table of Contents**

- [Postman and gRPC](#postman-and-grpc)
- [Requirement](#requirement)
- [Install Postman Desktop Agent on your automation setup](#install-postman-desktop-agent-on-your-automation-setup)
- [Create a new workspace or select an existing one](#create-a-new-workspace-or-select-an-existing-one)
- [Create a new environment](#create-a-new-environment)
- [Activate the new environment](#activate-the-new-environment)
- [Create a new request using server reflexion](#create-a-new-request-using-server-reflexion)
- [Create a new request using a .proto file](#create-a-new-request-using-a-proto-file)

# Postman and gRPC

We can use Postman to interact with CVP using gRPC (gNMI, resource APIs).  
The gRPC port is 443 and gPRC uses HTTP2.  

# Requirement

Token based authentication is required. To enable token based authentication, refer to [this directory](../Token%20based%20authentication)

# Install Postman Desktop Agent on your automation setup

Importing a proto file and invoking gRPC services is a new Postman feature.  
To connect with a gRPC server (CVP) requires using Postman Desktop Agent (this is not supported with Postman web).  
In this example we are using Postman Desktop Agent Version 9.26.8.

# Create a new workspace or select an existing one

# Create a new environment

From your workspace, you will need to create and activate a new environment  

Click on **Environment** and create a new environment.  
Provide a name to the new environment.
Define these two variables:

- grpcServerUrl: use the CloudVision IP address
- token: use the token generated previously

![create new environment](../Images/postman-gnmi-new-env.png)

# Activate the new environment

Activate the environment.  
![activate environment](../Images/postman-gnmi-activate-env.png)

# Create a new request using server reflexion

From your workspace, select **New > gRPC Request**
![create new request](../Images/postman-gnmi-new-collection.png)

Use the variable `grpcServerUrl` for the server URL  
Select the authorization type `Bearer token`  and use the variable `token` for the token  
![rapi](../Images/rapi.png)

Enable TLS
![rapi](../Images/rapi-tls.png)

Server reflection is enabled on CVP so you do not have to use the .proto source file.  
Select `Using server reflection` in service definition.  
![rapi](../Images/rapi-server-reflexion1.png)

Once the services are discovered, select as example `arista.inventory.v1.DeviceService.GetAll`.  
The `GetAll` RPC from the `DeviceService` service is defined in the file `arista/inventory.v1/services.gen.proto`  
![rapi](../Images/rapi-server-reflexion2.png)
![rapi](../Images/rapi-list.png)
![rapi](../Images/rapi-select.png)

Click on Invoke.  
You should get a response.  
![rapi](../Images/rapi-invoke.png)

Save the new request (name it `server-reflection`) to a new collection (name it `rAPI`)

# Create a new request using a .proto file