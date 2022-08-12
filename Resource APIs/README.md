**Table of Contents**

- [About Resource APIs](#about-resource-apis)
- [Requirement](#requirement)
- [Resource APIs Examples](#resource-apis-examples)
  
# About Resource APIs

Resource APIs can be used to:

- Collect information about CVP inventory, tags, events ...
- Configure tags, decommission devices ...

From CVP 2022.1.0, a resource API explorer is available in the CVP GUI.

Resources are modeled with `.proto` files:

- These files can be found in the repository https://github.com/aristanetworks/cloudvision-apis
- Documentation for these APIs is published on this web page https://aristanetworks.github.io/cloudvision-apis/

Resources APIs are accessed with gRPC. CVP is the gRPC server. We can use gRPC clients (gPRCurl, grpc_cli, Postman, ...) to call the RPC methods on CVP.  

REST APIs mappings are generated so we can also use a REST clients (cURL, Python request module, ...) for resource APIs.


# Requirement

Token based authentication is required. To enable token based authentication, refer to [this directory](../Token%20based%20authentication)

# Resource APIs Examples

You will find here Resources APIs examples using:

- The **gRPCurl** command-line tool
- The **cURL** command-line tool
- The **cvprac** Python library
- The **requests** Python library
