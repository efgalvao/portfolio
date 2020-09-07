import os
from django.db import models
from django.conf import settings

def images_path():
    return os.path.join(settings.BASE_DIR, 'static')

class Project(models.Model):
    title = models.CharField("title", max_length=50)
    brief = models.CharField("brief", max_length=50)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.ImageField()
    github = models.URLField(max_length=50, blank=True)
    heroku = models.URLField(max_length=50, blank=True)

    def __str__(self):
        return self.title


