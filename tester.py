import csv
# import prettyprint as pp
def tester():

	# C:\Program Files\PostgreSQL\9.6\data

	filename = 'C:/Python/Django_Files/data.csv'
	j = 0 
	with open(filename) as csvfile:
		csvreader = csv.reader(csvfile,delimiter=',')
		header = csvreader.__next__()
		print(header)

		for line in csvreader:
			items = zip(header, line)
			item = {}
			for (name, value) in items:
				item[name] = value
				if(len(item)==4):
					j = j+ 1
					print(item,j)

				# client = Client(
				# 	prj_name = item['Project Name'],
				# 	prj_manager = item['Project Manager'],
				# 	prj_number = item['Project No'],
				# 	app_centre = item['Application Centre'])

				# client.save()
tester()