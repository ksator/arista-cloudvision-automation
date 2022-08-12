**Table of contents**

- [About gRPCurl](#about-grpcurl)
- [Install GO on your automation setup](#install-go-on-your-automation-setup)
- [Install gRPCurl on your automation setup](#install-grpcurl-on-your-automation-setup)
- [Clone the repo on your automation setup](#clone-the-repo-on-your-automation-setup)
- [List from a proto file on your automation setup](#list-from-a-proto-file-on-your-automation-setup)
  - [List all services](#list-all-services)
  - [List all methods from a service](#list-all-methods-from-a-service)
- [Describe from a proto file on your automation setup](#describe-from-a-proto-file-on-your-automation-setup)
  - [Describe a service](#describe-a-service)
  - [Describe a method](#describe-a-method)
- [Server reflection](#server-reflection)
- [List from a gRPC server (CVP)](#list-from-a-grpc-server-cvp)
  - [List all services](#list-all-services-1)
  - [List all methods from a service](#list-all-methods-from-a-service-1)
- [Describe from a gRPC server (CVP)](#describe-from-a-grpc-server-cvp)
  - [Describe a service](#describe-a-service-1)
  - [Describe a method](#describe-a-method-1)
- [Get inventory from CVP](#get-inventory-from-cvp)
  - [Execute the GetAll method from arista.inventory.v1.DeviceService service](#execute-the-getall-method-from-aristainventoryv1deviceservice-service)
    - [Without filter](#without-filter)
    - [With a filter](#with-a-filter)
  - [Execute the Subscribe method from arista.inventory.v1.DeviceService service](#execute-the-subscribe-method-from-aristainventoryv1deviceservice-service)
  - [Execute the GetOne method from arista.inventory.v1.DeviceService service](#execute-the-getone-method-from-aristainventoryv1deviceservice-service)

# About gRPCurl

gRPCurl is a command-line tool that lets you interact with gRPC servers. It's basically curl for gRPC servers.  

You can invoke RPC methods on a gRPC server from the command-line.  

You can also inspect gRPC services, either by querying a server that supports server reflection, or by reading proto source files.  
So, if the server you interact with does not support reflection, you can use the proto source files that define the service.  

gRPCurl source code: https://github.com/fullstorydev/grpcurl

# Install GO on your automation setup

GO is required to install gRPCurl.  
Please follow these [instructions to install GO](../../GO.md) on your automation setup

# Install gRPCurl on your automation setup

gRPCurl is a command-line tool that lets you interact with gRPC servers. It's basically curl for gRPC servers.  
CVP is the gRPC server.  

```bash
go install github.com/fullstorydev/grpcurl/cmd/grpcurl@latest
```

```bash
ls $GOPATH/pkg/mod/github.com/fullstorydev/
ls $GOPATH/bin/
grpcurl  --help
```

# Clone the repo on your automation setup

```bash
git clone https://github.com/aristanetworks/cloudvision-apis.git $GOPATH/src/github.com/cloudvision-apis
```

# List from a proto file on your automation setup

## List all services

```bash
grpcurl --plaintext  --import-path ${GOPATH}/src/github.com/cloudvision-apis  --proto ${GOPATH}/src/github.com/cloudvision-apis/arista/inventory.v1/services.gen.proto list
grpcurl --plaintext  --import-path ${GOPATH}/src/github.com/cloudvision-apis  --proto ${GOPATH}/src/github.com/cloudvision-apis/arista/tag.v2/services.gen.proto list
grpcurl --plaintext  --import-path ${GOPATH}/src/github.com/cloudvision-apis  --proto arista/tag.v2/services.gen.proto list
```

## List all methods from a service

```bash
grpcurl --plaintext  --import-path ${GOPATH}/src/github.com/cloudvision-apis  --proto ${GOPATH}/src/github.com/cloudvision-apis/arista/inventory.v1/services.gen.proto list arista.inventory.v1.DeviceService
```

# Describe from a proto file on your automation setup

## Describe a service

```bash
grpcurl --plaintext  --import-path ${GOPATH}/src/github.com/cloudvision-apis  --proto ${GOPATH}/src/github.com/cloudvision-apis/arista/tag.v2/services.gen.proto describe arista.tag.v2.TagAssignmentService
grpcurl --plaintext  --import-path ${GOPATH}/src/github.com/cloudvision-apis  --proto arista/tag.v2/services.gen.proto describe arista.tag.v2.TagAssignmentService
grpcurl --plaintext  --import-path ${GOPATH}/src/github.com/cloudvision-apis  --proto arista/tag.v2/services.gen.proto describe arista.tag.v2.TagService
```

## Describe a method

```bash
grpcurl --plaintext  --import-path ${GOPATH}/src/github.com/cloudvision-apis  --proto ${GOPATH}/src/github.com/cloudvision-apis/arista/inventory.v1/services.gen.proto describe arista.inventory.v1.DeviceService.GetAll
grpcurl --plaintext  --import-path ${GOPATH}/src/github.com/cloudvision-apis  --proto ${GOPATH}/src/github.com/cloudvision-apis/arista/inventory.v1/services.gen.proto describe arista.inventory.v1.DeviceService.GetOne
```

# Server reflection

Server reflection is enabled on CVP so we can use a gRPCurl to inspect the gRPC services from CVP through server reflection (i.e you do not have to use the proto source file to inspect the gRPC services).

# List from a gRPC server (CVP)

## List all services

Run this command on your automation setup to list all services

```bash
grpcurl -H "Authorization: Bearer `cat token.tok`" -insecure 192.168.0.5:443 list
```

## List all methods from a service

```bash
grpcurl -H "Authorization: Bearer `cat token.tok`" -insecure 192.168.0.5:443 list arista.inventory.v1.DeviceService
```

# Describe from a gRPC server (CVP)

## Describe a service

```bash
grpcurl -H "Authorization: Bearer `cat token.tok`" -insecure 192.168.0.5:443 describe arista.inventory.v1.DeviceService
```

## Describe a method

```bash
grpcurl -H "Authorization: Bearer `cat token.tok`" -insecure 192.168.0.5:443 describe arista.inventory.v1.DeviceService.GetAll
```

# Get inventory from CVP

## Execute the GetAll method from arista.inventory.v1.DeviceService service

### Without filter

Run this command on your automation setup

```bash
grpcurl -H  "Authorization: Bearer `cat token.tok`"  -proto arista/inventory.v1/services.gen.proto  -format json -format-error --import-path ${GOPATH}/src/github.com/cloudvision-apis/ -insecure 192.168.0.5:443 arista.inventory.v1.DeviceService/GetAll
```

### With a filter

Run this command on your automation setup

```bash
grpcurl -H  "Authorization: Bearer `cat token.tok`"  -proto arista/inventory.v1/services.gen.proto  -format json -format-error --import-path ${GOPATH}/src/github.com/cloudvision-apis/  -insecure  -d '{"partialEqFilter": [{"softwareVersion":"4.27.2F","streamingStatus":"STREAMING_STATUS_ACTIVE"}]}' 192.168.0.5:443 arista.inventory.v1.DeviceService/GetAll
```

## Execute the Subscribe method from arista.inventory.v1.DeviceService service

Run this command on your automation setup

```bash
grpcurl -H  "Authorization: Bearer `cat token.tok`"  -proto arista/inventory.v1/services.gen.proto  -format json -format-error --import-path ${GOPATH}/src/github.com/cloudvision-apis/ -insecure 192.168.0.5:443 arista.inventory.v1.DeviceService/Subscribe
```

## Execute the GetOne method from arista.inventory.v1.DeviceService service

Run this command on your automation setup

```bash
grpcurl -H  "Authorization: Bearer `cat token.tok`"  -proto arista/inventory.v1/services.gen.proto  -format json -format-error --import-path ${GOPATH}/src/github.com/cloudvision-apis/  -insecure  -d '{"key": {"deviceId": "spine1"}}' 192.168.0.5:443 arista.inventory.v1.DeviceService/GetOne
```
