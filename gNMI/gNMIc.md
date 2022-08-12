**Table of contents**

- [About gNMIc](#about-gnmic)
- [Install gNMIc on your automation setup](#install-gnmic-on-your-automation-setup)
- [Generate data from YANG files](#generate-data-from-yang-files)
  - [Generate paths](#generate-paths)
  - [Generate a tree representation for quick visualization](#generate-a-tree-representation-for-quick-visualization)
- [Subscribe to CVP models](#subscribe-to-cvp-models)
  - [Capabilities RPC](#capabilities-rpc)
  - [Subscribe RPC](#subscribe-rpc)
    - [ONCE mode](#once-mode)
    - [STREAM with ON_CHANGE mode](#stream-with-on_change-mode)
- [Subscribe to OpenConfig data streamed by EOS devices and stored in CVP](#subscribe-to-openconfig-data-streamed-by-eos-devices-and-stored-in-cvp)
  - [Interfaces](#interfaces)
    - [Subscribe to the `counters` YANG container for all interfaces](#subscribe-to-the-counters-yang-container-for-all-interfaces)
    - [Subscribe to the `admin status` YANG leaf for the interface Ethernet1](#subscribe-to-the-admin-status-yang-leaf-for-the-interface-ethernet1)
  - [BGP](#bgp)
    - [Subscribe to the `bgp` YANG container](#subscribe-to-the-bgp-yang-container)
    - [Subscribe to the `state` YANG container for all bgp neighbors](#subscribe-to-the-state-yang-container-for-all-bgp-neighbors)
    - [Subscribe to the `session-state` YANG leaf for the bgp neighbor 172.16.200.2 in default VRF](#subscribe-to-the-session-state-yang-leaf-for-the-bgp-neighbor-172162002-in-default-vrf)
    - [Subscribe to the `config` YANG container for the bgp neighbor 172.16.200.1](#subscribe-to-the-config-yang-container-for-the-bgp-neighbor-172162001)
    - [Subscribe to the `state` YANG container for the bgp neighbor 172.16.200.1 in the default VRF](#subscribe-to-the-state-yang-container-for-the-bgp-neighbor-172162001-in-the-default-vrf)
  - [gNMI History Extension](#gnmi-history-extension)
    - [Get interfaces counters of a device at a specific time](#get-interfaces-counters-of-a-device-at-a-specific-time)
    - [Get interface counters of a device at a specified time range](#get-interface-counters-of-a-device-at-a-specified-time-range)
  - [Use `jq` to parse JSON in bash](#use-jq-to-parse-json-in-bash)
    - [Install `jq`](#install-jq)
    - [Pretty prints the JSON output](#pretty-prints-the-json-output)
    - [Filter the output to see only the paths](#filter-the-output-to-see-only-the-paths)
    - [Filter the output to see only the values of the `leaves` under the `counters` container for the interface Ethernet4](#filter-the-output-to-see-only-the-values-of-the-leaves-under-the-counters-container-for-the-interface-ethernet4)

# About gNMIc

gNMIc is a gNMI client

gNMIc documentation https://gnmic.kmrd.dev/  
gNMIc source code https://github.com/karimra/gnmic

# Install gNMIc on your automation setup

```bash
bash -c "$(curl -sL https://get-gnmic.kmrd.dev)"
```

```bash
gnmic version
gnmic help
```

# Generate data from YANG files

Copy all the YANG files from OpenConfig repository to the local directory

```bash
mkdir yang_modules
git clone https://github.com/openconfig/public.git
cp public/release/models/*.yang yang_modules/.
cp -R public/release/models/*/*.yang yang_modules/.
cp public/third_party/ietf/*.yang yang_modules/.
cd yang_modules/
ls
```

## Generate paths

```bash
gnmic generate path --file openconfig-interfaces.yang --state-only
gnmic generate path --file openconfig-interfaces.yang --types
```

## Generate a tree representation for quick visualization

```bash
gnmic generate --file openconfig-interfaces.yang
gnmic generate --file openconfig-interfaces.yang --json 
```

# Subscribe to CVP models

## Capabilities RPC

```bash
gnmic -a 192.168.0.5:443 capabilities --token=$token --skip-verify
```

## Subscribe RPC

### ONCE mode

Get the `device-id` YANG leaf for all devices from CVP inventory

```bash
gnmic -a 192.168.0.5:443 --mode=once subscribe --path /inventory/state/device/device-id --token=$token --skip-verify
```

### STREAM with ON_CHANGE mode

Subscribe to the `device-id` YANG leaf for all devices from CVP inventory

```bash
gnmic -a 192.168.0.5:443 --mode=stream subscribe  --path  /inventory/state/device/device-id --token=$token --skip-verify --stream-mode ON_CHANGE
```

# Subscribe to OpenConfig data streamed by EOS devices and stored in CVP

Go to **Devices > Inventory** and replace the target in the commands below with the `device ID` found in the CVP device inventory.  
The `device ID` is the device SN.  

## Interfaces

### Subscribe to the `counters` YANG container for all interfaces

```bash
gnmic -a 192.168.0.5:443 subscribe --path "openconfig:/interfaces/interface/state/counters" --token=$token --target=leaf1 --skip-verify
```

### Subscribe to the `admin status` YANG leaf for the interface Ethernet1

```bash
gnmic -a 192.168.0.5:443 subscribe --path "openconfig:/interfaces/interface[name=Ethernet1]/state/admin-status" --token=$token --target=leaf1 --skip-verify
```

## BGP

### Subscribe to the `bgp` YANG container

```bash
gnmic -a 192.168.0.5:443 subscribe --path "openconfig:/network-instances/network-instance/protocols/protocol/bgp/" --token=$token --target=leaf1 --skip-verify
```

### Subscribe to the `state` YANG container for all bgp neighbors

```bash
gnmic -a 192.168.0.5:443 subscribe --path "openconfig:/network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state" --token=$token --target=leaf1 --skip-verify
```

### Subscribe to the `session-state` YANG leaf for the bgp neighbor 172.16.200.2 in default VRF

```bash
gnmic -a 192.168.0.5:443 subscribe --path "openconfig:network-instances/network-instance[name=default]/protocols/protocol/bgp/neighbors/neighbor[neighbor-address=172.16.0.2]/state/session-state" --token=$token --target=leaf1 --skip-verify
```

### Subscribe to the `config` YANG container for the bgp neighbor 172.16.200.1

```bash
gnmic -a 192.168.0.5:443 subscribe --path "openconfig:/network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor[neighbor-address=172.16.200.1]/config" --token=$token --target=leaf1 --skip-verify
```

### Subscribe to the `state` YANG container for the bgp neighbor 172.16.200.1 in the default VRF

```bash
gnmic -a 192.168.0.5:443 subscribe --path "openconfig:/network-instances/network-instance[name=default]/protocols/protocol/bgp/neighbors/neighbor[neighbor-address=172.16.200.1]/state" --token=$token --target=leaf1 --skip-verify
```

## gNMI History Extension

This is defined in this repository https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-history.md

This allow to:

- retrieve data at a specific time in the past
- request all updates applied to a data tree between two specified times

### Get interfaces counters of a device at a specific time

```bash
gnmic -a 192.168.0.5:443 subscribe \
    --path "openconfig:/interfaces/interface/state/counters" \
    --token=`cat token.tok` --mode=once --target=spine1 \
    --skip-verify  --history-snapshot=2022-07-17T12:56:00Z
```

### Get interface counters of a device at a specified time range

```bash
gnmic -a 192.168.0.5:443 subscribe \
    --path "openconfig:/interfaces/interface/state/counters" \
    --token=`cat token.tok` --mode=stream --target=spine1 --skip-verify\
    --history-start=2022-07-17T12:53:00Z  --history-end=2022-07-17T12:55:00Z 
```

## Use `jq` to parse JSON in bash

### Install `jq`

```bash
sudo apt-get install -y jq
```

### Pretty prints the JSON output

```bash
gnmic -a 192.168.0.5:443 subscribe --path "openconfig:/interfaces/interface/state/counters" --token=$token --target=leaf1 --skip-verify | jq .
```

### Filter the output to see only the paths

```bash
gnmic -a 192.168.0.5:443 subscribe --path "openconfig:/interfaces/interface/state/counters" --token=$token --target=leaf1 --skip-verify | jq .updates[].Path
```

### Filter the output to see only the values of the `leaves` under the `counters` container for the interface Ethernet4

```bash
gnmic -a 192.168.0.5:443 subscribe --path "openconfig:/interfaces/interface[name=Ethernet4]/state/counters" --token=$token --target=leaf1 --skip-verify | jq .updates[].values
```
