import pandas as pd

data = pd.read_csv("splitter_test.csv", header=None)
data_category_range = data[0].unique()
data_category_range = data_category_range.tolist()
for i,value in enumerate(data_category_range):
    data[data[0] == value].to_csv('D:/dir'+str(i)+'/splitter_test.csv',index = False, na_rep = 'N/A')
