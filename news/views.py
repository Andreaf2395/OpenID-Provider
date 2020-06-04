"""These classes get interactors from factories.py, parse the input parameters and format the output with serializers"""

from django.shortcuts import render
import ast

from . serializers import MultipleNewsSerializer, NewsSerializer
from sso_trial.decorators import serialize_exceptions

class AllNewsView(object):
    def __init__(self, get_all_news_interactor = None, create_new_news_interactor = None):
        self.get_all_news_interactor = get_all_news_interactor
        self.create_new_news_interactor = create_new_news_interactor

    @serialize_exceptions
    def get(self):
        news = self.get_all_news_interactor.set_params().execute()

        body = MultipleNewsSerializer.serialize(news)
        status = 200

        return body,status

    @serialize_exceptions
    def post(self, news_title , news_content, tags, visible = True, audience = [] ):
        audience_list =  ast.literal_eval(audience)
       
        news = self.create_new_news_interactor.set_params(news_title = news_title, news_content = news_content, visible = visible, audience=audience_list, tags=tags).execute()
        body = NewsSerializer.serialize(news)
        status = 201

        return body,status


class NewsView(object):
    def __init__(self, get_news_interactor=None, update_existing_news_interactor = None, delete_existing_news_interactor = None):
        
        self.get_news_interactor = get_news_interactor
        self.update_existing_news_interactor = update_existing_news_interactor
        self.delete_existing_news_interactor = delete_existing_news_interactor
    
    @serialize_exceptions
    def get(self, id):
       
        news = self.get_news_interactor.set_params(id = id).execute()

        body = NewsSerializer.serialize(news)
        status = 200

        return body,status

    @serialize_exceptions
    def patch(self, id, news_title = None , news_content = None, visible = None, tags = None, audience = None):
        
        if audience is not None:
            audience =  ast.literal_eval(audience)
       
        news = self.update_existing_news_interactor.set_params(id = id, news_title= news_title, news_content= news_content, visible = visible, audience= audience, tags=tags).execute()

        body = NewsSerializer.serialize(news)
        status = 200

        return body,status

    def delete(self, id):
       
        self.delete_existing_news_interactor.set_params(id = id).execute()

        body = None
        status = 204

        return body,status

class AllNewsByTagView(object):
    def __init__(self, get_all_news_by_tag_interactor = None):
        self.get_all_news_by_tag_interactor = get_all_news_by_tag_interactor
        
    @serialize_exceptions
    def get(self, tag):
        news = self.get_all_news_by_tag_interactor.set_params(tag = tag).execute()

        body = MultipleNewsSerializer.serialize(news)
        status = 200

        return body,status

