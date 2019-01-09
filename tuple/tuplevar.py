"""5.	Assign tuple items into an individual variables """
tup=(1,2,3,4)
l=['a','b','c','d']
for i in range(0,len(tup)):
	p=tup[i]
	print("%s:%d" %(l[i],p))