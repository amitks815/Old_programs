#!/usr/bin/python

class JustCounter:
   name = "Python"
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
print counter.name
#print counter.__secretCount

#Python protects those members by internally changing the name to include the class name. You can access such attributes as object._className__attrName.
print counter._JustCounter__secretCount

print dir(counter)
