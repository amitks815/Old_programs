#List
#List is an collection of objects
#The main properties of Python lists:
#	They are ordered
#	The contain arbitrary objects
#	Elements of a list can be accessed by an index
#	They are arbitrarily nestable, i.e. they can contain other lists as sublists
#	Variable size
#	They mutable, i.e. they elements of a list can be changed

x = [] # An empty list

print (type(x), x)

# Integers list
x = [1, 2, 3, 4, 5]
print (x)

# Mixed data types
x = [123, "Strings", 34.904]
print(x)

# Strings list
x = ["Chennai", "Bangalore", "Hyderabad", "Kerala"]
print(x)

## Accessing a list elements
#    0    1   2  3   4   5   6 
x = [10, 20, 30, 40, 50, 60, 70]

print (x[0])
print (x[2])

print (x[2:])
print (x[:3])
print (x[1:4])
print (x[:])
print (x[::2])
print (x[-1])
print (x[-2])

x.append(10)
print (x)

x.insert(0,10)
print (x)
x.insert(2,100)
print (x)

print (len(x))
del(x[0])
print (x)
print (len(x))

x.remove(2)
print (x)

print (max(x))

print (min(x))

print list('myclass')

print type(range(10)), range(10)

x = range(20)
print (x)

x[3] = 200
print (x)

#Checking if an Element is Contained in list
print (10 in x)

print (10 not in x)

print (100 in x)

x  = [1,2,3,4,5,6,7,2,4,7,2,3]

print (x.index(2))

print (x.count(2))

x.extend(range(5))
print (x)

print (x.pop())

print (x.pop(0))

# A nested list
#       0       1         2      3 3.0      3.1            4
x = ["Apple", "Orange", "Banana",["Mango", "Pineapple"], "Grape"]

print (x[0])
print (x[3])
print (x[3][0])
print (x[3][1])
print (x[4])

#       0       1          2     3 3.0  3.1   3.2 3.2.0   3.2.1   3.3   4
x = ["Apple", "Orange", "Banana",[ 100, 200,   [  20.09,  30.23], 400], "Grape"    ]
print (x[3])
print (x[3][0])
print (x[3][2])
print (x[3][2][1])

## concatenation of list
colours1 = ["red", "green","blue"]
colours2 = ["black", "white"]
colours = colours1 + colours2
print(colours)

colours = ["red", "green","blue"]
colours += ["black", "white"]
print(colours)

## list Repetitions 
print (colours * 4)





