import csv,os

def has_numbers(inputstr):
	if isinstance(inputstr, str):
		return any(char.isdigit() for char in inputstr)
	else:
		return 0

def assign(key, dictionary):
	if key in dictionary.keys():
		return dictionary[key]
	else:
		return 0

def find_no_of_projects_for_each_pm(filename):
	prj_names = []
	prj_manager = []
	unique_prjnames = []
	unique_prjmanager = []
	rel = {}
	prj_nos = {}

	with open(filename) as csvfile: 
		csvreader = csv.reader(csvfile)
		for line in csvreader:
			prj_manager.append(line[2])
			prj_names.append(line[1])
			# the project name is related to project manager
			rel[line[1]] = line[2]

	for i in range(len(prj_names) - 1):
		for j in range(len(prj_names) - 1): 
			if prj_manager[i] == prj_manager[j]:
				if prj_manager[i] in unique_prjmanager:
					pass
				else: 
					unique_prjmanager.append(prj_manager[i])
	
	for i in unique_prjmanager: 
		s = 0
		for j in prj_names:
			if rel[j] == i: 
				s = s + 1
		prj_nos[i] = s

	print(prj_nos)


root = "c:/python/django_files/data/"
filename = "full_data.csv"
filename2 = "cost_forecasting.csv"
name = 'cleaned_data.csv'

file = root + filename
file2 = root + filename2
new_filename = root + name
	
def make_into_clean_data(file1, file2): 
	# allocate dicts for each compnent of new file
	prj_backlog = {}
	prj_q1 = {}
	prj_q2 = {}
	prj_q3 = {}
	prj_q4 = {}
	
	with open(file1) as csvfile, open(file2) as csvfile2:
		# find headers and add them
		csvfile.seek(0)
		csvfile2.seek(0)

		csvreader = csv.reader(csvfile)
		csvreader2 = csv.reader(csvfile2)

		header1 = csvreader.__next__()
		header2 = csvreader2.__next__()
		header3 = []

		for i in header2:
			if i in header1:
				pass
			else:
				header3.append(i)
				header1.append(i)

		try:
			os.remove(new_filename)
			Clean_file = open(new_filename, 'w')
		except OSError:
			Clean_file = open(new_filename, 'w')

		header_writer = csv.writer(Clean_file, delimiter=',')
		header_writer.writerow(header1)
		csvwriter = csv.DictWriter(Clean_file, fieldnames=header1)

		# make a writer that opens another file
		# populate dicts from csvfile2
		for line in csvreader2:
			prj_backlog[line[0][:-2]] = line[3]
			prj_q1[line[0][:-2]] = line[4]
			prj_q2[line[0][:-2]] = line[5]
			prj_q3[line[0][:-2]] = line[6]
			prj_q4[line[0][:-2]] = line[7]

		for line in csvreader:
			line = line + [0,0,0,0,0] # extend line to include new values
			items = zip(header1, line) # the error lies here, zip goes until the smallest array
			item = {}

			for (name, values) in items:
				if values == '' or values == "#VALUE!": 
					values = 0
				if isinstance(values, str) and "%" in values: 
					values.strip('%')
					values = float(value)/100
				if name != "Application Centre" and name != "Project Name" and name != "Project Number": 
					if has_numbers(values) and "K" in values:
						values = values.strip("K")
						values = float(values) * 1000
				if name == "Backlog Revenue":
					values = assign(line[0], prj_backlog)
					# print(values)
				if name == "Q1 Sales 16":
					values = assign(line[0], prj_q1)
				if name == "Q2 Sales 16":
					values = assign(line[0], prj_q2)
				if name == "Q3 Sales 16":
					values = assign(line[0], prj_q3)
				if name == "Q4 Sales 16":
					values = assign(line[0], prj_q4)

				item[name] = values
				if len(item) == 39:
					csvwriter.writerow(item)

make_into_clean_data(file, file2)