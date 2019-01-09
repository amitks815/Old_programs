x = [1,2,3,4]
def callByRef(x):
	print(id(x), x)
	x += [5,6,7]
	print(id(x), x)

callByRef(x)
print(id(x), x)