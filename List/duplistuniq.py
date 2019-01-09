a=['amit','sumit','amit']
b=set()
unique=[]

for i in a:
	if i not in b:
		unique.append(i)
		b.add(i)
print(unique)