from django.db import models
import uuid

class Member(models.Model):
	"""
	This class specifies the Attributes of a Team Member object.
	"""
	firstName = models.CharField(max_length=200, null=False, blank=False)
	lastName = models.CharField(max_length=200, null=False, blank=False)
	email = models.CharField(max_length=200, null=False, blank=False)
	mobile = models.CharField(max_length=14, null=False, blank=False) # +91-9585364407 (14 chars)
	ROLE_CHOICES = (
		(1, ("Admin")),
		(2, ("Regular")),
	)
	role =  models.IntegerField(choices=ROLE_CHOICES, null=False, blank=False)

