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

	# #we need to check the values of data exist or we need to give a default value
	# accession = data["accession"]
	# description = data["description"]
	# characteristics = data["characteristics"]
	# organization = data["organization"]

	#we use the accession as the name of the sample as well
	#TODO : add check for cases in whihc an attribute doesn't exist, e.g., data["organization"]
	sample = Biosample(data["accession"], data["accession"], data["description"], data["characteristics"], data["description"])


	#print data["accession"]

	#sample.characteristics is itself an array of arrays. It contains information about alleleName, geneName, material, alleleId, strain, geneSymbol, organism, geneId, alleleSymbol
	#each of those need to be parsed and mapped

	#let's build a list for the biosamples attributes we wish to be mapped to the GA4GH biosample
	descriptionList = ["description","clinicalHistory","secondaryDescription","sampleCharacteristics"]

	sampleSourcelist = ["hostBodyProduct","organismPart","sampleSourceName","strain","material","sourceName","bodysite","originalBodySiteAnnotation","hostBodySite","sampleType","environmentMaterial","biosourcetype","bodyProduct","bodySite","envMaterial"]

	phenotypeList = ["Organism","host","Species","cellType","hostTaxid","hostCommonName","specificHost","taxonId","hostScientificName","hostTaxonomyId","hostTissueSampled","subSpecies","sex","hostSex","hostAge","ageYears","age","ageY"]

	diseaseList = ["diseaseState","hostDisease","clinicallyAffectedStatus","condition","diagnosis","infection","diseaseStatus","clinicalinformation","healthState","disease","clinicalInformation","hostHealthState","status","affectedBy","clinicalhistory","tumor","causeOfDeath"]

	try:
		biocharacteristicSource = []
		for key, value in data["characteristics"].items():
			if key in sampleSourcelist:
				for s in data["characteristics"][key]:
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
		for key, value in data["characteristics"].items(): #we browse the data list, and check whether we find something of interest
			if key in phenotypeList: #we found a phenotype
				for s in data["characteristics"][key]: # get the values from the phenotype
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
		for key, value in data["characteristics"].items():
			if key in diseaseList:
				for s in data["characteristics"][key]:
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






