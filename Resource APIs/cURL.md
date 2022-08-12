**Table of contents**
- [Get inventory of all devices](#get-inventory-of-all-devices)
- [Get one device using it's serial number](#get-one-device-using-its-serial-number)
- [Filter the request](#filter-the-request)
  - [Get active tags](#get-active-tags)
  - [Get all device tags](#get-all-device-tags)
  - [Get all interface tags](#get-all-interface-tags)
  - [Get inventory of all devices running EOS 4.27.2F](#get-inventory-of-all-devices-running-eos-4272f)
  - [Get all devices running EOS 4.27.2F and with an active streaming status](#get-all-devices-running-eos-4272f-and-with-an-active-streaming-status)
  - [Get all devices running EOS 4.27.2F or EOS 4.27.1F](#get-all-devices-running-eos-4272f-or-eos-4271f)
- [Parse the JSON response](#parse-the-json-response)
  - [Install `JQ`](#install-jq)
  - [Parse the response to see only the devices hostname](#parse-the-response-to-see-only-the-devices-hostname)
  
# Get inventory of all devices

```bash
curl -k -X GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.168.0.5/api/resources/inventory/v1/Device/all'
```

# Get one device using it's serial number

Get one device using it's serial number in a query in the URL**

```bash
curl -k -X GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.168.0.5/api/resources/inventory/v1/Device?key.deviceId=leaf1'
```

# Filter the request

Use `partialEqFilter` in a POST body to filter the request  

## Get active tags

```bash
curl -k -X POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.168.0.5/api/resources/tag/v2/Tag/all' -d '{"partialEqFilter": [{"key":{"workspace_id":""}}]}'
```

## Get all device tags

```bash
curl -k -X POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.168.0.5/api/resources/tag/v2/Tag/all' -d '{"partialEqFilter": [{"key":{"workspaceId":"","elementType":"ELEMENT_TYPE_DEVICE"}}]}'
```

## Get all interface tags

```bash
curl -k -X POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.168.0.5/api/resources/tag/v2/Tag/all' -d '{"partialEqFilter": [{"key":{"workspaceId":"","elementType":"ELEMENT_TYPE_INTERFACE"}}]}'
```

## Get inventory of all devices running EOS 4.27.2F

```bash
curl -k -X POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.168.0.5/api/resources/inventory/v1/Device/all' -d '{"partialEqFilter": [{"softwareVersion":"4.27.2F"}]}'
```

## Get all devices running EOS 4.27.2F and with an active streaming status

```bash
curl -k -X POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.168.0.5/api/resources/inventory/v1/Device/all' -d '{"partialEqFilter": [{"softwareVersion":"4.27.2F","streamingStatus":"STREAMING_STATUS_ACTIVE"}]}'
```

## Get all devices running EOS 4.27.2F or EOS 4.27.1F

```bash
curl -k -X POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.168.0.5/api/resources/inventory/v1/Device/all' -d '{"partialEqFilter": [{"softwareVersion":"4.27.2F"},{"softwareVersion":"4.27.1F"}]}'
```

# Parse the JSON response

Parse the JSON response in bash using `JQ`

## Install `JQ`

```bash
sudo apt-get install -y jq
```

## Parse the response to see only the devices hostname

```bash
curl -s -k -X GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.168.0.5/api/resources/inventory/v1/Device/all' | jq '.result.value.hostname'
```
