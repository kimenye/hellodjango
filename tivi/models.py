from django.db import models

# Create your models here.
class Show(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()

	def __unicode__(self):
		return self.name