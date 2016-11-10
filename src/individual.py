from entity import Entity


class Individual(Entity):

    def entity_type(self):
        return 'individual'

    def __init__(self, individualID):
        self.individualID = individualID
