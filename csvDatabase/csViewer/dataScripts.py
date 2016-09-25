
import csv, os

# make a dictionary relating the field names of models with the actual column name



##
def has_numbers(inputstr):
	if isinstance(inputstr, str):
		return any(char.isdigit() for char in inputstr)
	else:
		return 0

##
def assign(key, dictionary):
	if key in dictionary.keys():
		return dictionary[key]
	else:
		return '0'

def strip_commas(value):
	v = value.replace(",", "")
	if v == "":
		v = 0
	return(v)
##
def clean_data(file1, file2, new): 
	# allocate dicts for each compnent of new file
	prj_backlog = {}; prj_q1 = {}; prj_q2 = {}; prj_q3 = {}; prj_q4 = {}
	
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
			os.remove(new)
			Clean_file = open(new, 'w')
		except OSError:
			Clean_file = open(new, 'w')

		header_writer = csv.writer(Clean_file, delimiter=',')
		header_writer.writerow(header1)
		csvwriter = csv.DictWriter(Clean_file, fieldnames=header1)

		# make a writer that opens another file
		# populate dicts from csvfile2
		for line in csvreader2:
			prj_backlog[line[0][:-2]] = strip_commas(line[3])
			prj_q1[line[0][:-2]] = strip_commas(line[4])
			prj_q2[line[0][:-2]] = strip_commas(line[5])
			prj_q3[line[0][:-2]] = strip_commas(line[6])
			prj_q4[line[0][:-2]] = strip_commas(line[7])
		# print(prj_q4)

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
