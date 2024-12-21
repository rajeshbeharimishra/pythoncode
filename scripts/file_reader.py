def create_data_lists():
for symbol in symbols:
	with open(symbol+'.csv', 'r') as f:
		print symbol
        rowdata = []
        reader = csv.reader(f)
        reader.next()
        for row in reader:
			rowdata.append(row)
    data_by_symbol.append(rowdata)