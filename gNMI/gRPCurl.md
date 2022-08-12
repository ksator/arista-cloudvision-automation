**Table of contents**
- [About gRPCurl](#about-grpcurl)
- [Install GO on your automation setup](#install-go-on-your-automation-setup)
- [Install gRPCurl on your automation setup](#install-grpcurl-on-your-automation-setup)
- [Clone the repo on your automation setup](#clone-the-repo-on-your-automation-setup)
- [Server reflection](#server-reflection)
- [List from a proto file on your automation setup](#list-from-a-proto-file-on-your-automation-setup)
  - [List services](#list-services)
  - [List methods from a service](#list-methods-from-a-service)
- [Describe from a proto file on your automation setup](#describe-from-a-proto-file-on-your-automation-setup)
  - [Describe all services](#describe-all-services)
  - [Describe a service](#describe-a-service)
  - [Describe methods from a service](#describe-methods-from-a-service)
  - [Describe messages used by methods](#describe-messages-used-by-methods)
  - [When describing messages, show a template of input data](#when-describing-messages-show-a-template-of-input-data)
- [Execute the method capabilities of the service gnmi.gNMI](#execute-the-method-capabilities-of-the-service-gnmignmi)

# About gRPCurl

gRPCurl is a command-line tool that lets you interact with gRPC servers. It's basically curl for gRPC servers.  

You can invoke RPC methods on a gRPC server from the command-line.  

You can also inspect gRPC services, either by querying a server that supports server reflection, or by reading proto source files.  
So, if the server you interact with does not support reflection, you can use the proto source files that define the service.  

gRPCurl source code: https://github.com/fullstorydev/grpcurl

# Install GO on your automation setup

GO is required to install gRPCurl.  
Please follow these [instructions to install GO](../../GO.md) to install GO on your automation setup

# Install gRPCurl on your automation setup

```bash
go install github.com/fullstorydev/grpcurl/cmd/grpcurl@latest
```

```bash
ls $GOPATH/pkg/mod/github.com/fullstorydev/
ls $GOPATH/bin/
grpcurl  --help
```

# Clone the repo on your automation setup

The gNMI proto file is https://github.com/openconfig/gnmi/blob/master/proto/gnmi/gnmi.proto

```bash
mkdir -p $GOPATH/src/github.com/openconfig
git clone https://github.com/openconfig/gnmi.git $GOPATH/src/github.com/openconfig/gnmi
ls $GOPATH/src/github.com/openconfig
```

# Server reflection

Server reflection is not enabled on CVP for the gNMI service. You can still use gRPCurl to inspect the gNMI service, but you need to use the proto source file to inspect the gNMI service (i.e you can not inspect this service through server reflection).  

# List from a proto file on your automation setup

## List services

```bash
grpcurl --plaintext --import-path ${GOPATH}/src --proto github.com/openconfig/gnmi/proto/gnmi/gnmi.proto list
```

## List methods from a service

```bash
grpcurl --plaintext --import-path ${GOPATH}/src --proto github.com/openconfig/gnmi/proto/gnmi/gnmi.proto list gnmi.gNMI
```

# Describe from a proto file on your automation setup

## Describe all services

```bash
grpcurl --plaintext --import-path ${GOPATH}/src --proto github.com/openconfig/gnmi/proto/gnmi/gnmi.proto describe
```

## Describe a service

```bash
grpcurl --plaintext --import-path ${GOPATH}/src --proto github.com/openconfig/gnmi/proto/gnmi/gnmi.proto describe gnmi.gNMI
```

## Describe methods from a service

```bash
grpcurl --plaintext --import-path ${GOPATH}/src --proto github.com/openconfig/gnmi/proto/gnmi/gnmi.proto describe gnmi.gNMI.Capabilities
grpcurl --plaintext --import-path ${GOPATH}/src --proto github.com/openconfig/gnmi/proto/gnmi/gnmi.proto describe gnmi.gNMI.Subscribe
```

## Describe messages used by methods

```bash
grpcurl --plaintext  --import-path ${GOPATH}/src  --proto github.com/openconfig/gnmi/proto/gnmi/gnmi.proto describe .gnmi.CapabilityRequest
grpcurl --plaintext  --import-path ${GOPATH}/src  --proto github.com/openconfig/gnmi/proto/gnmi/gnmi.proto describe .gnmi.SubscribeRequest
grpcurl --plaintext  --import-path ${GOPATH}/src  --proto github.com/openconfig/gnmi/proto/gnmi/gnmi.proto describe .gnmi.SubscriptionList
grpcurl --plaintext  --import-path ${GOPATH}/src  --proto github.com/openconfig/gnmi/proto/gnmi/gnmi.proto describe .gnmi.Subscription
```

## When describing messages, show a template of input data

The output will help you building working examples

```bash
grpcurl --plaintext --import-path ${GOPATH}/src -msg-template --proto github.com/openconfig/gnmi/proto/gnmi/gnmi.proto  describe .gnmi.SubscribeRequest
grpcurl --plaintext --import-path ${GOPATH}/src -msg-template --proto github.com/openconfig/gnmi/proto/gnmi/gnmi.proto describe .gnmi.Subscription 
grpcurl --plaintext --import-path ${GOPATH}/src -msg-template --proto github.com/openconfig/gnmi/proto/gnmi/gnmi.proto describe .gnmi.SubscriptionList
```

# Execute the method capabilities of the service gnmi.gNMI

```bash
grpcurl -H "Authorization: Bearer `cat token.tok`" -insecure \
-import-path ${GOPATH}/src  -proto github.com/openconfig/gnmi/proto/gnmi/gnmi.proto \
192.168.0.5:443 gnmi.gNMI/Capabilities
```
