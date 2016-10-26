import csv
import os
import sys

pth = (os.path.join (os.getcwd(), 'Data/BPSimport1.csv'))
pth2 = (os.path.join (os.getcwd(), 'Data/BPSFinal.csv'))

with open(pth) as file:
	csvreader = csv.reader(file)
	for i in range(5):
			csvreader.__next__()
	header = []
	header = csvreader.__next__()
	header[0] = 'Project Number'
	header[1] = 'Project Name'
	header[2] = 'WBS Element'
	header[3] = 'WBS Name'
	header[4] = ''
	header[5] = 'Activity'
	header[6] = 'Customer Number'
	header[7] = 'Customer Name'
	header[8] = 'Cost Type'
	header[9] = 'Cost Element Name'
	with open(pth2, 'w') as file2:
		csv.writer(file2).writerow(header)
		for line in csvreader:
			csv.writer(file2).writerow(line)
