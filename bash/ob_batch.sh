#!/bin/bash

if [[ -z "${OB_HOST}" ]]; then
  host_name="localhost"
else
  host_name=${OB_HOST}
fi

echo "OB_HOST=$OB_HOST"

if [ $# -eq 0 ]; then
  echo "provide path to ob_command_capture.txt"
  exit 1
fi

if [ ! -f $1 ]; then
  echo "$1 not found!"
  exit 1
fi

while read p; do
  ob $p
  # break
done <$1
