from django.db import models
from initiatives.models import ORMInitiative

# Create your models here.

class ORMNews(models.Model):
    news_id = models.IntegerField()
    news_title = models.CharField(max_length=500)
    news_content = models.TextField()
    initiatives = models.ManyToManyField(ORMInitiative)
    visible = models.BooleanField()
    publish_date =  models.DateTimeField()
    
