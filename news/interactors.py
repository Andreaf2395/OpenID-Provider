from .entities import News

class GetAllNewsInteractor(object):
    """Returns(gets) all news """
    def __init__(self, news_repo):
        self.news_repo = news_repo

    def set_params(self):
        return self

    def execute(self):
        return self.news_repo.get_all_news()

class GetNewsInteractor(object): 
    """Returns(gets) an news based on id """
    def __init__(self, news_repo):
        self.news_repo = news_repo

    def set_params(self, id):
        self.id = id
        return self

    def execute(self):
        return self.news_repo.get_news(id = self.id)


class CreateNewNewsInteractor(object):
    """Creates new news """
    def __init__(self, news_repo):
        self.news_repo = news_repo

    def set_params(self, news_title, news_content, visible = True, audience = []):
        self.news_title = news_title
        self.news_content = news_content
        self.visible = visible
        self.audience = audience
        return self

    def execute(self):
        return self.news_repo.create_new_news(news_title = self.news_title, news_content = self.news_content, visible = self.visible, audience = self.audience)

class UpdateExistingNewsInteractor(object):
    """Updates/modifies existing newss """
    def __init__(self, news_repo):
        self.news_repo = news_repo

    def set_params(self, id, news_title, news_content, visible = True, audience = []):
        self.id = id
        self.news_title = news_title
        self.news_content = news_content
        self.visible = visible
        self.audience= audience 
        return self

    def execute(self):
        return self.news_repo.update_existing_news(id = self.id, news_title = self.news_title, news_content = self.news_content, visible =self.visible, audience = self.audience)

class DeleteExistingNewsInteractor(object):
    """Deletes an existing news """
    def __init__(self, news_repo):
        self.news_repo = news_repo

    def set_params(self, id):
        self.id = id
        return self

    def execute(self):
        return self.news_repo.delete_existing_news(id = self.id)