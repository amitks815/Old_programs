with open('avengers.jpg','rb') as rf:
	with open('avengers_copy.jpg','wb') as wf:
		for line in rf :
			wf.write(line)