def func(*a):
	"""this is doc string """
	return sum(a)
print(func(10,20,20))
list=[10,20,30,40]
print(func(*list))
print(func.__doc__)
print(__file__)


def keywordArbArguments(**kwargs): 
	print ("kwargs parameter : ",  kwargs)
Dict = {'a':'append', 'b':'block','x':'extract','y':'yes'}
keywordArbArguments(**Dict)