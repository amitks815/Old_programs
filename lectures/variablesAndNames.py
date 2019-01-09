#What is variable or Identifiers?
	#All the variables in Python are class objects
	#Variables are a name space to reserve memory. Variables can vary the value.
	#Identifiers used to identify a variable, function, class, module and object 

#Variable declaration instructions
	#Variables are case sensitive
	#myname and Myname are two different Variables
	#Variables starts with a-z or A-Z or _ followed by one or more alpha numeric characters(a-zA-Z0-9_)
	#myname, Myname and _myname
	#Variables not allowed to include special characters (!@#$%^ &*) except _ 
	#Variables not allowed to start with numerical characters 0-9

	#Variables start with character (myname) meant for public
	#Variables start with single underscore(_myname) meant for private
	#Variables start with double underscore (__name) meant for strongly private
	#Variables starts and ends with two underscore(__myname__) is called language specific variable

# A simple variable may be more complex like below
# variables can store anything like value, any in-built functions, methods, class
# variables can be used to access attributes or methods like 
# x = someObject
# x.attribute = some value
# print (x.attribute)
# print (x.methods)


#Variables in Python two category , 
#	1. Mutable 
#	2. Immutable 
#Mutable object are changeable value but immutable may not
#Immutable objects are may look changing values but they are not
#This can be distinguish by id of value

#Mutable objects are like 
#	List 
#	Dictionaries
#Most of them in python immutable(or fundamental types)
#	Numbers
#	String 
#	Tuples

cars = 5 # left side to operator(= => 'is set to') variable and right is called value
seats = 5
colour = 'Red'
drivers = 5

print "Number of cars available :", cars
print "Total number of passenger can travel : ", cars * 4
print "Available drivers :", drivers

## MULTIPLE ASSIGNMENTS
a=b=c= 1

print (a)
print (b)
print (c)

## Integer value test
a,b = 0,1
print(type(a))

print (a == b)

print (a < b)

print (a > b)
