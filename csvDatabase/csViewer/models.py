from django.db import models

# Create your models here.
class Client(models.Model):

	prj_name = models.CharField(max_length=255)
	prj_number= models.CharField(max_length=255)

	prj_manager= models.CharField(max_length=255)
	app_centre= models.CharField(max_length=255)

	def __str__(self):
		return self.prj_name

