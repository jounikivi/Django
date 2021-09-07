from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class Articles(models.Model):
    title = models.TextField()
    content = models.TextField()