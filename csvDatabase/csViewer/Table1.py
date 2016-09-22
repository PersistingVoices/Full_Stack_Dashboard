import csv

root = "C:/Python/Django_Files/Data/"
filename = "full_data.csv"
filename2 = "cost_forecasting.csv"
name = 'cleaned_data.csv'

file = root + filename
file2 = root + filename2
new_filename = root + name

class Tab1():
	## make unique list from list
	def make_unique(lst):
		Ulist = []
		for i in range(len(lst) - 1):
			for j in range(len(lst) - 1):
				if lst[i] == lst[j]:
					if lst[i] in Ulist:
						pass
					else:
						Ulist.append(lst[i])
		return(Ulist)

	## for field 'P_nos'
	def find_no_of_projects_for_each_pm(filename):
		P_names = []
		P_manager = []
		unique_pnames = []
		unique_pm = []
		rel = {}
		P_nos = {}

		with open(filename) as csvfile:
			csvreader = csv.reader(csvfile)
			for line in csvreader:
				P_manager.append(line[2])
				P_names.append(line[1])
				# the project name is related to project manager
				rel[line[1]] = line[2]

		# after file closes, make unique list
		unique_pm = make_unique(P_names)

		# find the number of unique pm's in the original list
		for i in unique_pm: 
			s = 0
			for j in P_names:
				if rel[j] == i:
					s = s + 1
			P_nos[i] = s

		return(P_nos)

	## for field 'PS1'
	def find_sum_of_PS1_for_each_pm(filename):
		PS1 = [] 
		pm = []
		unique_pm = []
		# use rel for storing the final values
		# rel contains pm names, and their ps1's
		rel = {}
		individual_s = 0
		s = {}

		with open(filename) as csvfile:
			csvreader = csv.reader(csvfile)
			for line in csvreader:
				# store all these names
				# and make them unique later	
				
				pm.append([line[2]])

			# make unique pm list 
			unique_pm = Tab1.make_unique(pm)
			
			csvfile.seek(0)
			for line in csvreader:
				for i in unique_pm:
					if i in 
	## for field 'PS4'
	## for field 'PS1vsPS4'
	## for field 'Q1 sales'
	## for field 'Q2 sales'
	## for field 'Q3 sales'
	## for field 'Q4 sales'
	## for field 'cr'
	
Tab1.find_sum_of_PS1_for_each_pm(new_filename)