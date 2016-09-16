from django.db import transaction
from django.shortcuts import render
from django.http import HttpResponse
from .scripts import upload_data, clean_data
from .models import Pinfo 

import csv

# Create your views here.

def index(request):
	all_prj_names = Pinfo.objects.all()[:100]
	
	context = {'all_prj_names': all_prj_names}
	return render(request, 'csViewer/index.html',context)

# @transaction.atomic
# def csView(request):
# 	file_root = "C:/Python/Django_Files/Data/"
# 	file_name = "full_data.csv"
# 	file = file_root + file_name

# 	new_file_path = clean_data(file)
# 	print(HttpResponse(new_file_path))

# 	ok = "FALSE"
# 	ok = upload_data(new_file_path)
# 	if ok == "FALSE":
# 		return HttpResponse('Not Uploaded')
# 	else:
# 		return HttpResponse(ok)


