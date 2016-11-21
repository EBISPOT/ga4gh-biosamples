from entity import Entity


class Biosample(Entity):

	def __init__(self, id, name, description, characteristics, info, created="", updated=""):
		super(Biosample, self).__init__(id, name, description, characteristics, info, created, updated)

	def entity_type(self):
    	 return 'biosample'
