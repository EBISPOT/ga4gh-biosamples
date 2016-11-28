# import json
# import urllib.request
# req = urllib.request.Request('https://www.ebi.ac.uk/biosamples/xml/groups/SAMEG82620')
# with urllib.request.urlopen(req) as response:
#     result = json.loads(response.readall().decode('utf-8'))


import json
import requests
from biosample import Biosample
from entity import Entity
from mapFromBiosampleToGA4GH import mapsBioSampletoGA4GH

#group query
#response = requests.get('http://www.ebi.ac.uk/biosamples/api/groups/SAMEG82620')




#when we retrieve multiple samples, those are placed in an _embedded array
#we need to retrieve each individual sample and map it to the GA4GH sample (Only for the "samples" key)

#samples is an array of GA4GH biosample objects
samples = []

#sample query SAME1597591, SAMEA4195741
#for now let's deal with samples only
response = requests.get('http://www.ebi.ac.uk/biosamples/api/samples/SAMEA4195741')   #SAME1630551

data = response.json()


#if we retrieve only one sample
samples.append(mapsBioSampletoGA4GH(data))


#if we query the other endpoint to retrieve multiple samples
#response = requests.get('https://www.ebi.ac.uk/biosamples/api/samples/search/findByText?text=Merluccius-Merluccius')
#response = requests.get('https://www.ebi.ac.uk/biosamples/api/samples/search/findByText?text=achondroplasia')


#data = response.json()


# try:
# 	#we retrieve samples, when multiples, in an _embedded object. This needs to be split, and each sample passed to the mapping method to build the GA4GH samples
# 	for i in range(0, len(data["_embedded"]["samples"])):
# 		samples.append(mapsBioSampletoGA4GH(data["_embedded"]["samples"][i]))
# except Exception as e:
# 	pass




#to check the content of the samples list that had been built based on the _embedded object
for sample in samples:
	print sample.id
	print "phenotype: ", sample.characteristics["phenotype"]
	print "disease: ", sample.characteristics["disease"]
	print "sample source: ", sample.characteristics['sampleSource']
