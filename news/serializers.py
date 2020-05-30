class NewsSerializer:
    @staticmethod
    def serialize(news):
        return {
            'id': int(news.id),
            'news_title': news.news_title,
            'news_content': news.news_content,
            'visible': news.visible,
            'publish_date': news.publish_date,
            'audience': news.audience,
        }

class MultipleNewsSerializer:

    @staticmethod
    def serialize(news):
        return [NewsSerializer.serialize(news_) for news_ in news]