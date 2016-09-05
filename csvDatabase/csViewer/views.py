from django.db import transaction
from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
import csv

# Create your views here.

def index(request):
	client_list = Client.objects.order_by('prj_name')[:]
	output = ', '.join([client.prj_manager for client in client_list])
	return HttpResponse(output)

@transaction.atomic
def csView(request):
	filename = 'C:/Python/Django_Files/data.csv'
	with open(filename) as csvfile:
		csvreader = csv.reader(csvfile)
		header = csvreader.__next__()

		for line in csvreader:
			items = zip(header, line)
			item = {}
			
			for (name, value) in items:
				item[name] = value
				if (len(item)==4):
					client = Client(
						prj_name = item['Project Name'],
						prj_manager = item['Project Manager'],
						prj_number = item['Project No'],
						app_centre = item['Application Centre'])
					client.save()
				
	return HttpResponse('Uploaded')