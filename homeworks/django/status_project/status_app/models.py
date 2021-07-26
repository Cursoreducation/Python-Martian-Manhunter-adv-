from django.db import models

# Create your models here.


class Page(models.Model):
    title = models.CharField(max_length=144)
    body = models.CharField(max_length=3000)