##Dictionaries
#	Python has one more aggregator type Dictionaries, it also called as Associative array or Hash in other programming language.
#	Its stored information in the form of key and value pair
#	Its a Mutable
#	Its not ordered
#	Dict key is unique value

cars = {'Alto' : 'Maruti', 'X320' : 'BMW', 'Ventto' : 'VolksWagon', 'i20' : 'Hyundai', 'Amaze' : 'Honda'}

print (cars)

print cars['Alto']
print cars['i20']

# method of keyword arguments(more details in functions)
cars = dict(Alto = 'Maruti', X320 = 'BMW', Ventto = 'VolksWagon', i20 = 'Hyundai', Amaze = 'Honda') 

print (cars)

print (cars.keys())

print (cars.values())

cars['Figo'] = 'Ford'
print (cars)

del(cars['i20'])

print(cars)

print min(cars)
print max(cars)

print ('Alto' in cars)

print ('Audi' in cars)

print ('Audi' not in cars)

print ('Maruti' in cars)
print ('Maruti' in cars.values())

print (cars['Audi'])

print (cars.get('Audi'))

print (cars.get('Audi', 'Not found'))

print (cars.pop('Amaze'))

print (cars.pop('x320'))


print ('This is {a}, that is {b}'.format(a=11,b=33))

d = dict(a = 888, b = 777)

print ('This is {a}, that is {b}'.format(**d))

#Nested dict
x = {'123' : {'name' : "Sathish", 'sal' : "1500000", 'dept' : "Developer"}, 'Siva': ["Sathish",1500000,"Developer"]}

print x['123']['name']
print x['123']['sal']
print x['123']['dept']
print x['Siva'][0]
