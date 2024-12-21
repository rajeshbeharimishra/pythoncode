import os
import cx_Oracle
from hashlib import md5

file_list=""
folder = "C:\\Python27\\files"
rowdata = []
rowdata.extend(os.listdir(folder))
con = cx_Oracle.connect('fms_schema1/fms_schema1@192.168.4.107/evt01')
cur = con.cursor()

for k, name in enumerate(rowdata):
    file_list = str(folder+"\\"+rowdata[k])
    file_size = os.path.getsize(file_list)
    with open(file_list,'rb') as f:
        data = f.read()
        blob_md5 = md5(data).hexdigest()
        binary_var = cur.var(cx_Oracle.BLOB)
        binary_var.setvalue(0, data) 
        cur.callproc('prc_bot_case_attachments',[rowdata[k],file_size,binary_var,folder])
        #con.commit()
cur.close()
con.close()
