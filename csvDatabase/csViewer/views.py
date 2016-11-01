from django.db import transaction
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import db1
from .Classes.Classes import Classy
import sqlite3
from pathlib import Path
import csv

p = str(Path(__file__).parents[2])
srcFile = p + '/Data/BPSimport1.csv'
destFile = p + '/Data/BPSFinal.csv'

# make new global instance of class 

	
@transaction.atomic
def dbUpload():
	with open(destFile, 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		csvreader.__next__()
		for line in csvreader:
 			push = db1(
 				pno = line[0],
				pname = line[1],
				wbsElement = line[2],
				wbsName = line[3],
				act = line[5],
				cusNo = line[6],
				cusName = line[7],
				cosType = line[8],
				cosElementNumber = line[9],
				cosElementName = line[10],
				ps0 = float(line[12]),
				ps2 = float(line[13]),
				ps4 = float(line[16]),
				actual = float(line[17]),
				commitment = float(line[18]),
				poc = float(line[19])
				)
 			push.save()

def index(request):
	return render(request, "csViewer/template.html")

def index2(request):
	return render(request, "csViewer/dashboard.html")

def upload(request):
	C = Classy() 
	# make new file with filled headers
	C.writeHeader(srcFile, destFile)
	# upload to db 
	dbUpload()
	# write test to see if uploaded
	return (HttpResponse("So Clean, Uploaded!"))

def dashboard(request):
	a = []
	C = Classy() 
	# a = C.returnCols(C1='cosType',
	# 	C2='cosElementNumber', 
	# 	C3='cosElementName', 
	# 	C4='ps0',
	# 	C5='ps2', 
	# 	C6='ps4',
	# 	C7='actual',
	# 	C8='commitment')
	# a = C.returnAll()
	a = C.selectAllWhere('cosType', 'Execution Cost')
	b = C.returnAll()
	return render(request, "csViewer/Page2.html", {'WhereData' : a, 'AllData' : b} )