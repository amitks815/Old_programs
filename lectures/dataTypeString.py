## Strings:

x = "This is a string!"
x = 'This is a string!'
print (x)


##Difference between single and double quotes
##Unlike other languages, special characters such as \n have the same meaning with both single ('...') and double ("...") quotes. The only difference between the two is that within single quotes you don’t need to escape " (but you have to escape \') and vice versa.


##String formation
## py2 
count = 10
fruit = 'Apples'
x = "There are %s %s in my basket" % (count, fruit) # its obsolescent in future release of Python

print (x)

##py3
count = 10
x = "There are {} apples in my basket".format(count)

print (x)

count = 10
fruit = 'Apples'
x = "There are {} {} in my basket".format(count, fruit)

print ('This is %s, that is %d' % (100,200)) ##python 2

print ('This is {}, that is {}'.format(100,200))

print ('This is {1}, that is {0} and this too {0}'.format(100,200))


## string extraction
#    0123456789
x = "BestSchool"
print (type(x))
print (x[2])

print ("Length of string is {}".format(len(x)))

x = "BestSchool"
print (x[2:])

x = "BestSchool"
print (x[2:5])

x = "BestSchool"
print (x[:5])

x = "BestSchool"
print (x[:-5])

x = "BestSchool"
print (x[-5:])

x = 'This is a string!'
print (x)


#String methods
x = 'this is a string'

print(x.upper())

s = "I AM GOOD TO LEARN PYTHON"
print(s.lower())

print ('this is a string'.upper())

x = 'this is a string'
print(x.capitalize())

print(x.swapcase())

print(x.find('i'))

print(x.replace('this', 'that'))

print(x.center(30))

s = '     I am string     '

print (s.strip())

print (s.rstrip())

print (s.lstrip())

s = 'stringg'

print (s.strip('g'))

s = 'string\n'

print s
print "________"
print (s.strip('\n'))

s = 'string'
print (s.isalnum()) #[a-zA-Z0-9_]

#print (s.isnumeric())

print (s.isdigit())

## String concatenation 
x1 = " I am a car"
x2 = "My colour is red"

x3 = x1 + x2

print x3

## String repetition 
print x1 * 2

print x1,x2

print '.' * 10

print '*' * 10

print '.' * 10, #What is this comma does here?
print '*' * 10 # These two lines can be combined but more than 80 character line length is a bad style in python

