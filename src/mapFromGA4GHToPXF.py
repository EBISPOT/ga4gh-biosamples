import json
from biosample import Biosample
from entity import Entity
from phenopacket import *
from phenopacket.models.Meta import *
from phenopacket.models.Environment import *
from phenopacket.models.Condition import *
from phenopacket.PhenoPacket import *


#we have an array of samples
#first we need to write the PXF entities, here samples as a list of entities in PXF
#then for each sample, we need to write the phenotype_profile and the diagnosis_profile (where the latter represents diseases)
#we want to generate a PXF file at the end

def mapToPXF(samples):
	# Add Entity(s)
	sample_1 = Entity(
                    id = "http://ga4gh.org/samples/1",
                    type = EntityType.sample)
	# sample_2 = Entity(
 #                    id = "http://ga4gh.org/samples/2",
 #                    type = EntityType.sample)

	# phenopacket_entities = [sample_1, sample_2]
	phenopacket_entities = [sample_1]

	environment = Environment()
	severity = ConditionSeverity()
	onset = TemporalRegion()
	offset = TemporalRegion()


	phenotype_1_1 = Phenotype(
                        environment=environment,
                        severity=severity,
                        onset=onset,
                        offset=offset)


	#phenotype_1_1.onset = TemporalRegion()
	phenotype_1_1.types = [OntologyClass()]
	phenotype_1_1.types[0].id = "HP:0003593"
	phenotype_1_1.types[0].label = "Infantile onset"

	phenotype_association_1_1 = PhenotypeAssociation(
                                entity = sample_1.id,
                                evidence_list = [],     # Sequence[Evidence]=[],
                                # created = "!!date 2016 2 9"
                                phenotype = phenotype_1_1)

	phenotype_profile_1 = [phenotype_association_1_1]   # : Sequence[PhenotypeAssociation]=[]
	phenopacket = PhenoPacket(
                        packet_id = "packet1",
                        title = "Biosample export",
                        entities = phenopacket_entities,
                        # schema = "journal-example-level-1",
                        # '@context = "http://phenopacket.github.io/context/context.jsonld",
                        phenotype_profile = phenotype_profile_1)

	print(phenopacket)


mapToPXF("")
