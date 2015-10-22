#########################################################
# work in progress!
# 
# program parses through Snort fast alerts based on 
# timestamp, source IP address, destination IP address 
# and protocol
#
#########################################################

import os
import sys
import subprocess

# check arguments
if len(sys.argv) < 3:
	print "Usage: search.py [<fast log file>] [<Snort alert file>]"
	sys.exit()

# assign argument to variable
f = sys.argv[1] # ground truth file name
a = sys.argv[2] # log alert file name

# show count of all Snort alerts
command = ['wc']
command.append('-l')
command.append(a)
process = subprocess.Popen(command,stdout=subprocess.PIPE)
(out,err) = process.communicate()
print "The total number of alerts in " + a + " file is: " + out
print "******************************\n"

for line in open(f):

	# parse through attributes
	d = line.split(",")[0]
	tH = line.split(",")[1]
	tHH = int(tH) + 5
	tM = line.split(",")[2]
	tS = line.split(",")[3]
	#p = line.split(",")[X] # protocol (for future use)
	#sIP = line.split(",")[X] # source IP (for future use)
	dIP = line.split(",")[4]
	sysN = line.split(",")[5] # system name
	attack = line.split(",")[6] # attack name
	att = attack.strip("\n")
	#p = line.split(",")[X] # protocol (for future use)
        #sIP = line.split(",")[X] # source IP (for future use)

	#create a search pattern (fast logs only)
	pattern = d + "-" + str(tHH) + ":" + tM + ".*-> " + dIP + ":"
	
	print "Looking for " + att + " attack on " + sysN + " system."
	print "Date:\t\t" + d
	print "Time:\t\t" + str(tHH) + ":" + tM + ":" + tS
	print "Destination IP:\t" + dIP
	print "The total number of true positive alerts is:"

	#subprocess.call(["ls", "-l", "/var/log/snort/logs_fast/alert"])

	command = ['grep']
	command.append('-c') # count alerts/ remove for full alert output
	#command.append('-A 2') # return 2 lines above match pattern (non-fast logs only)
	#command.append('-B 3') # return 3 lines below matching pattern (non-fast logs only)
	#command.append('03/09.*-> 172.16.114.50') # manual pattern input example
	command.append(pattern)
	command.append(a)

	process = subprocess.Popen(command,stdout=subprocess.PIPE)
	(out,err) = process.communicate()

	print out
	print "******************************\n"
