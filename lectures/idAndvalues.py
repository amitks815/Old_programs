## ID and Values
#variable = Object, Object are referenced to variable
#Strings, integers and Tuple are Immutable object
#List, Dictionaries are mutable object
#Immutable objects ids are same even if you change the variable
x = 20
print (id(x), x)

y = 20
print (id(y), y)

z = y
print (id(z), z)

y = 10
print (id(y), y)

#compare id and value
#value
print (x == y) 

#ID compare
print (x is y)

print (x is z)

a = 'Bang'
b = 'Bang'

print (a == b)
print (a is b)

a = 'Bang!'
b = 'Bang!'

print (a == b)
print (a is b)

a = 'westregion'
b = 'westregion'

print (a == b)
print (a is b)

a = 'west-region!'
b = 'west-region!'

print (a == b)
print (a is b)

#Mutable object

cars = dict(Alto = 'Maruti')

xcars = dict(Alto = 'Maruti')

print (cars == xcars)

print (cars is xcars)

xcars = dict(Alto = 'Maruti', i20 = 'Hundai', city = 'Honda')

print (cars == xcars)

print (cars is xcars)

