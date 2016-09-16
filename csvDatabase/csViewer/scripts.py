from django.db import transaction
from django.shortcuts import render
from django.http import HttpResponse
from .models import Pinfo, Reporting, Backlog, PS1, PS4, Actuals, Payment, Slippages, CPO 

import csv
import os

# filename refers to csv file
# model_name refers to particular model 
# fields are strings that are to be placed into the assignment function
# field nos are the number of fields that are present inside fields

# make a dictionary relating the field names of models with the actual column name

root = "C:/Python/Django_Files/Data/"
filename = "full_data.csv"

file = root + filename

def has_numbers(inputstr):
	return any(char.isdigit() for char in inputstr)

def clean_data(file):
	ok = "FALSE"

	with open(file) as csvfile: 
		csvreader = csv.reader(csvfile)
		header = csvreader.__next__()

		file_name = 'Cleaned_Data.csv'
		new_file = file_root + file_name

		# deletes remakes if file exists, makes if doesnt
		try:
			os.remove(new_file)
			csvfile2 = open(new_file, 'w')
		except OSError: 
			csvfile2 = open(new_file, 'w')

		# writer headers into the file
		header_writer = csv.writer(csvfile2, delimiter=',')
		header_writer.writerow(header)

		csvwriter = csv.DictWriter(csvfile2, fieldnames=header)
		
		for line in csvreader:
			items = zip(header, line)
			item = {}
			
			for (name, value) in items: 
				if value == '' or value == "#VALUE!": 
					value = 0
				elif "%" in value: 
					value.strip('%')
					value = float(value)/100
				elif name != "Application Centre" and name != "Project Name" and name != "Project Number": 
					if has_numbers(value) and "K" in value: 
						value = value.strip("K")
						value = float(value) * 1000

				item[name] = value
				
				if len(item) == 34: 
					csvwriter.writerow(item)
		
		csvfile2.close()
	return(new_file)


def upload_data(filename):
	ok = "FALSE"

	with open(filename) as csvfile: 
		csvreader = csv.reader(csvfile)
		header = csvreader.__next__()
	
		for line in csvreader:
			items = zip(header, line)
			item = {}
			
			for (name, value) in items:
				name = name.strip()
				item[name] = value
				if len(item) == 34:

					pinfo = Pinfo(
						prj_name = item['Project Name'],
						prj_manager = item['Project Manager'],
						prj_number = item['Project Number'])
					pinfo.save()
				
					reporting = Reporting(
						# profit_centre = item['Profit Centre'], 
						# entity = item['Entity'],
						# activity = item['Activity'], 
						# report = item['Report Class Filter'],
						app_centre = item['Application Centre'])
					reporting.save()
				
		
					backlog = Backlog(
						revenue_backlog = item['Revenue Backlog (AED)'], 
						cost_to_go = item['Cost to Go (AED)'], 
						backlog_margin = item['Backlog Margin %'])
					backlog.save()
				
		
					ps1 = PS1(
						as_sold_revenue = item['As Sold Revenue'], 
						as_sold_cost = item['As Sold Cost'], 
						as_sold_margin_cost = item['As Sold Margin Amount'], 
						ps1_margin_lgm = item['PS1 Margin LGM'])
					ps1.save()
				
		
					ps4 = PS4(
						as_sold_revenue = item['As Sold Revenue'], 
						as_sold_cost = item['As Sold Cost'], 
						as_sold_margin_cost = item['As Sold Margin Amount'], 
						ps4_margin_lgm = item['PS4 Margin LGM'])
					ps4.save()
				
		
					actuals = Actuals(
						actual_cost = item['Actual Cost OTD'], 
						recognised_revenue_otd = item['Recognized Revenue OTD'], 
						invoice_revenue_otd = item['Invoice Revenue OTD'], 
						actual_cost_otd = item['Actual Cost OTD'],
						recognised_revenue_ytd = item['Recognized Revenue YTD'], 
						invoice_revenue_ytd = item['Invoice Revenue YTD'])
					actuals.save()
				
		
					payment = Payment(
						cash_in = item['Cash IN'], 
						excess_billing = item['Excess Billing'], 
						overdue = item['Unbilled'], 
						c_minus_i = item['C - I'],
						i_minus_r = item['I - R'], 
						c_minus_r_percentage = item['C - R %'])
					payment.save()
					
					# slippage = Slippages(
					# 	slippage_ps4_minus_ps1 = item['Slippage PS4 - PS1'])
					# slippage.save()

					# cpo = CPO(
					# 	merec_catalog = item['MEREC Category'], 
					# 	rel_score = item['REL Score']
					# 	)
						# rel_category = item['REL Category'],)
						# corporate_database = item['Corporate Database'])
					# cpo.save()
		ok = "TRUE"
	return(ok)