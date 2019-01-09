class robot:
	pass
x=robot()
y=robot()

x.name='kuzat' #instance attribute
x.height=120
y.name='lukat'
y.height=121
robot.name1='kuka'#class attribute
print(robot.name1)

print(robot.__dict__)

print(x.name)
print(y.height)
x.__dict__
print(x.__dict__)
print(y.__dict__)


def f(x):
    f.counter = getattr(f, "counter", 0) + 1 
    return "Monty Python"
        

for i in range(10):
    f(i)
    
print(f.counter)




def hi(obj):
	print("hi ,i am "+obj.name+"!")

class robot:
	pass
x=robot()
x.name='marvin'
hi(x)





