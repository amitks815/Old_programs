from sys import argv

print("My script is ", argv[0])
print("My name is ", argv[1])
print("My age is ", argv[2]) #type is str
print("I am from ", argv[3])

list=[argv[0],argv[1],argv[2],argv[3]]
print (list)

list.pop(0)
print(list)

print(argv)