# a. Call by value
x = 100
def callByValue(x):
	print (id(x), x)
	x = 200
	print (id(x), x)

callByValue(x)
print (id(x), x)