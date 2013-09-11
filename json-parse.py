import re
import json
import urllib
from pandas import Series, DataFrame
import pandas as pd

#path to datasource
# query_url= 'http://localhost:8888/solr/patito-files/select?q=*%3A*&fl=id%2C+title&wt=xml&indent=true' #change the rows=  to get a large dataset
# query_result = urllib.urlopen(query_url)
# string_result = query_result.read()
#print string_result

db = json.load(open('full_string_result.json'))
# print len(db)
print db['response']['docs']

# frame = DataFrame(db)
# print frame

# documents = DataFrame(db['response']['docs'])
# print documents

#load datasource
# records = [json.load(line) for line in open(string_result)]
# print records
#print records[0] [:2]