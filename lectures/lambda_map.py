l=[1,2,3,4]

a=(list(map(lambda x:x*x,l)))
print(a) 
b=(list(filter(lambda x:x>2,l)))
print(b)
# c=(list(reduce(lambda x,y:x*y,l)))
# print(c)