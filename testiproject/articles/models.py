from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=40, blank=True)
    content = models.TextField()