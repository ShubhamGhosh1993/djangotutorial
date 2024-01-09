from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class News(models.Model):
    news_title = models.CharField(max_length=100)
    news_desc = HTMLField()
    new_image = models.FileField(upload_to= "news/", max_length =255, null=True, default=None)