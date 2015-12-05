from django.contrib.gis.db import models

class Challenge(models.Model):
	slug = models.CharField(max_length=30, primary_key=True)
	name = models.CharField(max_length=30)
	description = models.TextField()
	help_text = models.TextField('help text')
	geom = models.GeometryField('extent')

class Task(models.Model):
	challenge = models.ForeignKey(
		Challenge,
		on_delete=models.CASCADE,
		db_column='challenge_slug')
	identifier = models.CharField(max_length=50, primary_key=True)
	pub_date = models.DateTimeField('date published')
	geom = models.GeometryCollectionField('geometry')


