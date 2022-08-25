Update the following command with your CVP details:

- CVP IP address
- userId
- password

```cli
curl -k -X 'POST' \
  'https://192.168.0.5/cvpservice/login/authenticate.do' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "userId": "arista",
  "password": "aristaj0bg"
}'
```
