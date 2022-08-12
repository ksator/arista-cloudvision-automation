**Table of Contents**

- [About the gnmi tool](#about-the-gnmi-tool)
- [gnmi installation](#gnmi-installation)
  - [Install GO on your automation setup](#install-go-on-your-automation-setup)
  - [Install the gnmi tool on your automation setup](#install-the-gnmi-tool-on-your-automation-setup)
- [Use gnmi](#use-gnmi)
  - [Subscribe to OpenConfig data streamed by EOS devices and stored in CVP](#subscribe-to-openconfig-data-streamed-by-eos-devices-and-stored-in-cvp)
    - [Subscribe to the admin-status YANG leaf for all the interfaces of the device spine1](#subscribe-to-the-admin-status-yang-leaf-for-all-the-interfaces-of-the-device-spine1)
    - [Subscribe to interface Ethernet2 admin-status of the device spine1 at a specific time](#subscribe-to-interface-ethernet2-admin-status-of-the-device-spine1-at-a-specific-time)
    - [Subscribe to interface Ethernet2 admin-status of the device spine1 at a specific time range](#subscribe-to-interface-ethernet2-admin-status-of-the-device-spine1-at-a-specific-time-range)

# About the gnmi tool

**gnmi** is a command-line gNMI client.  

source code https://github.com/aristanetworks/goarista/tree/master/cmd/gnmi

# gnmi installation

## Install GO on your automation setup

GO is required to install gnmi.  
Please follow these [instructions to install GO](../../GO.md) on your automation setup

## Install the gnmi tool on your automation setup

This will install the gnmi binary in the $HOME/go/bin directory.

```bash
go install github.com/aristanetworks/goarista/cmd/gnmi@latest
```

```bash
ls $GOPATH/pkg/mod/github.com
ls $GOPATH/bin/
ls $HOME/go/bin/
gnmi  --help
```

# Use gnmi

Go to **Devices > Inventory** and replace the target in the commands below with the `device ID` found in the CVP device inventory.  
The `device ID` is the device SN.  

## Subscribe to OpenConfig data streamed by EOS devices and stored in CVP

### Subscribe to the admin-status YANG leaf for all the interfaces of the device spine1

```bash
gnmi -addr=192.168.0.5:443 -token=`cat token.tok` -mode=stream subscribe \
    origin=openconfig target=spine1 /interfaces/interface/state/admin-status
```

### Subscribe to interface Ethernet2 admin-status of the device spine1 at a specific time

```bash
gnmi -addr=192.168.0.5:443 -token=`cat token.tok` -mode=once \
    -history_snapshot=2022-07-17T12:48:00Z subscribe origin=openconfig \
    target=spine1 /interfaces/interface[name=Ethernet2]/state/admin-status
```

### Subscribe to interface Ethernet2 admin-status of the device spine1 at a specific time range

```bash
gnmi -addr=192.168.0.5:443 -token=`cat token.tok` -mode=stream \
-history_start=2022-07-17T12:48:00Z -history_end=2022-07-17T16:04:00Z \
subscribe origin=openconfig target=spine1 /interfaces/interface[name=Ethernet2]/state/admin-status
```
