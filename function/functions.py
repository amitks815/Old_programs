##There are three types of function in Python
#1. Built-in function(print, len)
#2. Functions that are contained within external modules
#3. User defined function

#3. User defined function
Syntax:
def <functionName> (Parameters):
	suit
	return [Expression]

	
"""This is a file"""
def displayStr():
	""" This function intended to explain Function creation in Python """
	print ('Hello, I am function')

##Calling a function
# 1. Without arguments
# 2. Required arguments
# 3. keyword arguments
# 4. Default arguments
# 5. Required and keyword arguments
# 6. Arbitrary arguments(*a)
# 7. Required, keyword and arbitrary arguments
# 8. Arbitrary keyword arguments(**a)
# 9. Required, keyword, arbitrary and keyword  arbitrary arguments

# 1. Without arguments
displayStr()

print ("____________________________")
print (__doc__)
print ("____________________________")
print (displayStr.__doc__)
print ("____________________________")
print (__file__)

# 2. Required arguments
#	a. Call by value
#		In call-by-value, the argument expression is evaluated, and the result of this evaluation is bound to the 	corresponding variable in the function. So, if the expression is a variable, a local copy of its value will be  used, i.e. the variable in the caller's scope will be unchanged when the function returns.
#	b. Call by reference 
#		In call-by-reference evaluation, which is also known as pass-by-reference, a function gets an implicit reference to the argument, rather than a copy of its value. As a consequence, the function can modify the argument, i.e. the value of the variable in the caller's scope can be changed.
	
#	What python exactly does?
#	Python uses a mechanism, which is known as "Call-by-Object", sometimes also called "Call by Object Reference" or "Call by Sharing".
#If you pass immutable arguments like integers, strings or tuples to a function, the passing acts like call-by-value. The object reference is passed to the function parameters. They can't be changed within the function, because they can't be changed at all, i.e. they are immutable. It's different, if we pass mutable arguments. They are also passed by object reference, but they can be changed in place in the function. If we pass a list to a function, we have to consider two cases: Elements of a list can be changed in place, i.e. the list will be changed even in the caller's scope. If a new list is assigned to the name, the old list will not be affected, i.e. the list in the caller's scope will remain untouched. 

# a. Call by value
x = 100
def callByValue(x):
	print (id(x), x)
	x = 200
	print (id(x), x)

callByValue(x)
print (id(x), x) #This means that Python initially behaves like call-by-reference, but as soon as we are changing the value of such a variable, Python "switches" to call-by-value.

#	b. Call by reference 
#Referenced variable altered(the list will be changed even in the caller's scope)
x = [1,2,3,4]
def callByRef(x):
	print(id(x), x)
	x += [5,6,7]
	print(id(x), x)

callByRef(x)
print(id(x), x)

#Referenced variable reassigned(the list in the caller's scope will remain untouched)
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


# Variable referencing can be prevented by passing copy of global variable
x = [1,2,3,4]
def callByCopy(x):
	print(x)
	x += [5,6,7]
	print (x)

callByCopy(x[:])
print(x)


def getTotal(a,b):
	"""Function with two arguments"""
	c = a + b
	print (c)

getTotal()
getTotal(12,30)

def getSub(a,b):
	"""Function with return keyword"""
	c = b - a
	return c
	
result = getSub(10, 20)
print ("Return value : ", result)
print (getSub(100,200))

def getSub(a,b):
	"""Function with/without return keyword of None"""
	c = b - a
	#return
print (getSub(10,20))

def calculator(a,b):
	"""Here we are returning a list/tuple"""
	Sum = a + b
	Sub = b - a
	Mul = a * b
	Div = b / a
	return Sum, Sub, Mul, Div
	#return [Sum, Sub, Mul, Div]

values = calculator(10,20)

print "All values from function ", values

Sum, Sub, Mul, Div = calculator(10,20)
print ("Sum of two value : ", Sum)
print ("Sub of two value : ", Sub)
print ("Mul of two value : ", Mul)
print ("Div of two value : ", Div)

result = calculator(10,20)
print (type(result), result)

# 3. keyword arguments
def getUserName(fn,ln):
	name = fn + ' ' + ln
	return name
	
print (getUserName('Sachin','Tendulkar'))
print (getUserName('Tendulkar','Sachin'))
print (getUserName(fn='Sachin',ln='Tendulkar'))
print (getUserName(ln='Tendulkar',fn='Sachin'))
print (getUserName('Tendulkar',ln='Sachin'))

# 4. Default arguments
def getUserInfo(name="Aditya", age=40):
	print name,age
getUserInfo()
getUserInfo(name="Birla", age=30)
getUserInfo(name="Birla")
getUserInfo(age=25)
getUserInfo('Raj', 45)

# 5. Required and keyword arguments
def getUserInfo(name, age=40,location="Chennai"):
	print name, age, location
	
getUserInfo('Aditya')
getUserInfo('Aditya', age=30, location="Bangalore")
getUserInfo("Birla")
getUserInfo("Birla", age=25)

# 6. Arbitrary arguments(*a)
def getSum(*a):
	print type(a)
	return sum(a)
	
print getSum(10,20,30)
List = [100, 200, 300]
print getSum(*List)
Tuple = (5, 10, 15,100, 200, 300)
print getSum(*Tuple)

Tuple = ()
print getSum(*Tuple)
print getSum()

print getSum(*(input("Enter the values : ")))

def getSum(*a):
	for i in a:
		print "Arbitrary values : %s" % (i)
	return sum(a)
	
print "Sum of arbitrary values %s" % (getSum(10,20,30))

# 7. Required, keyword and arbitrary arguments
def arithmeticMean(first, keyword=10,*values):
	print ("Required : ", first)
        print ("Keyword : ", keyword)
        print ("Arbitrary : ", values)

arithmeticMean(45,32,89,78)
print ("----------------------------")
arithmeticMean(8989.8,78787.78,3453,78778.73)
print ("----------------------------")
arithmeticMean(45,32)
print ("----------------------------")
arithmeticMean(45)

# 8. Arbitrary keyword arguments(**a)
def keywordArbArguments(**kwargs):
	print(kwargs)

Dict = {'a':'append', 'b':'block','x':'extract','y':'yes'}
keywordArbArguments(**Dict)

Dict = {'x':'extract','y':'yes'}
keywordArbArguments(**Dict)

def keywordArbArguments(**kwargs):
	for key in kwargs.keys():
		print "key %s and value %s" % (key, kwargs[key])

Dict = {'a':'append', 'b':'block','x':'extract','y':'yes'}
keywordArbArguments(**Dict)


def keywordArbArguments(a,b,x,y):
	print(a,b,x,y)

Dict = {'a':'append', 'b':'block','x':'extract','y':'yes'}
keywordArbArguments(**Dict)

Tuple = (34, 44)
Dict = {'x':'extract','y':'yes'}
keywordArbArguments(*Tuple, **Dict)

# 9. Required, keyword, arbitrary and keyword  arbitrary arguments
def keywordArbArguments(required, keyword=200, *args, **kwargs): 
	print ("Required parameter : %s" % (required))
	print ("keyword parameter : %s" % (keyword))
	print ("Args parameter : ", args)
	print ("kwargs parameter : ",  kwargs)

#keywordArbArguments(100, 300, 400, 500, a=600, b=700)
#keywordArbArguments(100, 500, a=600, b=700)
#keywordArbArguments(100)
List = [100, 200, 300]
keywordArbArguments(*List)

Dict = {'a':'append', 'b':'block','x':'extract','y':'yes'}
keywordArbArguments(100, **Dict)




