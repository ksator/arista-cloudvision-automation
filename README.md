[![License](https://img.shields.io/badge/license-Apache_2.0-brightgreen.svg)](https://github.com/ksator/cloudvision-automation/blob/master/LICENSE)
[![CI](https://github.com/ksator/cloudvision-automation/actions/workflows/test.yml/badge.svg)](https://github.com/ksator/cloudvision-automation/actions)

**Table of Contents**

- [About this repository](#about-this-repository)
- [About the tools used in this repository](#about-the-tools-used-in-this-repository)
- [Requirements](#requirements)
- [CVP version](#cvp-version)
- [Credits](#credits)

# About this repository

This repository has CloudVision automation examples

- [GO](GO.md): How to install GO which is a requirement to install some tools
  - gRPCurl
  - gnmi
- [Token based authentication](token_based_authentication/): How to configure token based authentication which is a requirement in order to use CVP APIs
- [REST APIs](REST_APIs/): How to use REST APIs with
  - cURL
  - Wget
  - Postman
  - Python with the module requests
- [Resource APIs](resource_APIs/): How to use resources API with
  - cURL
  - gRPCurl
  - Postman
  - Python with the module
    - requests
    - cvprac
- [cvprac](cvprac/): How to use the Python module cvprac
- [Certificate based authentication](certificate_based_authentication): How to configure certificate based authentication (for the devices and CVP communication) which is a requirement for the devices to stream OpenConfig data to CVP
- [YANG](YANG/): How to generate paths and trees from YANG modules with
  - gNMIc
  - Pyang
- [OpenConfig](OpenConfig/): How to configure the devices to stream OpenConfig data to CVP
- [gNMI](gNMI/): How to use gNMI with
  - The gNMI command line client
    - gNMIc
    - gnmi
    - pygnmicli  
  - Python with the module pyGNMI
  - gRPCurl
  - Postman
- [RESTCONF](RESTCONF/): How to use RESTCONF with
  - cURL
  - Python with the module requests

# About the tools used in this repository

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

# Requirements

- CVP APIs require [token based authentication](Token_based_authentication).  
- [RESTCONF](RESTCONF) and [gNMI](gNMI) require to configure the devices to stream [OpenConfig](OpenConfig) data to CVP.  
- Configuring the devices to stream [OpenConfig](OpenConfig) data to CVP requires to use [certificate based authentication](Certificate_based_authentication/) (for devices and CVP communication).
  
# CVP version

All examples in this repository have been tested with CVP version 2022.1.0.

# Credits

Thank you to [Angélique Phillipps](https://github.com/aphillipps), [Khelil Sator](https://github.com/ksator), [Matthieu Tache](https://github.com/mtache) and [Tamas Plugor](https://github.com/noredistribution) for their contributions and guidances.
