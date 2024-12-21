import os
data=''
try:
	with open('D:\\FPDS-BOT\\OUTPUT\\3604396_MICA.txt') as fp:
		title=fp.next()       # strip title line
		data=''.join(line.rstrip() for line in fp)
		print data
except IOError:
	print "Error: MICA Output File does not appear to exist."