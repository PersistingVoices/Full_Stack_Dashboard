DELETE from csViewer_table1
WHERE rowid not in (
	SELECT min(rowid)
	from csViewer_table1
	GROUP BY PM );
