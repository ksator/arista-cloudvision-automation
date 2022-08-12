[![License](https://img.shields.io/badge/license-Apache%202.0-brightgreen.svg)](https://github.com/ksator/cvp-automation/blob/master/LICENSE)

**Table of Contents**

- [About this repository](#about-this-repository)
  - [Repository description](#repository-description)
  - [About the tools used in this repository](#about-the-tools-used-in-this-repository)
  - [Requirements](#requirements)
  - [CVP version](#cvp-version)

# About this repository

This repository has CVP automation examples

## Repository description

- [Certificate based authentication](Certificate%20based%20authentication): How to configure certificate based authentication (for the devices and CVP communication) which is required for the devices to stream OpenConfig data to CVP
- [cvprac](cvprac/): How to use the Python module cvprac
- [gNMI](gNMI/): How to use gNMI with various gNMI clients
  - gNMIc
  - gnmi
  - gRPCurl
  - pygnmicli
  - Python with the module pyGNMI
- [GO](GO.md): How to install GO which is a requirement to install some tools
  - gRPCurl
  - gnmi
- [OpenConfig](OpenConfig/): How to configure the devices to stream OpenConfig data to CVP
- [Resource APIs](Resource%20APIs/): How to use resources API with various tools
  - cURL
  - gRPCurl
  - Python with the module
    - requests
    - cvprac
- [REST APIs](REST%20APIs/): How to use REST APIs with various tools
  - cURL
  - Wget
  - Postman
  - Python with the module requests
- [RESTCONF](RESTCONF/): How to use RESTCONF with various tools
  - cURL
  - Python with the module requests
- [Token based authentication](Token%20based%20authentication/): How to configure token based authentication which is a requirement in order to use CVP APIs
- [YANG](YANG/): How to generate paths and trees from YANG modules with various tools
  - gNMIc
  - Pyang

## About the tools used in this repository

- **cURL** is a command-line tool for getting or sending data using URLs
- **Wget** is a program that retrieves content from web servers
- **Postman** can be used to explore and test REST APIs and gRPC services
- **Python** with the following modules:
  - The **requests** library can be used for making HTTP requests in Python
  - The **cvprac** python library can be used to manage CVP. cvprac is written using CVP REST APIs an CVP resource APIs
  - The **pyGNMI** library is a gNMI client
- **gNMIc** is a command-line gNMI client
- **gnmi** is a command-line gNMI client
- **pygnmicli** is a command-line gNMI client
- **pyang** can be used to generate a tree representation of YANG models for quick visualization
- **gRPCurl** is a command-line tool that lets you interact with gRPC servers. It's basically curl for gRPC servers  

## Requirements

CVP APIs require [token based authentication](Token%20based%20authentication).  

[RESTCONF](RESTCONF) and [gNMI](gNMI) require:

- To configure the devices to stream OpenConfig data to CVP.
- Configuring the devices to stream OpenConfig data to CVP require to use certificate based authentication (for EOS and CVP communication).
  
So [RESTCONF](RESTCONF) and [gNMI](gNMI) require:

- [Certificate based authentication](Certificate%20based%20authentication/) (for EOS and CVP communication)
- [YANG](YANG)
- [OpenConfig](OpenConfig)
- [Token based authentication](Token%20based%20authentication) (required for all CVP APIs)

## CVP version

All examples in this repository have been tested with CVP version 2022.1.0.
