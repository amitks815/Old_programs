"""This example for discussing about module concept"""
## Module is nothing but a grouping a related functions into a file
# All python files are module
# There is no special declaration applied to create module

def apple():
	print("Colour of apple is red and green")
	
def banana():
	print("Banana is good for diet")

def orange():
	"""Here is the doc string"""
	print("Orange has a more fibre content")
	
name = "Zara"

global x 
x = 100

def Trun():
	pass


def calculator(a,b):
	"""Here we are returning a list/tuple"""
	Sum = a + b
	Sub = b - a
	Mul = a * b
	Div = b / a
	return locals()

'''
print "Language specific variables\n"    
print __name__ 
print __package__
print "Language specific variables\n"
'''
	
