#!/bin/bash

# to get this to work, you need to export OB_HOST=192.168.50.114 or whatever your IP address in quest device is (process is documented in the README).

if [[ -z "${OB_HOST}" ]]; then
  host_name="localhost"
else
  host_name=${OB_HOST}
fi
curl --get --data-urlencode "$1"  http://$host_name:40074/api/v1
