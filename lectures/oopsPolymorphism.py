#Polymorphism is the process of using an operator or function in different ways for different data input. In practical terms, polymorphism means that if class B inherits from class A, it doesn't have to inherit everything about class A; it can do some of the things that class A does differently.

'''
a = "alfa"
b = (1, 2, 3, 4)
c = ['o', 'm', 'e', 'g', 'a']

print(a[2])
print(b[1])
print(c[3])

str1 = "I am Python"
str2 = "Learning"

str3 = str1 + str2

print str3

c = ['o', 'm', 'e', 'g', 'a']
d = [1,2,3,4]

e = c + d

print e

x = 10
y = 20
z = x + y

print z

'''
#Polymorphism is mostly used when dealing with inheritance.

class Animal:
   def __init__(self, name=''):
      self.name = name

   def talk(self):
       print "Animal"
      #pass

class Cat(Animal):
   def talk(self):
      print("Meow!")

class Dog(Animal):
   def talk(self):
      print("Woof!")

a = Animal()
a.talk()

c = Cat("Missy")
c.talk()

d = Dog("Rocky")
d.talk()

#Here we have two species: a dog and a cat. Both are animals. The Dog class and the Cat class inherit the Animal class. They have a talk() method, which gives different output for them.

