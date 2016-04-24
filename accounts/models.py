from __future__ import unicode_literals

from django.db import models
from django.conf import settings
# Create your models here.
class UserProfile(models.Model):
		
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	
	def __str__(self):
		return self.username