import csv

# Clean up this class, Classy aint classy yet
class Classy:
	## make unique list from list
	@staticmethod
	def make_unique(lst):
		myset = set(lst)
		Ulist = list(myset)
		# print(Ulist)
		return(Ulist)

	@staticmethod
	def find_no_of_projects_for_each_pm(filename):
		P_names = []
		P_manager = []
		unique_pm = []
		rel = {}
		P_nos = {}
		
		with open(filename) as csvfile:
			csvreader = csv.reader(csvfile)
			header = csvreader.__next__()
			for line in csvreader:
				if len(line) == 39:
					P_manager.append(line[2])
					P_names.append(line[1])
					# the project name is related to project manager
					rel[line[1]] = line[2]

		# after file closes, make unique list
		# unique = Classy.make_unique(P_names)
		unique_pm = Classy.make_unique(P_manager)
		# find the number of unique pm's in the original list
		for i in unique_pm:
			s = 0
			for j in P_names:
				if rel[j] == i:
					s = s + 1
				P_nos[i] = s
		# print(P_nos)
		return(P_nos, unique_pm)

	@staticmethod
	def template_for_sigmaX_V_PM(filename, X):
		pm = []
		unique_pm = []

		with open(filename) as csvfile:
			csvreader = csv.reader(csvfile)
			header = csvfile.__next__()
			for line in csvreader:
				pm.append(line[2])
			unique_pm = Classy.make_unique(pm)

			csvfile.seek(0)
			header = csvfile.__next__()
			item = {}
			for line in csvreader:
				for i in unique_pm:
					if len(line) == 39:
						if i == line[2]:
							if i in item:
								plc = float(item[i])
								# print(line[X])
								if line[X] != "":
									item[i] = plc + float(line[X])
							else:
								if line[X] != "":
									item[i] = float(line[X])
			return(item)

	# function to make sure data is in place in list,
	# before being uploaded into server
	@staticmethod
	def before_upload(new):
		PS1vsPS4 = {}
		P_nos = []; unique_pm = [];
		# find number of project numbers fora each pm
		P_nos, unique_pm = Classy.find_no_of_projects_for_each_pm(new)
		# PS1 revenue line[7]
		PS1 = Classy.template_for_sigmaX_V_PM(new, 7)
		# PS4 revenue line[11]
		PS4 = Classy.template_for_sigmaX_V_PM(new, 8)
		## for field 'PS1vsPS4'
		## PS1 Margin:line[10], PS4 margin:line[14], PS4 revenue:line[11]
		PS1_Margin = Classy.template_for_sigmaX_V_PM(new, 10)
		PS4_Marign = Classy.template_for_sigmaX_V_PM(new, 14)

		for i in unique_pm :
			if i in PS4_Marign:
				PS1vsPS4[i] = (PS4_Marign[i] - PS1_Margin[i]) * PS4[i]
		
		# q1 sales = line[35]
		Q1_sales = Classy.template_for_sigmaX_V_PM(new, 35)
		print(Q1_sales)
		# q2 sales = line[36]
		Q2_sales = Classy.template_for_sigmaX_V_PM(new, 36)
		# q3 sales = line[37]
		Q3_sales = Classy.template_for_sigmaX_V_PM(new, 37) 
		# q4 sales = line[38]
		Q4_sales = Classy.template_for_sigmaX_V_PM(new, 38)
		# c-r% line[28]
		crp = Classy.template_for_sigmaX_V_PM(new, 28)
		# c-r line[27]
		cr = Classy.template_for_sigmaX_V_PM(new, 27)

		return unique_pm, P_nos, PS1, PS4, PS1vsPS4, Q1_sales, Q2_sales, Q3_sales, Q4_sales, crp, cr
