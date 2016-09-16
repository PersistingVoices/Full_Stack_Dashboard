import csv

root = "C:/Python/Django_Files/Data/"
filename = "full_data.csv"
file = root + filename

# find unique pm's 
# find no of projects by each pm
# find PS1, PS4, PS1vsPS4, Q1, Q2, Q3, Q4, c-r and total sales relating to each PM

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
