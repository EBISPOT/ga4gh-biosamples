from abc import ABCMeta, abstractmethod
from datetime import date


class Entity(object):
    """
    An entity in the GA4GH schema - can be an individual or sample
    """
    __metaclass__ = ABCMeta


    def __init__(self, id, name, description, characteristics, info, created="", updated=""):
        """Return an Entity object"""
        self.id = id or ""
        self.name = name or ""
        self.description = description or ""
        self.characteristics = characteristics or []
        self.created = created or self.created_date()
        self.updated = updated or self.updated_date()
        self.info = info or []


    def created_date(self):
        return date.today().isoformat()



    def updated_date(self):
        return date.today().isoformat()



    @abstractmethod
    def entity_type():
        """returns the type of entity this is"""
        pass



