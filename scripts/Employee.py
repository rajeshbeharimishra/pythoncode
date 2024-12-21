#!/usr/bin/python

class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, first_name,middle_name,last_name,prop_name,unit_number,street_number	,street_name,apt,city	,state	,post_code,d_license,dob,abn,acn,phone):
       self.first_name=first_name
       self.middle_name=middle_name
       self.last_name=last_name

    def displayEmployee(self):
        print "First Name : ", self.first_name,  ", Last Name: ", self.middle_name

emp1 = Employee('Abhishek','Kumar','Negi','','','','','','','','','','1992-12-07','','','')
emp1.displayEmployee()
