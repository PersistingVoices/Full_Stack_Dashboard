import csv
import sqlite3
# from pathlib import Path
# p = str(Path(__file__).parents[3])
# srcFile = p + '/Data/BPSimport1.csv'
# destFile = p + '/Data/BPSFinal.csv'

headers = ['Project Number','Project Name','WBS Element','WBS Name','','Activity','Customer Number','Customer Name','Cost Type', 'Cost Element Name']

class Classy():

	@staticmethod
	def writeHeader(srcFile, destFile):
		with open(srcFile) as F:
			csvreader = csv.reader(F)
			for i in range(5):
				csvreader.__next__()
			header = []
			newLine = []
			header = csvreader.__next__()
			# write new header from headers array
			for i in range(10):
				header[i] = headers[i]
			# write into new file
			with open(destFile, 'w') as F2:
				csv.writer(F2).writerow(header)
				for line in csvreader:
					newLine = line
					for i in range(len(newLine)):
						if newLine[i] == '':
							newLine[i] = 0
						else:
							pass
					csv.writer(F2).writerow(newLine)
	@staticmethod
	def dictFactory(cursor, row):
		d = {}
		for idx, col in enumerate(cursor.description):
			d[col[0]] = row[idx]
		return (d)

	@staticmethod
	def returnCols(C1=None,C2=None,C3=None,C4=None,C5=None, C6=None, C7= None, C8=None):
		# Dont specify the actual path, Django will find the DB
		con = sqlite3.connect('db.sqlite3')
		con.row_factory = Classy.dictFactory
		cur = con.cursor()
		query = ("SELECT " + C1 + " , " + C2 + " , " + C3 + " , " + C4 + " , " + C5 + " , " + C6 + " , " + C7 + ' , ' + C8 + " FROM csViewer_db1")
		cur.execute(query)
		return(cur.fetchall())

# C = Classy()
# C.writeHeader(srcFile, destFile)
