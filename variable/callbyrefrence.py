x = [1,2,3,4]
def callByRef(x):
	print(x)
	x = [5,6,7]
	print (x)

callByRef(x)
print(x)

x = [1,2,3,4]
def callByRef(x, y=[]):
	print(x)
	y.append(x)
	print (y)

callByRef(99)
callByRef(88,[])
callByRef(77)
print(x)