## Anonymous function
#Syntax
#lambda arg1, arg2, ... : expression
s = lambda a, b: a + b

print s(20,30)

#lambda in map()
#Syntax of map: map(function, sequence)
#map() applies the function func to all the elements of the sequence seq. It returns a new list with the elements changed by func
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print Fahrenheit
celsius = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)
print celsius

a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
print (map(lambda x,y:x+y, a,b)) #More than one sequence can be passed but it should have same length
print (map(lambda x,y,z:x+y+z, a,b,c))
print (map(lambda x,y,z:x+y-z, a,b,c))

def square(x):
        return (x**2)
def cube(x):
        return (x**3)

funcs = [square, cube]
for r in range(5):
    value = map(lambda x: x(r), funcs)
    print value
	
def mymap(aFunc, aSeq):
	result = []
	for x in aSeq: result.append(aFunc(x))
	return result

list(map(sqr, [1, 2, 3]))

mymap(sqr, [1, 2, 3])

print (pow(2,10))

list(map(pow,[2, 3, 4], [10, 11, 12]))

'''
If function is None, the identity function is assumed; if there are multiple arguments, map() returns a list consisting of tuples containing the corresponding items from all iterables (a kind of transpose operation). The iterable arguments may be a sequence or any iterable object; the result is always a list:
'''
m = [1,2,3]
n = [1,4,9]
new_tuple = map(None, m, n)
new_tuple

###lambda in filter
#syntax of filter: filter(function, List)
#The filter offers an elegant way to filter out all the elements of a list, for which the function returns True
List = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, List)
print result
result = filter(lambda x: x % 2 == 0, List)
print result

#lambda in reduce
#syntax of reduce(function, sequence)
#The function reduce(func, seq) continually applies the function func() to the sequence seq. It returns a single value.
#func(func(s1, s2),s3), ... , sn

print (reduce(lambda x,y: x+y, [1,2,3,4,5]))
print (reduce(lambda x,y: x+y, ['a','b']))

#py 3
from functools import reduce
reduce( (lambda x, y: x * y), [1, 2, 3, 4] )

#Determining the maximum of a list of numerical values by using reduce:
func = lambda a,b: a if (a > b) else b
print (reduce(func, [47,11,4,10,97,100,13,2]))
