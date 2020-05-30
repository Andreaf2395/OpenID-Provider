from django.db import models
from initiatives.models import ORMInitiative

# Create your models here.

class ORMAudience(models.Model):
    audience = (
    ('S','Student'),('T','Teacher'),('G','General')
    )
    audience_type = models.CharField(choices=audience, max_length=1)
    def __str__(self):
        return self.audience_type

class ORMNews(models.Model):

    news_title = models.CharField(max_length=500)
    news_content = models.TextField()
    
    visible = models.BooleanField(default=True)
    audience = models.ManyToManyField(ORMAudience, default = 'G')
    publish_date =  models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'ORMNews'
        verbose_name_plural = 'ORMNews'

    def __str__(self):
        return self.news_title
