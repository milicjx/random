#########################################################
# work in progress!
# 
# program searches for Snort alerts based on 
# timestamp, source IP address, destination IP address 
# and protocol
#
#########################################################

import os
import sys
import subprocess

# check arguments
if len(sys.argv) < 4:
	print "Usage: search [timestamp] [source IP] [destination IP] [protocol]"
	sys.exit()

# assign arguments to variables
tstamp = sys.argv[1]
srcIP = sys.argv[2]
desIP = sys.argv[3]
pro = sys.argv[4]

# create a search pattern

p = tstamp + ".*-> " + desIP

command = ['grep']
command.append('-A 2') # return 2 lines above match pattern
command.append('-B 3') # return 3 lines below matching pattern
#command.append('03/09.*-> 172.16.114.50')
command.append(p)
command.append('alert') # log file name in pwd

process = subprocess.Popen(command,stdout=subprocess.PIPE)
(out,err) = process.communicate()

print out
