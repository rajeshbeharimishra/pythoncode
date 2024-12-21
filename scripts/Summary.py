#!/usr/bin/env python
import os
import xlsxwriter
rowdata = []
abn=''
entity_name=''
entity_type=''
abn_status=''
gst=''
main_business_location=''


# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('ABN_Property2.xlsx')
worksheet = workbook.add_worksheet('ABN-Property')

bold = workbook.add_format({'bold': True})
yellow = workbook.add_format({'bold': True, 'bg_color': '#DAA520'})
blue = workbook.add_format({'bold': True, 'bg_color': '#0000FF'})
green = workbook.add_format({'bold': True, 'bg_color': '#00FF2B'})
red = workbook.add_format({'bold': True, 'bg_color': 'red'})

worksheet.write('A1', 'Attributes', yellow)
worksheet.write('B1', 'Order Info', yellow)
worksheet.write('C1', 'ABN', blue)
worksheet.write('D1', 'Vacant Property- Buy', green)
worksheet.write('E1', 'Vacant Property- Rent', red)

worksheet.write('A2', 'Case Number', bold)
worksheet.write('A3','CAN',bold)
worksheet.write('A4','BAN',bold)
worksheet.write('A5','Customer Name',bold)
worksheet.write('A6','Billing Name',bold)
worksheet.write('A7','ABN',bold)
worksheet.write('A8','Entity Name',bold)
worksheet.write('A9','Entity Type',bold)
worksheet.write('A10','ABN Status',bold)
worksheet.write('A11','Goods & Services Tax (GST):',bold)
worksheet.write('A12','Main Business Location',bold)
worksheet.write('A13','Billing Address',bold)
worksheet.write('A14','Service Address',bold)


# Start from the first cell below the headers.
row = 1
col = 2

file_list=""
rowdata_files = []
rowdata_files.extend(os.listdir("C:\\Users\\rbmishra\\Desktop\\sample_data\\"))
print len(rowdata)
for k, name in enumerate(rowdata):
	#print "{name}".format(iteration=k, name=name)
	file_list = str(rowdata[k])
	print file_list

with open('3604403_ABN.txt') as fp:
    for line in fp:
		rowdata.append(line)
print len(rowdata)
for k, name in enumerate(rowdata):
	#print "{name}".format(iteration=k, name=name)
	if len(rowdata)>6:
		abn=rowdata[0].strip(' \t\n\r\n')
		entity_name=rowdata[1].strip(' \t\n\r\n')
		abn_status=rowdata[2].strip(' \t\n\r\n')
		entity_type=rowdata[3].strip(' \t\n\r\n')
		gst=rowdata[4].strip(' \t\n\r\n')
		main_business_location=rowdata[6].strip(' \t\n\r\n')
	else:
		print "No data found"

worksheet.write('C7', ''.join(abn.split("Details for ABN:")))
worksheet.write('C8', ''.join(entity_name.split("Entity name:")).strip(' \t\n\r\n'))
worksheet.write('C9', ''.join(entity_type.split("Entity type:")).strip(' \t\n\r\n'))
worksheet.write('C10', ''.join(abn_status.split("ABN status:")).strip(' \t\n\r\n'))
worksheet.write('C11', ''.join(gst.split("Goods & Services Tax (GST):")).strip(' \t\n\r\n'))
worksheet.write('C12', ''.join(main_business_location.split("Main business location:")).strip(' \t\n\r\n'))