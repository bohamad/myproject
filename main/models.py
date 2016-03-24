from django.db import models

# Create your models here.
class State(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True )
	abbreviation = models.CharField(max_length=2, null=True, blank=True)
	def __unicode__(self):
		return "%s"  % self.name


class StateCapital(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True )
	state = models.OneToOneField('main.State', null = True)
	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField(null=True, blank=True)
	population = models.IntegerField(null=True, blank=True)

	def __unicode__(self):
		return self.name


class City(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True )
	state = models.ForeignKey('main.State', null = True)
	country = models.CharField(max_length=100, null=True, blank=True )
	
	zip_code = models.IntegerField(null=True, blank=True )
	latitude  = models.FloatField(null=True, blank=True )
	longitude = models.FloatField(null=True, blank=True)

	def __unicode__(self):
		return '%s' % self.name




