## Loops
# Simplest form of loop in Python is While
#syntax
while <Condition>:
	suits

a = 1
while a < 20:
	print (a)
	a = a + 1
	
	
a = 1
while a < 20:
	print (a, end=' ')
	a = a + 1

a = 1
while a < 20:
	print (a, end=' ** ')
	#print (a)
	a = a + 1

## Fibonacci series generation

a,b = 0,1
while b < 50:
	print (b, end=' ')
	a,b=b,a+b

	
## For loop
# its a iterator 

syntax :
for <variable> in <input>:
	<suits>

T = (1, 2, 3, 4, 5)
for i in T:
	print (i)

L = [1, 2, 3, 4, 5]
for i in L:
	print (i)

s = "Heroine"
for i in s:
	print (i)
	
s = "Heroine"
for i in s:
	print (i, end=' ')

cars = {'Alto' : 'Maruti', 'X320' : 'BMW', 'Ventto' :     'VolksWagon', 'i20' : 'Hyundai', 'Amaze' : 'Honda'}

for i in cars.keys():
	print (cars[i]) 	
## get the index value of iterator

s = "Heroine"
for index, value in enumerate(s):
	print (index, value)

s = "This is a string"
for index, value in enumerate(s):
	if value == 's': print ('index {} is an s'.format(index))
	

## Loop control
s = "classroom"
for i in s:
	if i == 's':continue
	print (i, end='')

s = "classroom"
for i in s:
	if i == 's':break
	print (i, end='')
	
s = "This is a string"
for i in s:
	print (i, end='')
else:
	print ("\nElse statement")

for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print (n, 'equals', x, '*', n/x)
			break
		else:
			# loop fell through without finding a factor
			print (n, 'is a prime number')

s = "This is a string"
i = 0
while i < len(s):
	print (s[i], end='')
	i += 1
else:
	print ("\nElse statement")

	
## Range function
for i in range(20):
	print(i)
	
for i in range(1,20):
	print(i)

for i in range(0,20):
	print(i)
	
for i in range(0,20,2):
	print(i)
	
