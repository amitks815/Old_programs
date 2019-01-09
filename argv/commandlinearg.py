from sys import argv 

print ("value1",argv[0])
print ("value1",argv[1])
print ("value1",argv[2])
print ("value1",argv[3])
print ("value1",argv[4])

list=[argv[1],argv[2],argv[3],argv[4]]
print (list)

for i in list:
	print(int(i))