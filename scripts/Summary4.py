#################################################
#	Author: Rajesh Behari Mishra				#
#	Purpose: Read the output files from ABN,	#
#	Vacant Property Search and MICA and			# 
#	combine them to createa excel output		#
#	Created : 17-NOv-16							#
#	Modified: 20-Nov-16 to add the rental code	#
#################################################

#!/usr/bin/env python
import os
import csv
import xlsxwriter


# Varibale declarations
rowdata = []
rowdata_VPB=[]
rowdata_VPR=[]
rowdata_MICA=[]
abn=''
entity_name=''
entity_type=''
abn_status=''
gst=''
main_business_location=''
case_number=''
cust_acct_no=''
bill_acct_no=''
cust_name=''
bill_name=''
cust_address=''
bill_address=''
service_address=''
cust_addr_result=''
bill_addr_result=''
serv_addr_result=''
acct_create_dt=''
order_id=''
order_type=''
dob=''
cust_phone=''
cust_mphone=''
email_id=''
driving_lic=''
employer=''
employer_phoneno=''

#MICA output variables
custname_mica=''
dob_mica=''
abn_mica=''
tradename_mica=''
dl_mica=''
idproof_mica=''
idnumber_mica=''
employer_mica=''
employer_phone_mica=''
notes_mica=''




# Now a new dialect called mydialect is created
csv.register_dialect(
    'mydialect',
    delimiter = '|',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)

file_list=""
rowdata_files = []
rowdata_files.extend(os.listdir("C:\\Users\\rbmishra\\Desktop\\sample_data\\"))
print len(rowdata_files)
for k, name in enumerate(rowdata_files):
	#print "{name}".format(iteration=k, name=name)
	file_list = str(rowdata_files[k])
	#print file_list
	if file_list!='':
		# Read the order and case related data from input file.
		with open('C:\\Users\\rbmishra\\Desktop\\sample_data\\'+file_list, 'rb') as mycsvfile:
			thedata = csv.reader(mycsvfile, dialect='mydialect')
			for row in thedata:
				case_number=row[7]
				cust_acct_no=row[10]
				bill_acct_no=row[11]
				cust_name=row[0]+' '+row[1]
				bill_name=row[30]
				cust_address=row[3]
				bill_address=row[31]
				service_address=row[32]
				acct_create_dt=row[18]
				order_id=row[15]
				order_type=row[18]
				dob=row[2]
				cust_phone=row[22]
				cust_mphone=row[21]
				email_id=row[4]
				driving_lic=row[24]
				employer=row[25]
				employer_phoneno=row[26]

				# Create excel workbook and add a worksheet and write the results into it.
				workbook = xlsxwriter.Workbook('D:\\FPDS-BOT\\SUMMARY\\'+case_number+'_Summary.xlsx')
				worksheet = workbook.add_worksheet('ABN-Property')
				worksheet1 = workbook.add_worksheet('MICA')

				# Declare the excel formatting attributes
				bold = workbook.add_format({'bold': True})
				yellow = workbook.add_format({'bold': True, 'bg_color': '#DAA520'})
				blue = workbook.add_format({'bold': True, 'bg_color': '#0000FF'})
				green = workbook.add_format({'bold': True, 'bg_color': '#00FF2B'})
				red = workbook.add_format({'bold': True, 'bg_color': 'red'})

				# Define the top row headers for ABN-Property worksheet
				worksheet.write('A1', 'Attributes', yellow)
				worksheet.write('B1', 'Order Info', yellow)
				worksheet.write('C1', 'ABN', blue)
				worksheet.write('D1', 'Vacant Property- Buy', green)
				worksheet.write('E1', 'Vacant Property- Rent', red)

				# Define the first column for ABN-Property worksheet
				worksheet.write('A2', 'Case Number', bold)
				worksheet.write('A3','CAN',bold)
				worksheet.write('A4','BAN',bold)
				worksheet.write('A5','Customer Name',bold)
				worksheet.write('A6','Billing Name',bold)
				worksheet.write('A7','ABN',bold)
				worksheet.write('A8','Entity Name',bold)
				worksheet.write('A9','Entity Type',bold)
				worksheet.write('A10','ABN Status',bold)
				worksheet.write('A11','Goods & Services Tax (GST)',bold)
				worksheet.write('A12','Main Business Location',bold)
				worksheet.write('A13','Customer Address',bold)
				worksheet.write('A14','Billing Address',bold)
				worksheet.write('A15','Service Address',bold)

				# Define the top row headers for MICA worksheet
				worksheet1.write('A1', 'Screen Name', yellow)
				worksheet1.write('B1', 'Attributes', yellow)
				worksheet1.write('C1', 'Order Info', yellow)
				worksheet1.write('D1', 'Name & DOB 1', blue)
				worksheet1.write('E1', 'Name & DOB 2', blue)
				worksheet1.write('F1', 'Name & DOB 3', blue)
				worksheet1.write('G1', 'Contact 1', green)
				worksheet1.write('H1', 'Contact 2', green)
				worksheet1.write('I1', 'Contact 3', green)

				# Define the first and second columns for MICA worksheet
				worksheet1.write('A4', 'SERV')
				worksheet1.write('A5', 'SERV')
				worksheet1.write('A6', 'ACCT')
				worksheet1.write('A7', 'SERV')
				worksheet1.write('A8', 'ICAI')
				worksheet1.write('A11', 'PERS')
				worksheet1.write('A12', 'ACCT')
				worksheet1.write('A13', 'PERS')
				worksheet1.write('A14', 'SERV')
				worksheet1.write('A15', 'SERV')
				worksheet1.write('A16', 'NOTE')
				worksheet1.write('A17', 'PERC')
				worksheet1.write('A18', 'PERS')
				worksheet1.write('A19', 'ACCT')
				worksheet1.write('A20', 'ACCT')
				worksheet1.write('A21', 'ACCT')
				worksheet1.write('A22', 'PERS')
				worksheet1.write('A23', 'ACCT')
				worksheet1.write('A24', 'SERV')
				worksheet1.write('A25', 'PERC')
				worksheet1.write('A26', 'PERC')
				worksheet1.write('A27', 'PERC')
				worksheet1.write('A28', 'PERC')
				worksheet1.write('A29', 'NOTE')

				worksheet1.write('B2', 'Case Number', bold)
				worksheet1.write('B3', 'CAN', bold)
				worksheet1.write('B4','BAN',bold)
				worksheet1.write('B5','Account Create Date',bold)
				worksheet1.write('B6','Account Status',bold)
				worksheet1.write('B7','Account Balance',bold)
				worksheet1.write('B8','Bankrupt/Insolvent',bold)
				worksheet1.write('B9','Order ID',bold)
				worksheet1.write('B10','Order Type',bold)
				worksheet1.write('B11','Customer Name',bold)
				worksheet1.write('B12','Billing Name',bold)
				worksheet1.write('B13','DOB',bold)
				worksheet1.write('B14','Customer Phone',bold)
				worksheet1.write('B15','Customer Mphone',bold)
				worksheet1.write('B16','Email address',bold)
				worksheet1.write('B17','DL',bold)
				worksheet1.write('B18','ABN',bold)
				worksheet1.write('B19','Customer Address',bold)
				worksheet1.write('B20','Billing Address',bold)
				worksheet1.write('B21','Service Address',bold)
				worksheet1.write('B22','Trade Name',bold)
				worksheet1.write('B23','Status',bold)
				worksheet1.write('B24','Xfer from/to Acct Nr',bold)
				worksheet1.write('B25','Proof of Id',bold)
				worksheet1.write('B26','ID Number',bold)
				worksheet1.write('B27','Employer',bold)
				worksheet1.write('B28','Employer Phone Number',bold)
				worksheet1.write('B29','NOTES',bold)
				
				# Write the data from order info for ABN-Property worksheet
				worksheet.write('B2', case_number.strip(' \t\n\r\n'))
				worksheet.write('B3', cust_acct_no.strip(' \t\n\r\n'))
				worksheet.write('B4', bill_acct_no.strip(' \t\n\r\n'))
				worksheet.write('B5', cust_name.strip(' \t\n\r\n'))
				worksheet.write('B6', bill_name.strip(' \t\n\r\n'))
				worksheet.write('B13', cust_address.strip(' \t\n\r\n'))
				worksheet.write('B14', bill_address.strip(' \t\n\r\n'))
				worksheet.write('B15', service_address.strip(' \t\n\r\n'))

				# Write the data from order info for MICA worksheet
				worksheet1.write('C2', case_number.strip(' \t\n\r\n'))
				worksheet1.write('C3', cust_acct_no.strip(' \t\n\r\n'))
				worksheet1.write('C4', bill_acct_no.strip(' \t\n\r\n'))
				worksheet1.write('C5', acct_create_dt.strip(' \t\n\r\n'))
				worksheet1.write('C9', order_id.strip(' \t\n\r\n'))
				worksheet1.write('C10', order_type.strip(' \t\n\r\n'))
				worksheet1.write('C11', cust_name.strip(' \t\n\r\n'))
				worksheet1.write('C12', bill_name.strip(' \t\n\r\n'))
				worksheet1.write('C13', dob.strip(' \t\n\r\n'))
				worksheet1.write('C14', cust_phone.strip(' \t\n\r\n'))
				worksheet1.write('C15', cust_mphone.strip(' \t\n\r\n'))
				worksheet1.write('C16', email_id.strip(' \t\n\r\n'))
				worksheet1.write('C17', driving_lic.strip(' \t\n\r\n'))
				worksheet1.write('C18', abn.strip(' \t\n\r\n'))
				worksheet1.write('C19', cust_address.strip(' \t\n\r\n'))
				worksheet1.write('C20', bill_acct_no.strip(' \t\n\r\n'))
				worksheet1.write('C21', service_address.strip(' \t\n\r\n'))
				worksheet1.write('C26', employer.strip(' \t\n\r\n'))
				worksheet1.write('C27', employer_phoneno.strip(' \t\n\r\n'))


				print 'D:\\FPDS-BOT\\OUTPUT\\'+case_number+'_ABN.txt'
				try:
					with open('D:\\FPDS-BOT\\OUTPUT\\'+case_number+'_ABN.txt') as fp:
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
						
						# Write the data from search results
						worksheet.write('C7', ''.join(abn.split("Details for ABN:")))
						worksheet.write('C8', ''.join(entity_name.split("Entity name:")).strip(' \t\n\r\n'))
						worksheet.write('C9', ''.join(entity_type.split("Entity type:")).strip(' \t\n\r\n'))
						worksheet.write('C10', ''.join(abn_status.split("ABN status:")).strip(' \t\n\r\n'))
						worksheet.write('C11', ''.join(gst.split("Goods & Services Tax (GST):")).strip(' \t\n\r\n'))
						worksheet.write('C12', ''.join(main_business_location.split("Main business location:")).strip(' \t\n\r\n'))
						rowdata[:] = []
				except IOError:
					print "Error: ABN Output File does not appear to exist."

				print 'D:\\FPDS-BOT\\OUTPUT\\'+case_number+'_VPB.txt'
				try:
					with open('D:\\FPDS-BOT\\OUTPUT\\'+case_number+'_VPB.txt') as fp:
						for line in fp:
							rowdata_VPB.append(line)
						print len(rowdata_VPB)
						for k, name in enumerate(rowdata_VPB):
							#print "{name}".format(iteration=k, name=name)
							if len(rowdata_VPB)>=3:
								cust_addr_result=rowdata_VPB[0].strip(' \t\n\r\n')
								bill_addr_result=rowdata_VPB[1].strip(' \t\n\r\n')
								serv_addr_result=rowdata_VPB[2].strip(' \t\n\r\n')
							else:
								print "No data found"
						
						# Write the data from search results
						worksheet.write('D13', ''.join(cust_addr_result.split("CUST_ADDR:")).strip(' \t\n\r\n'))
						worksheet.write('D14', ''.join(bill_addr_result.split("BILL_ADDR:")).strip(' \t\n\r\n'))
						worksheet.write('D15', ''.join(serv_addr_result.split("SERV_ADDR:")).strip(' \t\n\r\n'))
						rowdata_VPB[:] = []
				except IOError:
					print "Error: Vacant Property Buy Output File does not appear to exist."

				print 'D:\\FPDS-BOT\\OUTPUT\\'+case_number+'_VPR.txt'
				try:
					with open('D:\\FPDS-BOT\\OUTPUT\\'+case_number+'_VPR.txt') as fp:
						for line in fp:
							rowdata_VPR.append(line)
						print len(rowdata_VPR)
						for k, name in enumerate(rowdata_VPR):
							#print "{name}".format(iteration=k, name=name)
							if len(rowdata_VPR)>=3:
								cust_addr_result=rowdata_VPR[0].strip(' \t\n\r\n')
								bill_addr_result=rowdata_VPR[1].strip(' \t\n\r\n')
								serv_addr_result=rowdata_VPR[2].strip(' \t\n\r\n')
							else:
								print "No data found"
						
						# Write the data from search results
						worksheet.write('E13', ''.join(cust_addr_result.split("CUST_ADDR:")).strip(' \t\n\r\n'))
						worksheet.write('E14', ''.join(bill_addr_result.split("BILL_ADDR:")).strip(' \t\n\r\n'))
						worksheet.write('E15', ''.join(serv_addr_result.split("SERV_ADDR:")).strip(' \t\n\r\n'))
						rowdata_VPR[:] = []
				except IOError:
					print "Error: Vacant Property Rent Output File does not appear to exist."

				print 'D:\\FPDS-BOT\\OUTPUT\\'+case_number+'_MICA.txt'
				try:
					with open('D:\\FPDS-BOT\\OUTPUT\\'+case_number+'_MICA.txt') as fp:
						for line in fp:
							rowdata_MICA.append(line)
						print len(rowdata_MICA)
						for k, name in enumerate(rowdata_MICA):
							#print "{name}".format(iteration=k, name=name)
							if len(rowdata_MICA)>=15:
								custname_mica=rowdata_MICA[0].strip(' \t\n\r\n')
								dob_mica=rowdata_MICA[1].strip(' \t\n\r\n')
								abn_mica=rowdata_MICA[2].strip(' \t\n\r\n')
								tradename_mica=rowdata_MICA[3].strip(' \t\n\r\n')
								dl_mica=rowdata_MICA[4].strip(' \t\n\r\n')
								idproof_mica=rowdata_MICA[5].strip(' \t\n\r\n')
								idnumber_mica=rowdata_MICA[6].strip(' \t\n\r\n')
								employer_mica=rowdata_MICA[7].strip(' \t\n\r\n')
								employer_phone_mica=rowdata_MICA[8].strip(' \t\n\r\n')
								notes_mica=rowdata_MICA[9].rstrip(' \t\n\r\n')
							else:
								print "No data found"
						
						# Write the data from MICA search results

						worksheet1.write('D11', ''.join(custname_mica.split("PERS:Customer Name:")))
						worksheet1.write('D13', ''.join(dob_mica.split("PERS:DOB:")))
						worksheet1.write('D18', ''.join(abn_mica.split("PERS:ABN:")))
						worksheet1.write('D22', ''.join(tradename_mica.split("PERS:Trade Name:")))
						worksheet1.write('D17', ''.join(dl_mica.split("PERC:DL:")))
						worksheet1.write('D25', ''.join(idproof_mica.split("PERC:Proof of Id:")))
						worksheet1.write('D26', ''.join(idnumber_mica.split("PERC:ID Number:")))
						worksheet1.write('D27', ''.join(employer_mica.split("PERC:Employer:")))
						worksheet1.write('D28', ''.join(employer_phone_mica.split("PERC:Employer's Phone Number:")))
						worksheet1.write('D29', ''.join(notes_mica.split("NOTE:NOTES:")))
						rowdata_MICA[:] = []
				except IOError:
					print "Error: MICA Output File does not appear to exist."