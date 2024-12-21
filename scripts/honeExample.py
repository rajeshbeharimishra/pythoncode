#!/usr/bin/python

import sys
import hone

Hone = hone.Hone()
schema = Hone.get_schema('D:\\Training\\Python\\Govern-LA-Data-Assets.csv.csv')   # returns nested JSON schema for input.csv
result = Hone.convert('D:\\Training\\Python\\Govern-LA-Data-Assets.csv.csv')     # returns converted JSON as Python dictionary
print(result)
