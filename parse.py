#This script imports results from a solr server returning python format
import re
import urllib
#import urllib2

#path to datasource, make sure to use a python formated file
query_url= 'http://localhost:8888/solr/patito-files/select?q=*%3A*&rows=5&wt=python&indent=true' #change the rows=  to get a large dataset

def parse(query_url):
	connection = urllib.urlopen(query_url)
	response = eval( connection.read() )
	return response

def main():
    # Call our parse function and give it the needed parameters
    new_data = parse(query_url)

    # Let's see what the data looks like!
    print new_data


if __name__ == "__main__":
    main()


# print "number of matches=", response['response']['numFound']
# for doc in response['response']['docs']:
#   print 'Folder =', doc['attr_belongstocontainer']
#   print 'File name =', doc['fileName']
#   print 'Id =', doc['id']

#to navigate the response:
#new_data = parse.parse(parse.query_url) # start by loading some data
#new_data.keys() #returns the keys of the entire dictionary
#new_data['response'].keys() #returns the keys of the response DICT
#new_data['response']['docs'] #returns a LIST of DICTs of the actial documents
#new_data['response']['docs'][0] #returns DICT document 0 with keys and values
#new_data['response']['docs'][2].keys() #returns the keys for document 2 DICT
#new_data['response']['docs'][0].values() #returns just the values
#new_data['response']['docs'][2]['author'] #returns the author of doc number 2

