#!/usr/bin/python
'''
Special Methods
Classes in Python programming language can implement certain operations with special method names. These methods are not called directly, but by a specific language syntax. This is similar to what is known as operator overloading in C++ or Ruby.

You can change the meaning of an operator in Python depending upon the operands used. This practice is known as operating overloading.

Python operators work for built-in classes. But same operator behaves differently with different types. For example, the + operator will, perform arithmetic addition on two numbers, merge two lists and concatenate two strings.

This feature in Python, that allows same operator to have different meaning according to the context is called operator overloading

Special Functions in Python
Class functions that begins with double underscore __ are called special functions in Python. This is because, well, they are not ordinary. The __init__() function we defined above, is one of them. It gets called every time we create a new object of that class. There are a ton of special functions in Python.

'''
class Vector:
   def __init__(self, a, b): 
      self.a = a 
      self.b = b 

   def __str__(self):
      return 'Vector str (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      print 'self.a : ', self.a
      print 'self.b : ', self.b
      print 'other.a : ', other.a
      print 'other.b : ', other.b
      return Vector(self.a + other.a, self.b + other.b)
   def __sub__(self,other):
      return Vector(self.a - other.a, self.b - other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1
print v2
print str(v1)
print str(40)
print v1 - v2


class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

p1 = Point(2,3)
p2 = Point(-1,2)
print p1 + p2


class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

p1 = Point(2,3)
print(p1)

'''
Turns out, that this same method is invoked when we use the built-in function str() or format()
'''

print str(p1)
print format(p1)

#when you do str(p1) or format(p1), Python is internally doing p1.__str__(). Hence the name, special functions.
#What actually happens is that, when you do p1 + p2, Python will call p1.__add__(p2) which in turn is Point.__add__(p1,p2). Similarly, we can overload other operators as well.

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)

p1 = Point(2,3)
p2 = Point(-1,2)
print(p1 + p2)


class Book():

    def __init__(self, title, author, pages):

        print("A book is created")

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):

        return "Title:{0} , author:{1}, pages:{2} ".format(
            self.title, self.author, self.pages)

    def __len__(self):

        return self.pages

    def __del__(self):

        print("A book is destroyed")

book = Book("Inside Steve's Brain", "Leander Kahney", 304)

print(book)
print(len(book))
del book


