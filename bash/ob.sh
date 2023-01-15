#!/bin/bash

if [[ -z "${OB_HOST}" ]]; then
  host_name="localhost"
else
  host_name=${OB_HOST}
fi
curl --get --data-urlencode "$1" -v http://$host_name:40074/api/v1 2>/dev/null
