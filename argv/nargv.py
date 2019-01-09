def getSum(*a):

	return sum(a)
	
print(getSum(10,20,30))
List = [100, 200, 300]
print(getSum(*List))


def kwargval(**kwarg):
	for key in kwarg.keys():
		print(key)
dict={'a':'abc','b':'cde','c':'efg'}
kwargval(**dict)

