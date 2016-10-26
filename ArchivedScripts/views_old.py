from django.db import transaction
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Table1
from .dataScripts import clean_data
from .Classes import Classy
import sqlite3

## root1 = "C:/Python/Django_Files/Data/"
root = "/home/shriram/Documents/Python/work/ENV3/Django/Data/"
src_file1 = "full_data.csv"
src_file2 = "Cost_Forecasting.csv"
dest_file = "Cleaned_Data.csv"

# file1 for full data
file1 = root + src_file1
# file2 to include cost forcasting 
file2 = root + src_file2
# new clean file name
new = root + dest_file
# Create your views here.

@transaction.atomic
def upload_data_to_db(PM, P_nos, PS1, PS4, PS1vsPS4, 
				Q1, Q2, Q3, Q4, crp, cr):
	ok = "FALSE"
	for i in PM:	
		table1 = Table1(
			PM = i,
			P_nos = P_nos[i],
			PS1 = PS1[i], 
			PS4 = PS4[i], 
			PS1vsPS4 = PS1vsPS4[i], 
			Q1 = Q1[i], 
			Q2 = Q2[i], 
			Q3 = Q3[i], 
			Q4 = Q4[i], 
			crp = crp[i],
			cr = cr[i]
			)
		table1.save()
	
def index(request):

	# clean_data takes in two files, combines them
	# and writes it to a new csv file
	clean_data(file1, file2, new)
	# makes a new instance of the class Classy()
	C = Classy()
	
	# Before upload takes the new csv file, new and 
	# spits out lists that have operations that have been performed on them , that can be uploaded into the DB
	(PM, 
	P_nos, PS1,
	PS4, PS1vsPS4,
	Q1_sales, Q2_sales,
	Q3_sales, Q4_sales,
	crp, cr) = C.before_upload(new)

	# upload the finished lists into the DB, basically performs
	# insert statements into the DB
	upload_data_to_db(PM, P_nos, PS1, PS4, PS1vsPS4, 
				Q1_sales, Q2_sales, Q3_sales, Q4_sales, 
				crp, cr)

	return HttpResponse("DB Uploaded")

# make into a new super function, or make into class
# returns specif rows ad columns as JSON

def dict_factory(cursor, row):
	d= {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return (d)

def ret_fields(id1, id2):
	# somehow, I dont need to specify the actual db path
	# simply specifing  the name of the db will do
	con = sqlite3.connect("db.sqlite3")
	con.row_factory = dict_factory
	cur = con.cursor()
	cur.execute("SELECT " + id1 + " , " + id2 +" PS1 FROM csViewer_table1")
	return (cur.fetchall())

def dashboard(request):
	a = []
	a = ret_fields("PM", "PS1")
	# return JsonResponse(a, safe=False)
	# return render(request, "csViewer/Page2.html", {'JsonData': a})
	return render(request, "csViewer/index.html")