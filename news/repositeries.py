from .entities import News
from . models import ORMNews

class NewsRepo:

    def _decode_db_news(self, db_news):
        """This converts ORM db_news to entity news """
        audience = []
        audience_query_set = db_news.audience.all()
        for a in audience_query_set:
            audience.append(a.audience_type)

        return News(id=db_news.id,news_title=db_news.news_title,
                        news_content=db_news.news_content, visible=db_news.visible, publish_date=db_news.publish_date, audience=audience)

    def get_all_news(self):
        all_db_news = ORMNews.objects.all()
        
        news =[]
        for db_news in all_db_news:
            news.append(self._decode_db_news(db_news))
        return news

    def get_news(self, id):
        db_news = ORMNews.objects.get(id = id)
        return self._decode_db_news(db_news)

    def create_new_news(self, news_title, news_content, visible = True, audience = []):
        db_news = ORMNews.objects.create(news_title = news_title, news_content = news_content, visible = visible)
        for a in audience:
            db_news.audience.set(a)
        return self._decode_db_news (db_news)

    def update_existing_news(self, id, news_title = None, news_content = None,  visible = True, audience=[]):
        orm_news = ORMNews.objects.get(id = id)

        orm_news.news_title = news_title
        orm_news.news_content = news_content
        orm_news.visible = visible
        for a in audience:
            orm_news.audience.set(a)

        orm_news.save()

        return self._decode_db_news (orm_news)

    def delete_existing_news(self, id):
        orm_news = ORMNews.objects.get(id = id)
        orm_news.delete()