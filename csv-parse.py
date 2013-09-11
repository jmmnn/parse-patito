import re
import json
import urllib
from pandas import Series, DataFrame
import pandas as pd

#path to datasource
query_url= 'http://localhost:8888/solr/patito-files/select?q=*%3A*&fl=id%2C+title&wt=csv&indent=true' #change the rows=  to get a large dataset
query_result = urllib.urlopen(query_url)
string_result = query_result.read()
#print string_result

#creating a csv from the html response
f = open('workfile.csv', 'w')
f.write(string_result)

#reading the csv into a dataFrame
my_data_frame = pd.read_csv('workfile.csv')
