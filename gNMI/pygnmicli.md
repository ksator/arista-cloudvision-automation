**Table of contents**

- [About pygnmicli](#about-pygnmicli)
- [Install pygnmicli on your automation setup](#install-pygnmicli-on-your-automation-setup)
- [Capabilities RPC](#capabilities-rpc)
- [Subscribe RPC](#subscribe-rpc)

# About pygnmicli

pygnmicli is a gNMI command line client

# Install pygnmicli on your automation setup

Install the pygnmi python library on your automation setup

```bash
pip install pygnmi==0.8.5
pip list
```

```bash
ls /home/arista/.local/bin | grep pygnmicli
echo $PATH
export PATH=/home/arista/.local/bin:$PATH
echo $PATH
```

```bash
pygnmicli --help
```

# Capabilities RPC

```bash
pygnmicli -t "192.168.0.5:443" --token `cat token.tok` -o capabilities
cat log/execution.log 
```

# Subscribe RPC

```bash
pygnmicli -t "192.168.0.5:443" --token `cat token.tok` -o subscribe-once -x /inventory/state/device/device-id
pygnmicli -t "192.168.0.5:443" --token `cat token.tok` -o subscribe-once -x arista:/inventory/state/device/device-id
pygnmicli -t "192.168.0.5:443" --token `cat token.tok` -o subscribe-once -x openconfig:/interfaces/interface[name=Ethernet2]/state/admin-status --gnmi-path-target leaf1
```

```bash
pygnmicli -t "192.168.0.5:443" --token `cat token.tok` -o subscribe-stream -x openconfig:/interfaces/interface[name=Ethernet2]/state/admin-status --gnmi-path-target leaf1
```
