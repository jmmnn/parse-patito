#This script imports results from a solr server returning python format
import re
import urllib
#import urllib2
from pandas import Series, DataFrame
import pandas as pd

#path to datasource, make sure to use a python formated file
query_url= 'http://localhost:8888/solr/patito-files/select?q=*%3A*&rows=5&wt=python&indent=true' #change the rows=  to get a large dataset

connection = urllib.urlopen(query_url)
response = eval( connection.read() )
#print "number of matches=", response['response']['numFound']
for doc in response['response']['docs']:
	print 'Id =', doc['id']


# function passing pageCount returns the fileName
def getName(valor):
    file_name = response['response']['docs']['pageCount']
    print file_name,

getName(4)


def printOneDoc
for doc in response['response']['docs']:
  print 'Folder =', doc['attr_belongstocontainer']
  print 'File name =', doc['fileName']
  print 'Id =', doc['id']