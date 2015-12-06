from django.contrib.gis.db import models
from django.utils import timezone
import secretballot

class Challenge(models.Model):
	slug = models.CharField(max_length=30)
	name = models.CharField(max_length=30)
	description = models.TextField()
	help_text = models.TextField('help text')
	geom = models.GeometryField('extent')
	active = models.BooleanField(default=False)
	creation_date = models.DateTimeField('date created', default=timezone.now)

class Task(models.Model):
	challenge = models.ForeignKey(
		Challenge,
		on_delete=models.CASCADE,
		db_column='challenge_slug',
		related_name='tasks')
	identifier = models.CharField(max_length=50)
	geom = models.GeometryCollectionField('geometry')
	status = models.CharField(max_length=10, default='new')
	creation_date = models.DateTimeField('date created', default=timezone.now)

secretballot.enable_voting_on(Challenge)