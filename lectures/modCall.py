# Syntax : import <Module name>
# 'import' is used to bringing python file into local scope or downloading all function to local
# Module function can be accessed by <Name of module>.<Function/Method>
# Importing module done only once

import modFruits

fruit = modFruits
fruit.banana()
fruit.orange()
fruit.apple()

print __doc__
print modFruits.__doc__
print modFruits.orange.__doc__

print __file__

print fruit.name
print fruit.x

# Importing a only specific function
from modFruits import banana
banana()

# Importing all name-spaces from module  
from modFruits import *
print (name)

from modFruits import banana, orange
banana()
orange()

# Importing a more than one module
import modFruits, modVegetables

modFruits.orange()
modVegetables.carrot()

# How module searched while importing
import sys
print (sys.path)

#expanding the path variables
sys.path.append('C:\\MyWorks\\photographs')


# Getting all contents and help 
import modFruits
contents = dir(modFruits)
print (contents)
Help = help(modFruits)
print (Help)

#Calling dir() without an argument, a list with the names in the current local scope is returned
x =10
s = "String"
List = [1,2,3,4]
print dir()

# To get a list of the Built-in functions, exceptions, and other objects
#python 3
import builtins
BuiltIns = dir(builtins)
print (BuiltIns)


# Find a local and global scope variables
import modFruits
Locals = modFruits.calculator(10,20)
print (Locals)


x = 10
def calculator(a,b):
	"""Here we are returning a list/tuple"""
	Sum = a + b
	Sub = b - a
	Mul = a * b
	Div = b / a
	

Globals = globals()
print (Globals)

# Create alias for module
import modVegetables as veg
veg.carrot()

# Create a local name for function
import modVegetables
beet = modVegetables.beetroot()
print (beet)

#Importing module only once
import modJustOnce
import modJustOnce #Nothing to do in second time importing
# Importing again 
reload(modJustOnce) #Python 2


# Reload in python 3
from imp import reload
import modJustOnce
import modJustOnce
reload(modJustOnce)













