p=[2,3,4,5,5]
le=len(p)
sum=0
#print(p)
for j in p:
	l=p[0:]
	a=j
	l.remove(j)
	print(l)
	r=len(l)
	for i in range(0,r):
		sum+=l[i]
		b=sum/a
	sum=0
	print(b)