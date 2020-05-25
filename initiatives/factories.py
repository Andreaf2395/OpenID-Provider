"""factories represents dependency injections. They connect repositeries to interactors  """

from .repositeries import InitiativeRepo
from .interactors import GetInitiativeInteractor, CreateNewInitiativeInteractor, UpdateExistingInitiativeInteractor, DeleteExistingInitiativeInteractor
from .views import InitiativeView

def create_initiative_repo():
    return InitiativeRepo()

def create_get_initiative_interactor():
    return GetInitiativeInteractor(initiative_repo= create_initiative_repo())

def create_create_new_initiative_interactor():
    return CreateNewInitiativeInteractor(create_initiative_repo())

def create_update_existing_initiative_interactor():
    return UpdateExistingInitiativeInteractor(create_initiative_repo())

def create_delete_existing_initiative_interactor():
    return DeleteExistingInitiativeInteractor(create_initiative_repo())


def create_initiative_view(request, **kwargs):
    return InitiativeView(create_get_initiative_interactor(), create_create_new_initiative_interactor(),
    create_update_existing_initiative_interactor(), create_delete_existing_initiative_interactor())