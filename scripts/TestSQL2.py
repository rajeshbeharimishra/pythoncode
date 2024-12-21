import os
import csv
import cx_Oracle
from time import gmtime, strftime

class TY_ALS_REQ:
        def __init__(self,first_name,middle_name,last_name,prop_name,unit_number,street_number	,street_name,apt,city,state,post_code,d_license,dob,abn,acn,phone):
                self.first_name=first_name
                self.middle_name=middle_name
                self.last_name=last_name
                self.prop_name=prop_name
                self.unit_number=unit_number
                self.street_number=street_number
                self.street_name=street_name
                self.apt=apt
                self.city=city	
                self.state=state	
                self.post_code=post_code
                self.d_license=d_license
                self.dob=dob
                self.abn=abn
                self.acn=acn
                self.phone=phone

# Create TY_ALS_REQ python object
emp1 = TY_ALS_REQ('Abhishek','Kumar','Negi','Plot#1','Udyog Vihar','Anath Street','Phase IV','','Haryana','','122016','DL1234','1992-12-07','','','98101234567')



try:
        db = cx_Oracle.connect('cara_schema1/cara_schema1@192.168.4.68:1521/FPDIAV1B')
        cursor = db.cursor()
        
        sql="""
        set serveroutput on
        declare
                lr_als_req ty_als_req := ty_als_req('Abhishek','','','','','','','','','','','','1992-12-07','','','');
                lv_status_cd number;
                lv_status_msg varchar2(2000);
                lv_ref_num varchar2(100 char);
        begin
                pkg_cara_apps.get_als_match_info(pr_als_req => lr_als_req, pv_status_code => lv_status_cd, pv_status_msg => lv_status_msg,pv_ref_num => lv_ref_num);
                dbms_output.put_line(lv_ref_num||':'||lv_status_cd||':'||lv_status_msg);
        end;
        """

        #input parameter
        in_param=cursor.var(cx_Oracle.OBJECT(emp1))
        #Output Parameters
        out_status_code=cursor.var(cx_Oracle.NUMBER)
        out_status_msg=cursor.var(cx_Oracle.STRING)
        out_ref_num=cursor.var(cx_Oracle.STRING)
        
        #Arguments for GET_ALS_MATCH_INFO procedure
        proc_arguments=(in_param,out_status_code,out_status_msg,out_ref_num)
        
        
        # Execute the procedure
        cursor.callproc('CARA_SCHEMA1.PKG_CARA_APPS.GET_ALS_MATCH_INFO',proc_arguments)

      
        print 'Executed the procedure and now printing the output'
        print out_status_code.getvalue.__self__
        print out_status_msg.getvalue.__self__
        print out_ref_num.getvalue.__self__
        

except cx_Oracle.DatabaseError as e:
        print 'Exception Occured'
        print(e)
 
finally:
        cursor.close()
        db.close()
