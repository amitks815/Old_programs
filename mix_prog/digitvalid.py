a=int(input("enter the number:"))
b=int(input("enter the number:"))

c=int(input("enter the number:"))
list=[]
list.append(a)
list.append(b)
list.append(c)
for i in range(0,3):
	for j in range(0,3):
		for k in range(0,3):
			if(i!=j&j!=k&k!=i):
				print(list[i],list[j],list[k])



