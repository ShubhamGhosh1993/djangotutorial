from django.db import models

# Create your models here.
from tinymce.models import HTMLField

# Create your models here.
class Enquiry(models.Model):
    enquiry_title = models.CharField(max_length=100)
    enquiry_desc = HTMLField()