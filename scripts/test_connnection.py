import cx_Oracle


con = cx_Oracle.connect('fms_schema1/fms_schema1@192.168.4.107/evt01')
ver = con.version.split(".")
for v in ver:
    print "Testing: "
    if v == "2":
        print v + " is 2"
    else:
        print v + " is not 2"

con.close()
