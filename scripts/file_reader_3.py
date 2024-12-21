#!/usr/bin/env python
import os
import xlsxwriter

abn=''
entity_name=''
entity_type=''
abn_status=''
main_business_location=''
gst=''

rowdata = []

with open('3604396_ABN.txt') as fp:
    for line in fp:
		rowdata.append(line)
print len(rowdata)
for k, name in enumerate(rowdata):
	#print "{name}".format(iteration=k, name=name)
	abn=rowdata[0].strip(' \t\n\r\n')
	entity_name=rowdata[1].strip(' \t\n\r\n')
	abn_status=rowdata[2].strip(' \t\n\r\n')
	entity_type=rowdata[3].strip(' \t\n\r\n')
	gst=rowdata[4].strip(' \t\n\r\n')
	main_business_location=rowdata[6].strip(' \t\n\r\n')

print ''.join(abn.split("Details for ABN:"))	
print ''.join(entity_name.split("Entity name:")).strip(' \t\n\r\n')
print ''.join(entity_type.split("Entity type:")).strip(' \t\n\r\n')
print ''.join(abn_status.split("ABN status:")).strip(' \t\n\r\n')
print ''.join(gst.split("Goods & Services Tax (GST):")).strip(' \t\n\r\n')
print ''.join(main_business_location.split("Main business location:")).strip(' \t\n\r\n')