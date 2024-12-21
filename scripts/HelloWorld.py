# Hello world python program
import csv
with open('C:\\Users\\rbmishra\\Desktop\\sample_data\\sample_data.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
print "Hello World!";