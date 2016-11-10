# import json
# import urllib.request
# req = urllib.request.Request('https://www.ebi.ac.uk/biosamples/xml/groups/SAMEG82620')
# with urllib.request.urlopen(req) as response:
#     result = json.loads(response.readall().decode('utf-8'))


import json
import requests
from biosample import Biosample

#group query
#response = requests.get('http://www.ebi.ac.uk/biosamples/api/groups/SAMEG82620')

#sample query SAME1597591
#for now let's deal with samples only
response = requests.get('http://www.ebi.ac.uk/biosamples/api/samples/SAME1597591')
data = response.json()

sample = Biosample()


for key, value in data.items():
     #print key, value
     sample.id = data["accession"]
     sample.description =  data["description"]
     sample.characteristics = data["characteristics"]
    # print "biosample description is: " + str(biosample.description)
     sample.created = data["releaseDate"]
     sample.updated = data["updateDate"]

#print sample.entity_type()
print sample.characteristics.keys()
print sample.characteristics.values()

for item in sample.characteristics.values():
	  print item

    #     self.id = id
    # self.name = name
    # self.description = description
    # self.characteristics = characteristics
    # self.created = created
    # self.updated = updated
    # self.info = info
    #print data['description']

    #print('{} {}'.format(item['id'], item['summary']))


#print data
