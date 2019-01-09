## Tuple
#Where is the benefit of tuples?
#	Tuples are Immutable
#	Tuples are faster than lists.
#	If you know that some data doesn't have to be changed, you should use tuples instead of lists, because this protect your data against accidental changes to these data.
#	Tuples can be used as keys in dictionaries, while lists can't.
#	Tuple can hold any datatypes

x = (1, 2, 3, 4)
print (x)
print (type(x), x)

#Accessing tuple elements
print (x[0])

print (x[-1])

print (x[3:])

print ("Length of tuple is {}".format(len(x)))

x = (1, 2, 3, 4)
x.append(10)

x = 1, 2, 3, 4, 5
print (x)

x = (1, 2, 3, 4, 5, 100, 34, 67, 88, 99)

print (len(x))

print (max(x))

print (min(x))

x = tuple(range(20))

x[2] = 200

print (x)

print (10 in x)

print (10 not in x)

print (100 in x)

print (x.index(2))

print (x.count(2))
