user0={
	'carol':'C',
	'roberta':'java',
	'pedro':'python',
	'charles':'ruby',
	'lindo':'java',
	}
gens=['lindo','viktor','pedro','nicolas']

for i in gens:
	if i in user0.keys():
		print( i + ' ty')
	else:
		print( i +' doit')
