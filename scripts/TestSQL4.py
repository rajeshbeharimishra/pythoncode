import os
import csv
import cx_Oracle
import PropertiesReader
from time import gmtime, strftime

#print PropertiesReader.getCARAConnectionURL()


try:
        db = cx_Oracle.connect(PropertiesReader.getCARAConnectionURL())
        cursor = db.cursor()
        
        r = cursor.execute("select * from cara_schema1.CARA_PLR_DATA")
        for row in cursor:
                print row
        
except cx_Oracle.DatabaseError as e:
        print 'Exception Occured'
        print(e)
 
finally:
        cursor.close()
        db.close()
