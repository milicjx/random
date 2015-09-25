# go to nessus root dir
cd /Library/Nessus/run/sbin/
# download plugins
./Library/Nessus/run/sbin/nessuscli fetch --plugins
# install plugins
./Library/Nessus/run/sbin/nessuscli update all-2.0.tar.gz
