beg=2000
end=2500
count=0
l=[]
for i in range(beg,end):
	if (i%7==0) and (i%5!=0):
		count=count+1
		l.append(str(i))
print(l)
print('')

print (','.join(l))
print("count",count)