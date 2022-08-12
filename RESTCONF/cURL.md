**Table of contents**

- [cURL options](#curl-options)
  - [Disable URL globbing](#disable-url-globbing)
  - [Ignore the warning about the certificates](#ignore-the-warning-about-the-certificates)
- [Get CVP inventory](#get-cvp-inventory)
  - [Get the `device-id` YANG leaf for all the devices from CVP inventory](#get-the-device-id-yang-leaf-for-all-the-devices-from-cvp-inventory)
- [Get OpenConfig data streamed by EOS devices and stored in CVP](#get-openconfig-data-streamed-by-eos-devices-and-stored-in-cvp)
  - [BGP](#bgp)
    - [Get the `state` YANG container for all the bgp neighbors](#get-the-state-yang-container-for-all-the-bgp-neighbors)
    - [Get the `session-state` YANG leaf for all the bgp neighbors](#get-the-session-state-yang-leaf-for-all-the-bgp-neighbors)
    - [Get the `config` YANG container for all the bgp neighbors](#get-the-config-yang-container-for-all-the-bgp-neighbors)
    - [Get the `config` YANG container for the bgp neighbor 172.16.200.1](#get-the-config-yang-container-for-the-bgp-neighbor-172162001)
    - [Get the `state` YANG container for the bgp neighbor 172.16.200.1](#get-the-state-yang-container-for-the-bgp-neighbor-172162001)
    - [Get the `session-state` YANG leaf for the bgp neighbor 172.16.200.1](#get-the-session-state-yang-leaf-for-the-bgp-neighbor-172162001)
  - [Interfaces](#interfaces)
    - [Get the `state` YANG container for all the interfaces](#get-the-state-yang-container-for-all-the-interfaces)
    - [Get the `state` YANG container of the interface Ethernet1](#get-the-state-yang-container-of-the-interface-ethernet1)
    - [Get the `counters` YANG container for all the interfaces](#get-the-counters-yang-container-for-all-the-interfaces)
    - [Get the `admin-status` YANG leaf for all the interfaces](#get-the-admin-status-yang-leaf-for-all-the-interfaces)
    - [Get the `admin-status` YANG leaf for the interface Ethernet6](#get-the-admin-status-yang-leaf-for-the-interface-ethernet6)
  - [Use `jq` to parse JSON in bash](#use-jq-to-parse-json-in-bash)
    - [Install `jq`](#install-jq)
    - [Pretty prints the JSON output](#pretty-prints-the-json-output)
    - [Filter the output to see only the interfaces `name`](#filter-the-output-to-see-only-the-interfaces-name)
    - [Filter the output to see only the `counters` container of the interface ethernet 1](#filter-the-output-to-see-only-the-counters-container-of-the-interface-ethernet-1)
    - [Filter the output to see only the `leaf` enabled of the container `config` of the interface ethernet 1](#filter-the-output-to-see-only-the-leaf-enabled-of-the-container-config-of-the-interface-ethernet-1)
    - [Filter the output to see only the devices id](#filter-the-output-to-see-only-the-devices-id)

# cURL options

## Disable URL globbing

By default cURL uses URL globbing. The globbing uses the reserved symbols [] and {} that normally cannot be part of a legal URL. If the URLs contain these symbols, disable URL globbing from cURL using the `-g` option.

## Ignore the warning about the certificates

Ignore the warning about the certificates with the `-k` option.

# Get CVP inventory

## Get the `device-id` YANG leaf for all the devices from CVP inventory

```bash
curl -s -k -X GET --header "Authorization: Bearer `cat token.tok`" 'https://192.168.0.5:443/restconf/data/inventory/state/device/device-id?arista-origin=arista&arista-target='
```

# Get OpenConfig data streamed by EOS devices and stored in CVP

Go to **Devices > Inventory** and replace the target in the commands below with the `device ID` found in the CVP device inventory.  
The `device ID` is the device SN.  

## BGP

### Get the `state` YANG container for all the bgp neighbors

```bash
curl -s -k -X GET --header 'Accept: application/json' --header "Authorization: Bearer `cat token.tok`" 'https://192.168.0.5/restconf/data/network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state?arista-target=spine1&arista-origin=openconfig'
```

### Get the `session-state` YANG leaf for all the bgp neighbors

```bash
curl -s -k -X GET --header 'Accept: application/json' --header "Authorization: Bearer `cat token.tok`" 'https://192.168.0.5/restconf/data/network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/session-state?arista-target=spine1&arista-origin=openconfig'
```

### Get the `config` YANG container for all the bgp neighbors

```bash
curl -s -k -X GET --header 'Accept: application/json' --header "Authorization: Bearer `cat token.tok`" 'https://192.168.0.5/restconf/data/network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/config?arista-target=spine1&arista-origin=openconfig'
```

### Get the `config` YANG container for the bgp neighbor 172.16.200.1 

```bash
curl -s -g -k -X GET --header 'Accept: application/json' --header "Authorization: Bearer `cat token.tok`" 'https://192.168.0.5/restconf/data/network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor[neighbor-address=172.16.200.1]/config?arista-target=spine1&arista-origin=openconfig'
```

### Get the `state` YANG container for the bgp neighbor 172.16.200.1 

```bash
curl -s -g -k -X GET --header 'Accept: application/json' --header "Authorization: Bearer `cat token.tok`" 'https://192.168.0.5/restconf/data/network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor[neighbor-address=172.16.200.1]/state?arista-target=spine1&arista-origin=openconfig'
```

### Get the `session-state` YANG leaf for the bgp neighbor 172.16.200.1 

```bash
curl -s -g -k -X GET --header 'Accept: application/json' --header "Authorization: Bearer `cat token.tok`" 'https://192.168.0.5/restconf/data/network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor[neighbor-address=172.16.200.1]/state/session-state?arista-target=spine1&arista-origin=openconfig'
```

## Interfaces

### Get the `state` YANG container for all the interfaces

```bash
curl -s -k -X GET --header 'Accept: application/json' --header "Authorization: Bearer `cat token.tok`" 'https://192.168.0.5/restconf/data/interfaces/interface/state?arista-target=spine1&arista-origin=openconfig'
```

### Get the `state` YANG container of the interface Ethernet1

```bash
curl -s -k -g -X GET --header 'Accept: application/json' --header "Authorization: Bearer `cat token.tok`" 'https://192.168.0.5/restconf/data/interfaces/interface[name=Ethernet1]/state?arista-target=spine1&arista-origin=openconfig'
```

### Get the `counters` YANG container for all the interfaces

```bash
curl -s -k -X GET --header 'Accept: application/json' --header "Authorization: Bearer `cat token.tok`" 'https://192.168.0.5/restconf/data/interfaces/interface/state/counters?arista-target=spine1&arista-origin=openconfig'
```

### Get the `admin-status` YANG leaf for all the interfaces

```bash
curl -s -k -X GET --header 'Accept: application/json' --header "Authorization: Bearer `cat token.tok`" 'https://192.168.0.5/restconf/data/interfaces/interface/state/admin-status?arista-target=spine1&arista-origin=openconfig'
```

### Get the `admin-status` YANG leaf for the interface Ethernet6

```bash
curl -s -g -k -X GET --header 'Accept: application/json' --header "Authorization: Bearer `cat token.tok`" 'https://192.168.0.5/restconf/data/interfaces/interface[name=Ethernet6]/state/admin-status?arista-target=spine1&arista-origin=openconfig'
```

## Use `jq` to parse JSON in bash

### Install `jq`

```bash
sudo apt-get install -y jq
```

### Pretty prints the JSON output 

```bash
curl -s -k -X GET --header 'Accept: application/json' --header "Authorization: Bearer `cat token.tok`" 'https://192.168.0.5/restconf/data/interfaces/interface/state?arista-target=leaf1&arista-origin=openconfig' | jq .
```

```bash
curl -s -k -g -X GET --header 'Accept: application/json' --header "Authorization: Bearer `cat token.tok`" 'https://192.168.0.5/restconf/data/interfaces/interface[name=Ethernet1]?arista-target=leaf1&arista-origin=openconfig' | jq .
```

### Filter the output to see only the interfaces `name` 

```bash
curl -s -k -X GET --header 'Accept: application/json' --header "Authorization: Bearer `cat token.tok`" 'https://192.168.0.5/restconf/data/interfaces/interface?arista-target=leaf1&arista-origin=openconfig' | jq .interfaces.interface[].name
```

### Filter the output to see only the `counters` container of the interface ethernet 1

```bash
curl -s -k -g -X GET --header 'Accept: application/json' --header "Authorization: Bearer `cat token.tok`" 'https://192.168.0.5/restconf/data/interfaces/interface[name=Ethernet1]?arista-target=leaf1&arista-origin=openconfig' | jq .interfaces.interface[0].state.counters
```

### Filter the output to see only the `leaf` enabled of the container `config` of the interface ethernet 1

```bash
curl -s -k -g -X GET --header 'Accept: application/json' --header "Authorization: Bearer `cat token.tok`" 'https://192.168.0.5/restconf/data/interfaces/interface[name=Ethernet1]?arista-target=leaf1&arista-origin=openconfig' | jq .interfaces.interface[0].config.enabled
```

### Filter the output to see only the devices id

```bash
curl -s -k -X GET --header "Authorization: Bearer `cat token.tok`" 'https://192.168.0.5:443/restconf/data/inventory/state/device/device-id?arista-origin=arista&arista-target=' | jq '.inventory.state.device[]."device-id"'
```
