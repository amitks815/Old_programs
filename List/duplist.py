list=[10,20,30,40,50,20,30]

print(list)
l=len(list)
print(l)
for i in range(0,l):
    for j in range(i+1,l-2):
	    if list[i] == list[j]:
		    del list[i]
			
print(list)

