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

#sample query SAME1597591, SAMEA4195741
#for now let's deal with samples only
response = requests.get('http://www.ebi.ac.uk/biosamples/api/samples/SAMEA4195741')
data = response.json()

#print data["accession"]

# for key, value in data.items():
# 	print key, value


sample = mapsBioSampletoGA4GH(data)

for key, value in sample.characteristics['sampleSource'].items():
	print "sampleSource " + key, value

for key, value in sample.characteristics['phenotype'].items():
	print "Phenotype " + key, value
for key, value in sample.characteristics['disease'].items():
	print "Disease " + key, value