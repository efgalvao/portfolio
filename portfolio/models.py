import os
from django.db import models
from django.conf import settings



class Project(models.Model):
    title = models.CharField("title", max_length=50)
    brief = models.CharField("brief", max_length=50)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.FilePathField(path='/static/img')
    github = models.URLField(max_length=50)
    heroku = models.URLField(max_length=50)

    def __str__(self):
        return self.title


