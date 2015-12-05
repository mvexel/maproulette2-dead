from django.contrib.gis.db import models

class Challenge(models.Model):
	slug = models.CharField(max_length=30)
	name = models.CharField(max_length=30)
	description = models.TextField()
	help_text = models.TextField('help text')
	geom = models.GeometryField('extent')

class Task(models.Model):
	challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
	identifier = models.CharField(max_length=50)
	pub_date = models.DateTimeField('date published')
	geom = models.GeometryCollectionField('geometry')


