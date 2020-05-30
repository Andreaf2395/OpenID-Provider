"""factories represents dependency injections. They connect repositeries to interactors  """

from .repositeries import NewsRepo
from .interactors import GetAllNewsInteractor, GetNewsInteractor, CreateNewNewsInteractor, UpdateExistingNewsInteractor, DeleteExistingNewsInteractor
from .views import NewsView, AllNewsView

class NewsRepoFactory(object):
    @staticmethod
    def get():
        return NewsRepo()

class GetAllNewsInteractorFactory(object):
    @staticmethod
    def get():
        news_repo = NewsRepoFactory.get()
        return GetAllNewsInteractor(news_repo)

class GetNewsInteractorFactory(object):
    @staticmethod
    def get():
        news_repo = NewsRepoFactory.get()
        return GetNewsInteractor(news_repo)

class CreateNewNewsInteractorFactory(object):
    @staticmethod
    def get():
        news_repo = NewsRepoFactory.get()
        return CreateNewNewsInteractor(news_repo)

class UpdateExistingNewsInteractorFactory():
    @staticmethod
    def get():
        news_repo = NewsRepoFactory.get()
        return UpdateExistingNewsInteractor(news_repo)

class DeleteExistingNewsInteractorFactory(object):
    @staticmethod
    def get():
        news_repo = NewsRepoFactory.get()
        return DeleteExistingNewsInteractor(news_repo)


class NewsViewFactory(object):
    @staticmethod
    def create(request, **kwargs):
        return NewsView(GetNewsInteractorFactory.get(), 
       UpdateExistingNewsInteractorFactory.get(), DeleteExistingNewsInteractorFactory.get())

class AllNewsViewFactory(object):
    @staticmethod
    def create(request, **kwargs):
        return AllNewsView(GetAllNewsInteractorFactory.get(), CreateNewNewsInteractorFactory.get())