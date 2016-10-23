import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def ret_row():
	con = sqlite3.connect("../db.sqlite3")
	con.row_factory = dict_factory
	cur = con.cursor()
	cur.execute("select PM,PS1 from csViewer_table1")
	print (cur.fetchall())

ret_row()