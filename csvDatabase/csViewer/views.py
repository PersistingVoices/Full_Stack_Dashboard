from django.db import transaction
from django.shortcuts import render
from django.http import HttpResponse
from .models import Table1
from .dataScripts import clean_data
from .Classes import Classy

## root1 = "C:/Python/Django_Files/Data/"
root = "/home/shriram/Documents/Python/work/ENV3/Django/Data/"
src_file1 = "full_data.csv"
src_file2 = "Cost_Forecasting.csv"
dest_file = 'Cleaned_Data.csv'

# file1 for full data
file1 = root + src_file1
# file2 to include cost forcasting 
file2 = root + src_file2
# new clean file name
new = root + dest_file
# Create your views here.

@transaction.atomic
def upload_data(PM, P_nos, PS1, PS4, PS1vsPS4, 
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
		ok = "TRUE"
	return ok

#@transaction.atomic
def index(request):
	ok = "False"
	clean_data(file1, file2, new)
	C = Classy()
	
	(unique_pm, 
	P_nos, PS1,
	PS4, PS1vsPS4,
	Q1_sales, Q2_sales,
	Q3_sales, Q4_sales,
	crp, cr) = C.before_upload(new)

	upload_data(unique_pm, P_nos, PS1, PS4, PS1vsPS4, 
				Q1_sales, Q2_sales, Q3_sales, Q4_sales, crp, cr)
	return(HttpResponse("Done!, Check DB"))


