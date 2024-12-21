abn=''
entity_name=''
entity_type=''
abn_status=''
main_business_location=''

with open('3604396_ABN.txt') as fp:
     for line in fp:
		abn = ''.join(line.split("Details for ABN:")).strip(' \t\n\r\n')
		entity_name = ''.join(line.split("Entity name:")).strip(' \t\n\r\n')
		entity_type = ''.join(line.split("Entity type:")).strip(' \t\n\r\n')
		abn_status = ''.join(line.split("ABN status:")).strip(' \t\n\r\n')
		main_business_location = ''.join(line.split("Main business location:")).strip(' \t\n\r\n')
		print abn
		print entity_name
		print entity_type
		print abn_status
		print main_business_location