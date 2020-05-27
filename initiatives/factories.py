"""factories represents dependency injections. They connect repositeries to interactors  """

from .repositeries import InitiativeRepo
from .interactors import GetInitiativeInteractor, CreateNewInitiativeInteractor, UpdateExistingInitiativeInteractor, DeleteExistingInitiativeInteractor
from .views import InitiativeView

class InitiativeRepoFactory(object):
    @staticmethod
    def get():
        return InitiativeRepo()

class GetInitiativeInteractorFactory(object):
    @staticmethod
    def get():
        initiative_repo = InitiativeRepoFactory.get()
        return GetInitiativeInteractor(initiative_repo)

class CreateNewInitiativeInteractorFactory(object):
    @staticmethod
    def get():
        initiative_repo = InitiativeRepoFactory.get()
        return CreateNewInitiativeInteractor(initiative_repo)

class UpdateExistingInitiativeInteractorFactory():
    @staticmethod
    def get():
        initiative_repo = InitiativeRepoFactory.get()
        return UpdateExistingInitiativeInteractor(initiative_repo)

class DeleteExistingInitiativeInteractorFactory(object):
    @staticmethod
    def get():
        initiative_repo = InitiativeRepoFactory.get()
        return DeleteExistingInitiativeInteractor(initiative_repo)


class InitiativeViewFactory(object):
    @staticmethod
    def create():
        return InitiativeView(GetInitiativeInteractorFactory.get(), CreateNewInitiativeInteractorFactory.get(),
       UpdateExistingInitiativeInteractorFactory.get(), DeleteExistingInitiativeInteractorFactory.get())