from dateutil import parser
import datetime

dt1 = parser.parse("15-04-2019 06:05:00")
dt2 = parser.parse("15-04-2019 06:10:15")
print(dt2-dt1)

dt3 = datetime.datetime.strptime('15-04-2019 06:05:00', '%d-%m-%Y %H:%M:%S')
dt4 = datetime.datetime.strptime('15-04-2019 06:10:15', '%d-%m-%Y %H:%M:%S')
_delta = (dt4-dt3).seconds

print(_delta)

str1 = "919810861681"
str2=str1[0:2]
str3=str1[0:3]
str4=str1[0:4]
l1 = [str2, str3, str4];
print(l1)

