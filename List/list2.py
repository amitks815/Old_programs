list1 = [123, 32,56,12,12,32,24,32,98,23,32,24]
print(len(list1))
print(max(list1))
print(min(list1))

#tuple to list
tuple=(12,32,24,32,98,23,32,24)
list2=list(tuple)
print(list2)
#str to list
str='string'
lt=list(str)
print(lt)

#count
list2=[1,2,3,4,5,6,7]
print(list2.count(24))
#append
list2.append(5)
print(list2)

#Index
print(list2.index(1))

#insert
''' here 2 is index value and 6 is value'''
list2.insert(2,6)
print(list2)

#pop
list2.pop(1)
print (list2)

#remove 

#here 4 is value
list2.remove(4)
print(list2)

#delete
#here 4 is index value 
del list[4]
print list

#extend
l=[1,2,3,4]
l2=[3,4,5]
l.extend(l2)
print(l)



