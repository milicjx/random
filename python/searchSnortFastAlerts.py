import os
import sys
import subprocess

# check arguments
if len(sys.argv) < 2:
	print "Usage: search.py [<fast log file>]"
	sys.exit()

# assign argument to variable
f = sys.argv[1] # log name

for line in open(f):
	d = line.split(",")[0]
	tH = line.split(",")[1]
	tHH = int(tH) + 5
	tM = line.split(",")[2]
	tS = line.split(",")[3]
	#p = line.split(",")[X] # protocol
	#sIP = line.split(",")[X] # source IP
	dIP = line.split(",")[4]
	#print d + " " + t + " " + dIP

	#create a search pattern (fast logs only)
	#grep '03/10-00:48:04.*{TCP} 172.16.114.50.*-> 172.16.112.50' alert

	pattern = d + "-" + str(tHH) + ":" + tM + ".*-> " + dIP + ":"
	print pattern

	#subprocess.call(["ls", "-l", "/var/log/snort/logs_fast/alert"])

	command = ['grep']
	#command.append('-A 2') # return 2 lines above match pattern (non-fast logs only)
	#command.append('-B 3') # return 3 lines below matching pattern (non-fast logs only)
	#command.append('03/09.*-> 172.16.114.50')
	command.append(pattern)
	command.append('alert')

	process = subprocess.Popen(command,stdout=subprocess.PIPE)
	(out,err) = process.communicate()

	print out
