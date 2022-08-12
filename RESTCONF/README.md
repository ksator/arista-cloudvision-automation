**Table of Contents**

- [About RESTCONF](#about-restconf)
  - [RESTCONF and EOS Switches](#restconf-and-eos-switches)
  - [RESTCONF and CVP](#restconf-and-cvp)
    - [About RESTCONF and CVP](#about-restconf-and-cvp)
    - [Requirements](#requirements)
      - [Configure the devices to stream OpenConfig data to CVP](#configure-the-devices-to-stream-openconfig-data-to-cvp)
      - [Token based authentication](#token-based-authentication)
    - [Origin and target](#origin-and-target)
    - [DeviceID](#deviceid)
    - [URL Format](#url-format)
    - [OpenConfig paths](#openconfig-paths)
- [RESTCONF examples](#restconf-examples)

# About RESTCONF

RESTCONF is defined in the [RFC 8040](https://datatracker.ietf.org/doc/html/rfc8040).

The following RESTCONF methods are sent by the client:

- GET: to retrieve data for a resource
- POST: to create a data resource
- PUT: to create or replace the target data resource
- DELETE: to delete the target resource
- HEAD: to retrieve the header fields (which contain the metadata for a resource) that would be returned for the comparable GET method, without the response message-body. It is supported for all resources that support the GET method

## RESTCONF and EOS Switches

EOS supports the 5 RESTCONF methods.

EOS can be configured to run a RESTCONF server.

Examples: https://github.com/arista-netdevops-community/restconf_demo_with_arista

## RESTCONF and CVP

### About RESTCONF and CVP

Once we configured the devices to stream OpenConfig data to CVP, we can use RESTCONF and the GET method to retrieve OpenConfig data from CVP.

Only the RESTCONF GET method is supported with CVP.

This [document](https://aristanetworks.force.com/AristaCommunity/s/article/Understanding-CloudVIsion-APIs-and-accessing-NetDB-data) describes how to access OpenConfig data streamed by the devices to CVP using RESTCONF.

**Note:** This is not yet fully supported by Arista so do not use it on production

### Requirements

#### Configure the devices to stream OpenConfig data to CVP

Refer to the [OpenConfig directory](../OpenConfig)

#### Token based authentication

To use RESTCONF with CVP, token based authentication is required.  
To enable token based authentication, refer to [this directory](../Token%20based%20authentication) and copy the token into an environment variable.

```bash
token=xxxxx
echo $token
```

We can now use RESTCONF to access device OpenConfig data on CVP.

### Origin and target

`arista-origin`and `arista-target` need to be added as query arguments in the URL:

- The default `arista-origin` is `arista`
  - `arista-origin` is `arista` for CVP data (inventory ...)
  - `arista-origin` is `openconfig` for the data streamed by devices to CVP
- The default `arista-target` is CVP.
  - To get the states of a device, `arista-target` must be the deviceID (SN of the switch).

### DeviceID

The deviceID is the device SN.  
on CVP GUI, go to **Devices > Inventory** to get the device SN.  

### URL Format

To get CVP data (inventory ...), here's the URL format:  
```https://{{cvp_ip_address}}/restconf/data/{{cvp_path}}?arista-origin=arista&arista-target=```

To get the OpenConfig data streamed by a device to CVP, here's the URL format:  
```https://{{cvp_ip_address}}/restconf/data/{{OpenConfig_path}}?arista-target={{device_SN}}&arista-origin=openconfig```

### OpenConfig paths

Use the telemetry browser on CVP GUI (**Settings and Tools** > **Developper Tools** > **Telemetry Browser**) to view the OpenConfig data stored in CloudVision telemetry database. The paths in CVP are not exactly the OpenConfig paths. You will need to manipulate them to be able to use them with cURL or requests.

Refer to the [YANG](../YANG/) directory to understand how to generate paths and trees from YANG modules.

# RESTCONF examples

You will find here RESTCONF examples for CVP using:

- The **cURL** command-line tool
- The **requests** Python library
