# header[0] = 'Project Number'
# header[1] = 'Project Name'
# header[2] = 'WBS Element'
# header[3] = 'WBS Name'
# header[4] = ''
# header[5] = 'Activity'
# header[6] = 'Customer Number'
# header[7] = 'Customer Name'
# header[8] = 'Cost Type'
# header[9] = 'Cost Element Name'
# header[11] = 'PS0'
# header[12] = 'PS1'
# header[13] = 'PS2'
# header[15] = 'PS3'
# header[16] = 'PS4'
# header[17] = 'Actual '
# header[18] = 'Commitment'
# header[19] = 'POC%'

from django.db import models 

class db1(models.Model):
	pno = models.CharField(max_length=255)
	pname = models.CharField(max_length=255)
	wbsElement = models.CharField(max_length=255)
	wbsName = models.CharField(max_length=255)
	act = models.CharField(max_length=255)
	cusNo = models.CharField(max_length=255)
	cusName = models.CharField(max_length=255)
	cosType = models.CharField(max_length=255)
	cosElementNumber = models.CharField(max_length=255)
	cosElementName = models.CharField(max_length=255)
	ps0 = models.FloatField()
	ps2 = models.FloatField()
	ps4 = models.FloatField()
	actual = models.FloatField()
	commitment = models.FloatField()
	poc = models.FloatField()