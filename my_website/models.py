from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=280)
    long_description = models.TextField()
    technology = models.CharField(max_length=150)
    image = models.CharField(max_length=100)
    github_link = models.URLField(max_length=200, default="https://github.com/foorast")
