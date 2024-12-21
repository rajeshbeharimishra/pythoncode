import csv
import os
csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)

print('\n Output from an iterable object created from the csv file')
rowdata = []
case_number=""
		 
with open('C:\\Users\\rbmishra\\Desktop\\sample_data\\11122016_1.csv', 'rb') as mycsvfile:
    thedata = csv.reader(mycsvfile, dialect='mydialect')
    for row in thedata:
        print(row[7])