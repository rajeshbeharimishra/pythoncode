#!/usr/bin/python

from json import dumps, loads, JSONEncoder, JSONDecoder
import pickle
import sys, getopt
import csv
import pandas as pd



class PythonObjectEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (list, dict, str, unicode, int, float, bool, type(None))):
            return JSONEncoder.default(self, obj)
        return {'_python_object': pickle.dumps(obj)}

df = pd.read_csv('Govern-LA-Data-Assets-2.csv')

def get_nested_rec(key, grp):
    rec = {}
    rec['TypeID'] = key[0]
    rec['Type'] = key[1]
##    rec['Name'] = key[2]
##    rec['ID'] = key[3]
##    rec['AssetID'] = key[4]

    for field in ['TypeID','Type']:
        rec[field] = list(grp[field].unique())

    return rec

records = []
##for key, grp in df.groupby(['Type','TypeID','Name',"ID",'AssetID']):
for key, grp in df.groupby(['TypeID','Type']):
    rec = get_nested_rec(key, grp)
    records.append(rec)

records = dict(data = records)


with open("json_filenew.json", "w") as f:
    try:
        f.write(dumps(records,cls=PythonObjectEncoder,sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
    except IOError:
        print("Exception Occured" + IOError)
