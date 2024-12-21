#created by Rajesh Mishra on 2-Dec-21

import pandas as pd
import json


#give the path to output json file to read into a dataframe
df = pd.read_json('D:/Training/3.8.1/InputFiles/GraydonOutPutJson/0403772495_companyProfile.json')


#write the dataframe to a csv - give the path to csv where you want to write the data
df.to_csv('D:/Training/Python/0403772495_companyProfile.csv')



