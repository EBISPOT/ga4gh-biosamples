from abc import ABCMeta, abstractmethod


class Entity(object):
    """
    An entity in the GA4GH schema - can be an individual or sample
    """
__metaclass__ = ABCMeta


def __init__(self, id, name, description, characteristics, created, updated, info):
    """Return an Entity object"""
    self.id = id
    self.name = name
    self.description = description
    self.characteristics = characteristics
    self.created = created
    self.updated = updated
    self.info = info


def created_date(self):
    if self.created is None:
        return date.today().isoformat()
    return self.created


def updated_date(self):
    if self.updated is None:
        return date.today().isoformat()
    return self.updated


@abstractmethod
def entity_type():
    """returns the type of entity this is"""
    pass



