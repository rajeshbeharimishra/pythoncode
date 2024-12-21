#import glob
import os
#result = glob.glob("C:\\Users\\rbmishra\\Desktop\\sample_data\\*.csv")
#print len(os.listdir("C:\\Users\\rbmishra\\Desktop\\sample_data\\"))
#print result
#print os.listdir("C:\\Users\\rbmishra\\Desktop\\sample_data\\")
file_list=""
rowdata = []
rowdata.extend(os.listdir("C:\\Users\\rbmishra\\Desktop\\sample_data\\"))
print len(rowdata)
for k, name in enumerate(rowdata):
	#print "{name}".format(iteration=k, name=name)
	file_list = str(rowdata[k])
	print file_list