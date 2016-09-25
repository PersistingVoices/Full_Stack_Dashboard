import csv

class Tab1:
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

	@staticmethod
	def template_for_sigmaX_V_PM(filename, X):
		pm = []
		unique_pm = []

		with open(filename) as csvfile:
			csvreader = csv.reader(csvfile)
			header = csvfile.__next__()
			for line in csvreader:
				if len(line) == 39:
					pm.append(line[2])
			unique_pm = Tab1.make_unique(pm)

			csvfile.seek(0)
			header = csvfile.__next__()
			item = {}
			for line in csvreader:
				for i in unique_pm:
					if len(line) == 39:
						if i == line[2]:
							if i in item:
								plc = int(item[i])
								item[i] = plc + int(line[X])
							else:
								item[i] = int(line[X])
			return(item)

root1 = "C:/Python/Django_Files/Data/"
root2 = "/home/shriram/Documents/Python/work/Django/Data/"
filename = "full_data.csv"
filename2 = "cost_forecasting.csv"
name = 'Cleaned_Data.csv'

file1 = root2 + filename
file2 = root2 + filename2
new = root2 + name

T = Tab1()
PS1 = T.template_for_sigmaX_V_PM(new, 7)
print(PS1)
PS2 = T.template_for_sigmaX_V_PM(new, 8)
print(PS2)

## for field 'PS4'
## for field 'PS1vsPS4'
## for field 'Q1 sales'
## for field 'Q2 sales'
## for field 'Q3 sales'
## for field 'Q4 sales'
## for field 'cr'
