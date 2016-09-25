from django.db import models

class Table1(models.Model):
	# table can be found in MPdashboard.worksheets("Data")
	PM = models.CharField(max_length=255)
	P_nos = models.IntegerField()
	PS1 = models.FloatField()
	PS4 = models.FloatField()
	PS1vsPS4 = models.FloatField()
	Q1 = models.FloatField()
	Q2 = models.FloatField()
	Q3 = models.FloatField()
	Q4 = models.FloatField()
	cr = models.FloatField()
	crp = models.FloatField()

	# target = models.FloatField()
	# total = models.FloatField()