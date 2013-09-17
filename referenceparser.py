#crawl and index using Solr - done
#get from Solr a list of all the document IDs in the collection. Variable is type set: solr_ids
import urllib
import re
import nltk

query_url= "http://127.0.0.1:8888/solr/patito-files/select?q=*%3A*&start=0&rows=2&fl=body&wt=csv&indent=true" #change the rows=  to get a large dataset
query_result = urllib.urlopen(query_url)
query_result_string = query_result.read()
#print query_result_string  #uncomment this to see the solr_ids

#keep only domains of interest e.g. un.org
#solr_ids_list = re.findall(r'\w*pdf', query_result_string)
# solr_ids_list = re.findall(r'\*pdf', query_result_string)
# print solr_ids_list

#open each doc though Solr rest api 
#parse each document to find its own document symbol. Variable type string: doc_symbol
#create a dictionary to keep pairs [solr_id : doc_symbol]

tokens = nltk.word_tokenize(query_result_string)
print tokens






#TODO later
#parse the body of each document to find citations to other documents e.g. A/RES/...
# write a new document keeping the citations from each document: 
# e.g. docsymbol X [docsymbol Y, Doc Z] , doc A [doc X, doc B]
 

