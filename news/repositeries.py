from .entities import News, Audience
from . models import ORMNews, ORMAudience

class NewsRepo:

    def _decode_db_news(self, db_news):
        """This converts ORM db_news to entity news """
        audience = []
        audience_query_set = db_news.audience.all()

        for a in audience_query_set:
            audience.append(Audience(a.audience_type))

        return News(id=db_news.id,news_title=db_news.news_title,
                        news_content=db_news.news_content, visible=db_news.visible, 
                        publish_date=db_news.publish_date, audience=audience, tags=db_news.tags)

    def get_all_news(self):
        all_db_news = ORMNews.objects.all()
        
        news =[]
        for db_news in all_db_news:
            news.append(self._decode_db_news(db_news))
        return news

    def get_news(self, id):
        db_news = ORMNews.objects.get(id = id)
        return self._decode_db_news(db_news)

    def create_new_news(self, news_title, news_content, tags, visible = True, audience = []):
        db_news = ORMNews.objects.create(news_title = news_title, news_content = news_content, visible = visible, tags = tags)
        for a in audience:
            db_news.audience.add(a)
        return self._decode_db_news (db_news)

    def update_existing_news(self,news):
        orm_news = ORMNews.objects.get(id = news.id)
        orm_news.audience.clear()

        orm_news.news_title = news.news_title
        orm_news.news_content = news.news_content
        orm_news.visible = news.visible
        orm_news.tags = news.tags
        for a in news.audience:
            orm_aud = ORMAudience.objects.filter(audience_type = a.audience_type)[0]
            orm_news.audience.add(orm_aud)
        orm_news.save()

        return self._decode_db_news (orm_news)

    def delete_existing_news(self, id):
        orm_news = ORMNews.objects.get(id = id)
        orm_news.delete()

    def get_all_news_by_tag(self, tag):
        all_db_news = ORMNews.objects.filter(tags__icontains = tag)
        
        news =[]
        for db_news in all_db_news:
            news.append(self._decode_db_news(db_news))
        return news

   