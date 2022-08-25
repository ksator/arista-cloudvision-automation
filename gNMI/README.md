**Table of Contents**

- [About gNMI](#about-gnmi)
- [gNMI and EOS Switches](#gnmi-and-eos-switches)
- [gNMI and CVP](#gnmi-and-cvp)
  - [About gNMI and CVP](#about-gnmi-and-cvp)
  - [Requirements](#requirements)
    - [Configure the devices to stream OpenConfig data to CVP](#configure-the-devices-to-stream-openconfig-data-to-cvp)
    - [Token based authentication](#token-based-authentication)
  - [Origin and target](#origin-and-target)
  - [DeviceID](#deviceid)
  - [OpenConfig paths](#openconfig-paths)
  - [Examples](#examples)

# About gNMI

gNMI stands for gRPC Network Management Interface.

gNMI specifications are defined in this [repository](https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md)

The gNMI proto file is [here](https://github.com/openconfig/gnmi/blob/master/proto/gnmi/gnmi.proto)  

gNMI is the gRPC service. The Remote Procedure Calls (RPC)  methods of the gNMI service are:

- CAPABILITIES: to discover the capabilities of the target
- SET: to modify the state of the target
- GET: to retrieve snapshots from the target for a specified set of paths
- SUBSCRIBE: to subscribe to updates from the target for a specified set of paths.
  
# gNMI and EOS Switches

EOS supports the 4 gNMI RPCs described above.

The target is a network device. The gNMI server runs on the target.

The gNMI client, typically in a collector or in a network management system, sends the RPCs to the targets to modify and collect data.

Examples:

- https://github.com/arista-netdevops-community/gnmi_demo_with_arista_eos
- https://github.com/arista-netdevops-community/automation_and_telemetry_demo

# gNMI and CVP

## About gNMI and CVP

CVP is the gNMI server.  

Once we configured the devices to stream OpenConfig data to CVP, we can use gNMI to access to OpenConfig data on CVP.

CVP supports 2 gNMI RPCs:

- CAPABILITIES
- SUBSCRIBE

SUBSCRIBE has two modes:

- ONCE: Equivalent of a GET RPC. Returns all data matching the subscription path at the specified time
- STREAM: Returns the same as ONCE + subsequent updates until the client closes the subscription

This [document](https://aristanetworks.force.com/AristaCommunity/s/article/Understanding-CloudVIsion-APIs-and-accessing-NetDB-data) describes how to access OpenConfig data streamed by the devices to CVP using gNMI.

**Note:** This is not yet fully supported by Arista so do not use it on production

## Requirements

### Configure the devices to stream OpenConfig data to CVP

Refer to the [OpenConfig directory](../OpenConfig)

### Token based authentication

To use gNMI with CVP, token based authentication is required. To enable token based authentication, refer to [this directory](../token_based_authentication) and copy the token into an environment variable.

```bash
token=xxxxx
echo $token
```

We can now use gNMI to access device OpenConfig data on CVP.

## Origin and target

- The default `arista-origin` is `arista`
  - `arista-origin` is `arista` for CVP data (inventory ...)
  - `arista-origin` is `openconfig` for the data streamed by devices to CVP
- The default `arista-target` is CVP.
  - To get the states of a device, `arista-target` must be the deviceID (SN of the switch).

## DeviceID

The deviceID is the device SN.  
on CVP GUI, go to **Devices > Inventory** to get the device SN.  

## OpenConfig paths

Use the telemetry browser on CVP GUI (**Settings and Tools** > **Developper Tools** > **Telemetry Browser**) to view the OpenConfig data stored in CloudVision telemetry database. The paths in CVP are not exactly the OpenConfig paths. You will need to manipulate them to be able to use them with a gNMI client.

Refer to the [YANG](../YANG/) lab to understand how to generate paths and trees from YANG modules.

## Examples

You will find in this directory examples using:

- The gNMI command-line client:
  - **gNMIc**
  - **gnmi**
  - **pygnmicli**
- The **pyGNMI** Python library
- The **gRPCurl** command line tool
- **Postman** using gPRC
