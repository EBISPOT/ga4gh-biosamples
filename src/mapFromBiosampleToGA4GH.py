import json
import requests
from biosample import Biosample
from entity import Entity



def mapsBioSampletoGA4GH (data):
	#we use the accession as the name of the sample as well
	sample = Biosample(data["accession"], data["accession"], data["description"], data["characteristics"], data["organization"])



	#sample.characteristics is itself an array of arrays. It contains information about alleleName, geneName, material, alleleId, strain, geneSymbol, organism, geneId, alleleSymbol
	#each of those need to be parsed and mapped

	#let's build a list for the biosamples attributes we wish to be mapped to the GA4GH biosample
	descriptionList = ["description","clinicalHistory","secondaryDescription","sampleCharacteristics"]

	sampleSourcelist = ["hostBodyProduct","organismPart","sampleSourceName","strain","material","sourceName","bodysite","originalBodySiteAnnotation","hostBodySite","sampleType","environmentMaterial","biosourcetype","bodyProduct","bodySite","envMaterial"]

	phenotypeList = ["Organism","host","Species","cellType","hostTaxid","hostCommonName","specificHost","taxonId","hostScientificName","hostTaxonomyId","hostTissueSampled","subSpecies","sex","hostSex","hostAge","ageYears","age","ageY"]

	diseaseList = ["diseaseState","hostDisease","clinicallyAffectedStatus","condition","diagnosis","infection","diseaseStatus","clinicalinformation","healthState","disease","clinicalInformation","hostHealthState","status","affectedBy","clinicalhistory","tumor","causeOfDeath"]

	try:
		biocharacteristicSource = {}
		for key, value in data["characteristics"].items():
			if key in sampleSourcelist:
				biocharacteristicSource[key] = {}
				for s in data["characteristics"][key]:
					biocharacteristicSource[key] = {'termLabel': s["text"], 'termId': s["ontologyTerms"]}
			sample.characteristics['sampleSource'] = biocharacteristicSource
	except Exception:
		pass

	try:
		biocharacteristicPhenotype = {}
		for key, value in data["characteristics"].items():
			if key in phenotypeList:
				biocharacteristicPhenotype[key] = {}
				for s in data["characteristics"][key]:
					biocharacteristicPhenotype[key] = {'termLabel': s["text"], 'termId': s["ontologyTerms"]}
			sample.characteristics['phenotype'] = biocharacteristicPhenotype
	except Exception:
		pass

	try:
		biocharacteristicDisease = {}
		for key, value in data["characteristics"].items():
			if key in diseaseList:
				biocharacteristicDisease[key] = {}
				for s in data["characteristics"][key]:
					biocharacteristicDisease[key] = {'termLabel': s["text"], 'termId': s["ontologyTerms"]}
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



	return sample






