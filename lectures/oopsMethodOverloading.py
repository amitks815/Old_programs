class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __len__(self):
        return 100
p1 = Point(2,3)

'''
Turns out, that this same method is invoked when we use the built-in function str() or format()
'''

print str(10) 
print str(p1)
print format(p1)

#when you do str(p1) or format(p1), Python is internally doing p1.__str__(). Hence the name, special functions.


l = [1,2,3]

print len(l)
print len(p1)
