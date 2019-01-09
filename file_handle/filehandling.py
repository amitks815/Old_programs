#file handle!

with open("hello1.txt",'w') as f:
	f.write('test')
	f.seek(6)
	f.write('hello')






#readmode 
	'''sizetoread = 10
	fo=f.read(sizetoread)
	print(fo,end='')
	f.seek(0)
	fo=f.read(sizetoread)
	print(fo,end='')
	print(f.tell())

	while len(fo)>0:
		print(fo,end='')
		fo=f.read(sizetoread)'''


	