from django.contrib.gis.db import models

class Task(models.Model):
    slug = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    geom = models.GeometryField('geometry')
