pid=$(ps -ef | grep OpenBrush | grep -v grep | awk '{print $2}')
kill -9 $pid