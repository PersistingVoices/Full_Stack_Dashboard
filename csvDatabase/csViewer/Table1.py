import csv

class Tab1():
	## make unique list from list
	def make_unique(lst):
		Ulst = []
		for i in range(len(lst) - 1):
			for j in range(len(lst) - 1):
				if lst[i] == lst[j]:
					if lst[i] in Ulst:
						pass
					else:
						Ulist.appen(lst[i])
		return(Ulst)

	## for field 'Prj_nos'
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

		return(prj_nos)

	## for field 'PS1'
	def find_sum_of_PS1_for_each_pm(filename):
		PS1 = [];s = [];pm = [];unique_pm = []
		# use rel for storing the final values
		# rel contains pm names, and their ps1's
		rel = {}

		with open(filename) as csvfile:
			csvreader = csv.reader(csvfile)
			for line in csvreader:
				# store all these names
				# and make them unique later
				pm.append(line[2])
				PS1.append(line[7])

	## for field 'PS4'
	## for field 'PS1vsPS4'
	## for field 'Q1 sales'
	## for field 'Q2 sales'
	## for field 'Q3 sales'
	## for field 'Q4 sales'
	## for field 'cr'
	
