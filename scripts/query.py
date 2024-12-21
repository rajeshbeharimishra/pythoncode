import cx_Oracle
con = cx_Oracle.connect('fms_schema1/fms_schema1@192.168.4.68/orcl')
cur = con.cursor()
cur.execute('select * from bpr_active_rules')
for result in cur:
    print result
cur.close()
con.close()