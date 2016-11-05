import csv
import sqlite3
from string import Template
# import sqlparse as sp
import json

from pathlib import Path
p = str(Path(__file__).parents[3])
srcFile = p + '/Data/BPSimport1.csv'
destFile = p + '/Data/BPSFinal.csv'

headers = ['Project Number','Project Name','WBS Element','WBS Name','','Activity','Customer Number','Customer Name','Cost Type', 'Cost Element Name']

class Classy():

	@staticmethod
	# need a function that writes a new header to the file that is to be uploaded, 
	# not strictly needed but will be useful when viewing csv
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
	# need a function to relate column titles with row fields
	def dictFactory(cursor, row):
		d = {}
		for idx, col in enumerate(cursor.description):
			d[col[0]] = row[idx]
		return (d)

	@staticmethod
	# need a function to return db back into the browser
	def returnCols(C1=None,C2=None,C3=None,C4=None,C5=None, C6=None, C7= None, C8=None):
		# Dont specify the actual path, Django will find the DB
		con = sqlite3.connect('db.sqlite3')
		con.row_factory = Classy.dictFactory
		cur = con.cursor()
		query = ("SELECT " + C1 + " , " + C2 + " , " + C3 + " , " + C4 + " , " + C5 + " , " + C6 + " , " + C7 + ' , ' + C8 + " FROM csViewer_db1")
		cur.execute(query)
		return(cur.fetchall())

	@staticmethod
	# need a function to return the entire db
	def returnAll():
		con = sqlite3.connect('db.sqlite3')
		con.row_factory = Classy.dictFactory
		cur = con.cursor()
		query = ("SELECT * from csViewer_db1")
		cur.execute(query)
		return(cur.fetchall())

	@staticmethod
	# need a function to query return for one column depending on another
	# for example, Select * from table where col1.val = something
	def selectAllWhere(colName, Value):
		con = sqlite3.connect('db.sqlite3')
		con.row_factory = Classy.dictFactory
		cur = con.cursor()
		query = ("SELECT * from csViewer_db1 WHERE " + colName + " = " + '"%s"' %Value)
		cur.execute(query)
		return(cur.fetchall())

	@staticmethod
	# need a method to make fields/ array for processing waterfall graph
	def returnNewFields(col1, col2):
		# con = sqlite3.connect('../../db.sqlite3')
		con = sqlite3.connect('db.sqlite3')
		con.row_factory = Classy.dictFactory
		cur = con.cursor()
		query = ("""	

					INSERT INTO csViewer_waterfall (start, curr, lag, base, pDiff, nDiff, fin, cosElementName)

						SELECT 

						0 as start,

						ABS({var1}-{var2}) AS curr, 

						0  as lag, 

						0  as base, 

						0  as pDiff, 

						0  as nDiff, 
						
						CASE 
							WHEN cosElementName = "Travel Cost - Visa D"
							THEN ABS({var1}-{var2})
						ELSE
							0
						END 
						AS fin, 

						cosElementName

						FROM csViewer_db1
						WHERE {colName} = "{cost}"
						ORDER BY cosElementName

						""").format(colName="cosType",
									cost="Execution Cost",
									var1=col1,
									var2=col2)


		cur.execute(query)


		cur.execute('''
				
				UPDATE csViewer_waterfall
				SET lag = (SELECT w2.curr
							FROM csViewer_waterfall w2
							WHERE w2.id =  csViewer_waterfall.id - 1 
							ORDER BY w2.id ASC
							LIMIT 1
							)

				''')
		

		cur.execute('''
				
				UPDATE csViewer_waterfall
				SET lag = 0 WHERE lag IS NULL

			''')

		cur.execute('''
					UPDATE csViewer_waterfall
					SET start = (SELECT
								CASE 
									WHEN w2.cosElementName = "AE01/ML-03"
									THEN w2.curr
								ELSE
									0
								END
								AS start
								FROM csViewer_waterfall w2
								WHERE w2.id = csViewer_waterfall.id
								ORDER BY w2.id ASC
								LIMIT 1)
			''')
		
		cur.execute('''
				UPDATE csViewer_waterfall
				SET pDiff = (SELECT 
							CASE 
								WHEN (w2.curr - w2.lag) > 0 
								THEN ABS(w2.curr - w2.lag)
							ELSE
								0
							END
							AS pDiff
							FROM csViewer_waterfall w2
							WHERE w2.id = csViewer_waterfall.id
							ORDER BY w2.id ASC
							LIMIT 1
							)
			''')
		
		cur.execute('''
				UPDATE csViewer_waterfall
				SET nDiff = (SELECT 
							CASE 
								WHEN (w2.curr - w2.lag) < 0 
								THEN ABS(w2.curr - w2.lag)
							ELSE
								0
							END
							AS nDiff
							FROM csViewer_waterfall w2
							WHERE w2.id = csViewer_waterfall.id
							ORDER BY w2.id ASC
							LIMIT 1 
							)
			''')

		cur.execute('''
				
				UPDATE csViewer_waterfall
				SET base = (SELECT 
							CASE
								WHEN (w2.pDiff > 0) THEN (w2.curr-w2.pDiff)
							ELSE
								(SELECT
								CASE
								WHEN (w2.curr > w2.lag) THEN w2.lag
								ELSE w2.curr 
								END)
							END
							AS base
							FROM csViewer_waterfall w2
							WHERE w2.id = csViewer_waterfall.id
							ORDER BY w2.id ASC
							LIMIT 1
							)
			''')

		cur.execute('''
			
				UPDATE csViewer_waterfall
				SET base = 0, pDiff = 0, nDiff = 0 WHERE cosElementName = 'AE01/ML-03'

			
			''')

		cur.execute('''

				UPDATE csViewer_waterfall
				SET base = 0 WHERE cosElementName = 'Travel Cost - Visa D'
			
			''')

		# cur.execute("SELECT base, id, cosElementName FROM csViewer_waterfall WHERE base = 0 ")
		# cur.execute("SELECT * FROM csViewer_waterfall WHERE cosElementName = 'Travel Cost - Visa D' ")
		cur.execute("""DELETE FROM csViewer_waterfall WHERE rowid NOT IN 
						(SELECT MAX(rowid) FROM csViewer_waterfall GROUP BY cosElementName)

			""")

		cur.execute("SELECT * FROM csViewer_waterfall")
		return(cur.fetchall())


# C = Classy()
# col1 = "ps4"
# col2 = "ps0"
# for i in range(0, len(C.returnNewFields(col1, col2))):
# 	print(C.returnNewFields(col1,col2)[i], '\n')