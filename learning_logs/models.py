from django.db import models

# Create your models here.

class Topic(models.Model):
    "user学习主题"
    text = models.CharField(max_length=200)
    date_add