import pandas as pd
import numpy as np
import shutil
import os
import glob
import oracledb
from datetime import datetime

source_dir = 'C:\\Users\\rajesh.mishra\\Downloads\\EBB\\'
target_dir = 'C:\\Users\\rajesh.mishra\\Downloads\\EBB\\Processed\\'


file_names = os.listdir(source_dir)
    
for file_name in glob.glob(source_dir+'*.xlsx'):
    print(file_name)
    if file_name.__contains__('ICOMS'):
        print("inside if")
        dfICOMS = pd.read_excel(file_name, index_col=None, na_values=['NA'], usecols = "B,G")
        #print(dfICOMS)
    elif file_name.__contains__('CSG'):
        print("inside elf")
        dfCSG = pd.read_excel(file_name, index_col=None, na_values=['NA'], usecols = "B,E")
        #print(dfCSG)
    else:
        print("No ICOMS or CSG File Found")

try:
    db = oracledb.connect(user='fms_schema1', password='fms_schema1', dsn='ora-uat101.corp.chartercom.com:1521/infgx01s_svc.corp.chartercom.com')
    cursor = db.cursor()
    icoms_data=[]
    for index,icoms_row in dfICOMS.iterrows():
        icoms_biller=icoms_row['BILLER']
        icoms_acct_no=icoms_row['ACCT']
        sqlquery="insert into CHTR_EBB_RPT(BILLER,ACCOUNT_NO,INSERT_DT) values(:1,:2,:3)"
        icoms_data=icoms_data+[(icoms_biller,icoms_acct_no,datetime.now())]
    cursor.executemany(sqlquery,icoms_data)
    print(cursor.rowcount, "Rows Inserted")
    db.commit()

except oracledb.DatabaseError as e:
        print ('Exception Occured while inserting ICOMS EBB data')
        print(e)
 
finally:
        cursor.close()
        db.close()


try:
    db = oracledb.connect(user='fms_schema1', password='fms_schema1', dsn='ora-uat101.corp.chartercom.com:1521/infgx01s_svc.corp.chartercom.com')
    cursor = db.cursor()
    csg_data=[]
    for index,icoms_row in dfCSG.iterrows():
        csg_biller=icoms_row['BILLER']
        csg_acct_no=icoms_row['SUB_ACCT_NO_SBB']
        sqlquery="insert into CHTR_EBB_RPT(BILLER,ACCOUNT_NO,INSERT_DT) values(:1,:2,:3)"
        csg_data=csg_data+[(csg_biller,csg_acct_no,datetime.now())]
    cursor.executemany(sqlquery,csg_data)
    print(cursor.rowcount, "Rows Inserted")
    db.commit()

except oracledb.DatabaseError as e:
        print ('Exception Occured while inserting CSG EBB data')
        print(e)
 
finally:
        cursor.close()
        db.close()


move_file_names = os.listdir(source_dir)
for file_name_to_move in move_file_names:
    shutil.move(os.path.join(source_dir, file_name_to_move), target_dir)
