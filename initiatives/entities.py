"""Contains business properties of entities related to Initiative app"""

class Initiative:
    """Entity representing various initiatives and their properties"""

    def __init__(self, init_id, acronym, full_name): # Mind the underscore after self. 
        self._init_id = init_id 
        self._acronym = acronym
        self._full_name = full_name

    @property
    def init_id(self):
        return self._init_id
    
    @property
    def acronym(self):
        return self._acronym

    @property
    def full_name(self):
        return self._full_name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other