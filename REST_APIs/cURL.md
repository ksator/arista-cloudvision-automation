**Table of contents**

- [Get the CVP version](#get-the-cvp-version)
- [Get the CVP inventory](#get-the-cvp-inventory)
  - [Getting the token from a local file](#getting-the-token-from-a-local-file)
  - [Getting the token from an environment variable](#getting-the-token-from-an-environment-variable)
- [Install `jq` to parse JSON in bash](#install-jq-to-parse-json-in-bash)
  - [Filter the output to see only the first device of the inventory](#filter-the-output-to-see-only-the-first-device-of-the-inventory)
  - [Filter the output to see only the hostname of each device of the inventory](#filter-the-output-to-see-only-the-hostname-of-each-device-of-the-inventory)

# Get the CVP version

```bash
curl -k -X GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.168.0.5/cvpservice/cvpInfo/getCvpInfo.do'
```

# Get the CVP inventory

## Getting the token from a local file

```bash
curl -k -X GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.168.0.5/cvpservice/inventory/devices'
```

## Getting the token from an environment variable

Copy the token in an environment variable

```bash
token=xxx
```

Read the environment variable

```bash
echo $token
```

Use the environment variable from cURL

```bash
curl -k -X GET --header 'Accept: application/json' --cookie "access_token=$token" 'https://192.168.0.5/cvpservice/inventory/devices'
```

# Install `jq` to parse JSON in bash

```bash
sudo apt-get install -y jq
```

## Filter the output to see only the first device of the inventory 

```bash
curl -k -s -X GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.168.0.5/cvpservice/inventory/devices' | jq '.[0]'
```

## Filter the output to see only the hostname of each device of the inventory

```bash
curl -k -s -X GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.168.0.5/cvpservice/inventory/devices' | jq '.[].hostname'
```
