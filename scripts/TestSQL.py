import os
import csv
import cx_Oracle
import PropertiesReader
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

# Create my_type python objects
my_list = [TY_ALS_REQ('Abhishek','Kumar','Negi','Plot1','Udyog Vihar','Anath Street','Phase IV','','Haryana','','122016','DL1234','1992-12-07','','','98101234567')]
          
#emp1 = TY_ALS_REQ('Abhishek','Kumar','Negi','Plot#1','Udyog Vihar','Anath Street','Phase IV','','Haryana','','122016','DL1234','1992-12-07','','','98101234567')



try:
        db = cx_Oracle.connect(getCARAConnectionURL())
        cursor = db.cursor()
        
        #r = cursor.execute("select * from cara_schema1.CARA_PLR_DATA")
        #for row in cursor:
                #print row
        
        #in_param='MARIA AKRAS'
        #out_param=cursor.var(cx_Oracle.STRING)
        #args0=(in_param,out_param)
        #cursor.callproc('CARA_SCHEMA1.get_als_match_info_copy',args0)
        #print out_param.getvalue.__self__

        #Input parameter - array of String
        
        in_search_array=cursor.arrayvar(cx_Oracle.STRING,['Abhishek','','','','','','','','','','','','1992-12-07','','',''])

        #Output Parameters
        out_status_code=cursor.var(cx_Oracle.NUMBER)
        out_status_msg=cursor.var(cx_Oracle.STRING)
        out_ref_num=cursor.var(cx_Oracle.STRING)
        
        #Arguments for GET_ALS_MATCH_INFO procedure
        #proc_arguments=(emp1,out_status_code,out_status_msg,out_ref_num)

        #Print the input parameter and the procedure argumenta
        #print in_search_array
        #print proc_arguments
        
        #cursor.callproc('CARA_SCHEMA1.PKG_CARA_APPS.GET_ALS_MATCH_INFO',proc_arguments)

        # Run CARA_SCHEMA1.PKG_CARA_APPS.GET_ALS_MATCH_INFO over my_list
        cursor.execute("""
                declare
                        l_params TY_ALS_REQ_TAB;
                        op1 number;
                        type varchar_list is table of varchar2(255) index by binary_integer;
                        l_first_name varchar_list := :p_first_name;
                        l_middle_name varchar_list := :p_middle_name;
                        l_last_name varchar_list := :p_last_name;
                        l_prop_name varchar_list := :p_prop_name;
                        l_unit_number varchar_list := :p_unit_number;
                        l_street_number varchar_list := :p_street_number;
                        l_street_name varchar_list := :p_street_name;
                        l_apt varchar_list := :p_apt;
                        l_city varchar_list := :p_city;
                        l_state varchar_list := :p_state;
                        l_post_code varchar_list := :p_post_code;
                        l_d_license varchar_list := :p_d_license;
                        l_dob varchar_list := :p_dob;
                        l_abn varchar_list := :p_abn;
                        l_acn varchar_list := :p_acn;
                        l_phone varchar_list := :p_phone;
                        op2 varchar_list;
                        op3 varchar_list;
                begin
                        l_params.extend(l_first_name.count);
                        for i in 1..l_first_name.count loop
                                l_params(i) := TY_ALS_REQ(l_first_name(i),l_middle_name(i),l_last_name(i),l_prop_name(i),l_unit_number(i),l_street_number(i),l_street_name(i),l_apt(i),l_city(i),l_state(i) ,l_post_code(i),l_d_license(i),l_dob(i),l_abn(i),l_acn(i),l_phone(i));
                        --l_params := TY_ALS_REQ(l_first_name,l_middle_name,l_last_name,l_prop_name,l_unit_number,l_street_number,l_street_name,l_apt,l_city,l_state ,l_post_code,l_d_license,l_dob,l_abn,l_acn,l_phone);
                        end loop;
                        CARA_SCHEMA1.PKG_CARA_APPS.GET_ALS_MATCH_INFO(l_params,op1,op2,op3);
                end;""",
                p_first_name=[item.first_name for item in my_list],
                p_middle_name=[item.middle_name for item in my_list],
                p_last_name=[item.last_name for item in my_list],
                p_prop_name=[item.prop_name for item in my_list],
                p_unit_number=[item.unit_number for item in my_list],
                p_street_number=[item.street_number for item in my_list],
                p_street_name=[item.street_name for item in my_list],
                p_apt=[item.apt for item in my_list],
                p_city=[item.city for item in my_list],
                p_state=[item.state for item in my_list],
                p_post_code=[item.post_code for item in my_list],
                p_d_license=[item.d_license for item in my_list],
                p_dob=[item.dob for item in my_list],
                p_abn=[item.abn for item in my_list],
                p_acn=[item.acn for item in my_list],
                p_phone=[item.phone for item in my_list],
        )

        print 'Executed the procedure and now printing the output'
        print status_code.getValue.__self__
        print status_msg.getValue.__self__
        print ref_num.getValue.__self__
        

except cx_Oracle.DatabaseError as e:
        print 'Exception Occured'
        print(e)
 
finally:
        cursor.close()
        db.close()
