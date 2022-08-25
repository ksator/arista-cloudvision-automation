**Table of contents**

- [Get the inventory](#get-the-inventory)
  - [Getting the token from a local file](#getting-the-token-from-a-local-file)
  - [Getting the token from an environment variable](#getting-the-token-from-an-environment-variable)

# Get the inventory

## Getting the token from a local file

```bash
wget --no-check-certificate --quiet --method GET --output-document=inventory --header='Accept: application/json' --header="Authorization: Bearer `cat token.tok`" 'https://192.168.0.5/cvpservice/inventory/devices'
```

Check the result

```bash
more inventory
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

Get the inventory

```bash
wget --no-check-certificate --quiet --method GET --output-document=inventory --header='Accept: application/json' --header="Authorization: Bearer $token" 'https://192.168.0.5/cvpservice/inventory/devices'
```

Check the result

```bash
more inventory
```
