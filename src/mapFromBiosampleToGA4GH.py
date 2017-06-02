import json
import requests
from biosample import Biosample
from entity import Entity


def createBiocharacteristic(data,interestList,characteristicLabel):  #data, phenotypeList, 'phenotype'
	try:
		biocharacteristic = []
		for key, value in data["characteristics"].items(): #we browse the data list, and check whether we find something of interest
			if key in interestList: #we found a phenotype
				for s in data["characteristics"][key]: # get the values from the phenotype
					biocharacteristicDict = {} #create an empty dict to store the content of the key found for phenotype
					biocharacteristicDict['termLabel'] = s["text"]
					biocharacteristicDict['termId'] =  s["ontologyTerms"] #TODO: check this is populated
					biocharacteristic.append(biocharacteristicDict)
			sample.characteristics['phenotype'] = biocharacteristic
	except Exception:
		pass


def mapsBioSampletoGA4GH (data):
	"""Generate GA4GH Biosample representation from EBI Biosamples data."""

	# Get all top-lvel keys from json response
	data_keys = data.keys()

	# Additional attributes found in EBI Biosamples but with no direct mapping to GA4GH
	info = []

	# Check if Biosamples response contains attributes that map to GA4GH
	# Accession
	if 'accession' in data_keys:
		id = data["accession"]
		name = data['accession']
		data_keys.remove('accession')

	# Description
	if "description" in data_keys:
		description = data["description"]
		data_keys.remove('description')
	else:
		description = "null"

	# Characteristics
	if "characteristics" in data_keys:
		characteristics = data["characteristics"]
		data_keys.remove('characteristics')

	# Release Date
	if "releaseDate" in data_keys:
		created = data["releaseDate"]
		data_keys.remove('releaseDate')
	else:
		created = "1974-07-04"  # date EMBL became a legal entity, use ISO 8601 format of YYYY-MM-DD

	# Updated Date
	if "updateDate" in data_keys:
		updated = data["updateDate"]
		data_keys.remove('updateDate')
	else:
		updated = "1974-07-04"

	# Addititional attributes 
	additional_attributes = {}
	for key in data_keys:
		if key != '_links':
			additional_attributes[key] = data[key]
	info.append(additional_attributes)


	# create Biosample object: id, name, description, characteristics, info, created, updated
	sample = Biosample(id, name, description, characteristics, info, created, updated)
	print "** SAMPLE: ", sample.id, "\n** CHAR: ", sample.characteristics

	
	#sample.characteristics is itself an array of arrays. It contains information about alleleName, geneName, material, alleleId, strain, geneSymbol, organism, geneId, alleleSymbol
	#each of those need to be parsed and mapped

	#let's build a list for the biosamples attributes we wish to be mapped to the GA4GH biosample
	descriptionList = ["description","clinicalHistory","secondaryDescription","sampleCharacteristics"]

	sampleSourcelist = ["hostBodyProduct","organismPart","sampleSourceName","strain","material","sourceName","bodysite","originalBodySiteAnnotation","hostBodySite","sampleType","environmentMaterial","biosourcetype","bodyProduct","bodySite","envMaterial"]

	phenotypeList = ["Organism","organism","host","Species","cellType","hostTaxid","hostCommonName","specificHost","taxonId","hostScientificName","hostTaxonomyId","hostTissueSampled","subSpecies","sex","hostSex","hostAge","ageYears","age","ageY"]

	diseaseList = ["diseaseState","hostDisease","clinicallyAffectedStatus","condition","diagnosis","infection","diseaseStatus","clinicalinformation","healthState","disease","clinicalInformation","hostHealthState","status","affectedBy","clinicalhistory","tumor","causeOfDeath"]

	try:
		biocharacteristicSource = []
		for key, value in list(data["characteristics"].items()):
			if key in sampleSourcelist:
				#print ("Found sample key: ", key)
				for s in list(data["characteristics"][key]):
					biocharacteristicDict = {} #create an empty dict to store the content of the key found for phenotype
					biocharacteristicDict['termLabel'] = s["text"]
					if "ontologyTerms" in s:
						biocharacteristicDict['termId'] =  s["ontologyTerms"]
					biocharacteristicSource.append(biocharacteristicDict)
			sample.characteristics['sampleSource'] = biocharacteristicSource
	except Exception:
		pass

	try:
		biocharacteristicPhenotype = []
		for key, value in list(data["characteristics"].items()): #we browse the data list, and check whether we find something of interest
			#print ("existing phenotype keys: ", key)
			if key in phenotypeList: #we found a phenotype
				#print ("Found phenotype key: ", key)
				for s in list(data["characteristics"][key]): # get the values from the phenotype
					biocharacteristicDict = {} #create an empty dict to store the content of the key found for phenotype
					biocharacteristicDict['termLabel'] = s["text"]
					if "ontologyTerms" in s:
						biocharacteristicDict['termId'] =  s["ontologyTerms"]
					biocharacteristicPhenotype.append(biocharacteristicDict)
			sample.characteristics['phenotype'] = biocharacteristicPhenotype
	except Exception:
		pass

	try:
		biocharacteristicDisease = []
		for key, value in list(data["characteristics"].items()):
			if key in diseaseList:
				#print ("Found disease key: ", key)
				for s in list(data["characteristics"][key]):
					biocharacteristicDict = {} #create an empty dict to store the content of the key found 
					biocharacteristicDict['termLabel'] = s["text"]
					if "ontologyTerms" in s:
						biocharacteristicDict['termId'] =  s["ontologyTerms"]
					biocharacteristicDisease.append(biocharacteristicDict)
			sample.characteristics['disease'] = biocharacteristicDisease
	except Exception:
		pass

	# for key, value in sample.characteristics['sampleSource'].items():
	# 	print "sampleSource " + key, value

	# for key, value in sample.characteristics['phenotype'].items():
	# 	print "Phenotype " + key, value

	# for key, value in sample.characteristics['disease'].items():
	# 	print "Disease " + key, value

#mapping to the description field:  in addition to the above retrieved description, need to fetch and concatenate information from the following Biosamples fields: description, clinicalHistory, secondaryDescription, sampleCharacteristics
#in this case however we just want a string at the end - unless we want to stick this in info? 



	return sample






