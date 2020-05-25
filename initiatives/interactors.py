"""All business use cases are written here in form of functions """

from .entities import Initiative

class GetInitiativeInteractor: 
    """Returns(gets) an initiatives based on init_id """
    def __init__(self, initiative_repo):
        self.initiative_repo = initiative_repo

    def set_params(self, init_id):
        self.init_id = init_id
        return self

    def execute(self):
        return self.initiative_repo.get_initiative(init_id = self.init_id)


class CreateNewInitiativeInteractor:
    """Creates new initiative """
    def __init__(self, initiative_repo):
        self.initiative_repo = initiative_repo

    def set_params(self, acronym, full_name):
        self.acronym = acronym
        self.full_name = full_name
        return self

    def execute(self):
        return self.initiative_repo.create_new_initiative(acronym = self.acronym, full_name = self.full_name)

class UpdateExistingInitiativeInteractor:
    """Updates/modifies existing initiatives """
    def __init__(self, initiative_repo):
        self.initiative_repo = initiative_repo

    def set_params(self, acronym, full_name):
        self.acronym = acronym
        self.full_name = full_name
        return self

    def execute(self):
        return self.initiative_repo.update_existing_initiative(acronym = self.acronym, full_name = self.full_name)

class DeleteExistingInitiativeInteractor:
    """Deletes an existing initiative """
    def __init__(self, initiative_repo):
        self.initiative_repo = initiative_repo

    def set_params(self, acronym, full_name):
        self.acronym = acronym
        self.full_name = full_name
        return self

    def execute(self):
        return self.initiative_repo.delete_existing_initiative(acronym = self.acronym, full_name = self.full_name)