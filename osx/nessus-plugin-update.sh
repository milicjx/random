#!/bin/bash
echo "updating Nessus plugins"
cd /Library/Nessus/run/sbin/
./Library/Nessus/run/sbin/nessuscli fetch --plugins
./Library/Nessus/run/sbin/nessuscli update all-2.0.tar.gz
echo "exiting"
exit 0
